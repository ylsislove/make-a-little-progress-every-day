# golang-request请求的分发及body体的复用

## 前言
需求是这样的：客户端向服务端发起一个 POST 请求，包含一张图片和其他 Form 表单数据。服务端需要把图片保存到指定位置，然后把图片路径和 Form 表单中的其他数据保存到数据库；同时，需要把传来的图片数据分发到另一个服务端口进行视觉分析，然后拿到分析结果返回给客户端。

这里就涉及到如何在 golang 中构建一个新的 request 请求，复用 `r.body` 和 `r.header`，进行发送并获取到响应结果。

由于 `r.body` 不能被 `ioutil.ReadAll` 重复读取，所以这里 `r.body` 的复用就需要一些技巧。相关代码如下~

## 代码
Image 结构体
```golang
type Image struct {
	ID        int
	Longitude float64
	Latitude  float64
	Altitude  float64
	ImgUrl    string
	Income    Income
	Time      string
}
```

视觉分析结果结构体
```golang
package model

type Income struct {
	Low    float64 `json:"低收入,omitemty"`
	MLow   float64 `json:"中低收入,omitemty"`
	Middle float64 `json:"中等收入,omitemty"`
	MHigh  float64 `json:"中高收入,omitemty"`
	High   float64 `json:"高收入,omitemty"`
	Other  float64 `json:"其他,omitemty"`
}
```

请求处理函数
```golang
package handler

import (
	"ArGIS-Cloud/dao"
	"ArGIS-Cloud/model"
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"io/ioutil"
	"mime/multipart"
	"net/http"
	"os"
	"strconv"
	"strings"
)

const UPLOAD_PATH string = "upload/"

// SaveAndPredict 保存图片路径和表单数据到数据库，并返回视觉分析结果
func SaveAndPredict(w http.ResponseWriter, r *http.Request) {
	var img model.Image
	var income model.Income
	var bodyByte []byte

	// 拷贝一份request的Body
	if r.Body != nil {
		bodyByte, _ = ioutil.ReadAll(r.Body)
		// 把刚刚读出来的再写进去，不然后面解析表单数据就解析不到了
		r.Body = ioutil.NopCloser(bytes.NewBuffer(bodyByte))
	}

	// 解析位置数据
	img.Longitude, _ = strconv.ParseFloat(r.FormValue("longitude"), 64)
	img.Latitude, _ = strconv.ParseFloat(r.FormValue("latitude"), 64)
	img.Altitude, _ = strconv.ParseFloat(r.FormValue("altitude"), 64)

	// 解析图片
	imgFile, imgHead, imgErr := r.FormFile("image")
	if imgErr != nil {
		fmt.Println("imgErr", imgErr)
		return
	}
	defer imgFile.Close()

	// 保存图片
	imgFormat := strings.Split(imgHead.Filename, ".")
	img.ImgUrl = r.FormValue("longitude") + "_" + r.FormValue("latitude") + "." + imgFormat[len(imgFormat)-1]
	saveImage(UPLOAD_PATH+img.ImgUrl, imgFile)

	// 复用Body和header进行分发请求，获取视觉分析结果，并写入response
	bodyCopy := ioutil.NopCloser(bytes.NewBuffer(bodyByte))
	resp, _ := sendRequest("POST", "http://localhost:3000/stream_predict", bodyCopy, r.Header)
	json.Unmarshal(resp, &income)
	json.NewEncoder(w).Encode(income)

	// 将数据保存到数据库
	img.Income = income
	dao.SaveImage(&img)
}

// 保存图片到指定路径
func saveImage(path string, imgFile multipart.File) (err error) {
	image, err := os.Create(path)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer image.Close()

	_, err = io.Copy(image, imgFile)
	if err != nil {
		fmt.Println(err)
	}
	return
}

// 分发 request 请求
func sendRequest(method string, url string, body io.Reader, header http.Header) (resp []byte, err error) {
	// 1. 创建req
	req, err := http.NewRequest(method, url, body)
	if err != nil {
		return
	}

	// 2. 设置headers
	req.Header = header

	// 3、发送http请求
	client := &http.Client{}
	response, err := client.Do(req)
	if err != nil {
		return
	}
	defer response.Body.Close()

	if response.StatusCode != 200 {
		fmt.Println(response.StatusCode)
		return
	}

	// 4、返回响应结果
	resp, err = ioutil.ReadAll(response.Body)
	return
}
```

