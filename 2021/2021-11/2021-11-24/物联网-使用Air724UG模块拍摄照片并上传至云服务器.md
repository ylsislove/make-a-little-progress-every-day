# 物联网-使用Air724UG模块拍摄照片并上传至云服务器

  - [前言](#%E5%89%8D%E8%A8%80)
  - [基础知识](#%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86)
  - [编写 TCP 客户端代码](#%E7%BC%96%E5%86%99-tcp-%E5%AE%A2%E6%88%B7%E7%AB%AF%E4%BB%A3%E7%A0%81)
  - [编写 TCP 服务端代码](#%E7%BC%96%E5%86%99-tcp-%E6%9C%8D%E5%8A%A1%E7%AB%AF%E4%BB%A3%E7%A0%81)

## 前言
最近在做物联网的项目，有一个需求是要每隔一段时间要拍摄一张现场的图片并上传至云服务器保存。在查阅了很多资料后，发现这方面的资料是真的匮乏。同时，tb 上的摄像头产品也太高度集成了，很难进行二次开发。一次机缘巧合下，在逛 tb 的时候偶然发现一款产品，就是如下图所示 Air724UG 模块，自带 4G 通信模块和摄像头接口，而且成本也比较便宜，带通信卡和摄像头总价格不超过 80，简直就是完美符合我需求的天选产品。同时该系列产品的官方网站上也给出了很多代码 demo，非常有利于初学者的学习。最终，在经历了几天的学习后，终于成功把这个需求实现了，开心ヾ(•ω•`)o，于是在此记录下来，希望能帮助到其他有需要的小伙伴们~

![Air724UG](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211124202038.png)

![Air724UG](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20211124202306.png)

## 基础知识
如果买了这个模块，首先把卖家写的五篇开发文档看一下，如下
* [1-Air724UG(4G全网通GPRS)开发-硬件使用说明](https://www.cnblogs.com/yangfengwu/p/15122303.html)
* [2-Air724UG(4G全网通GPRS)开发-下载AT指令固件](https://www.cnblogs.com/yangfengwu/p/15125406.html)
* [200-Air724UG(4G全网通GPRS)开发-下载和运行第一个lua程序](https://www.cnblogs.com/yangfengwu/p/15163863.html)
* [201-Air724UG模块(4G全网通GPRS开发)-模块测试-测试SD卡和扬声器(喇叭)播放功能](https://www.cnblogs.com/yangfengwu/p/15163986.html)
* [202-Air724UG模块(4G全网通GPRS开发)-模块测试-摄像头扫码,LCD显示摄像头图像](https://www.cnblogs.com/yangfengwu/p/15164453.html)

最重要的是最后一个文档，因为我们后面要修改这里面的代码。

看完文档后，应该就会对 Air724UG 模块有了大致的了解，同时我们也会发觉二次开发是基于 Lua 语言的。有小伙伴可能就会问，没学过 Lua 语言肿么办

莫慌，因为合宙官方给出了很多案例的示例代码，包括上面第五个文档里面用的摄像头案例的代码。我们可以打开代码看一下，官方的代码规范写的很好，每一句代码几乎都有注释，这就非常有利于我们初学者的学习~

博主也是在大致浏览了下代码后，尝试性的将 socket 的示例代码和 camera 的示例代码融合起来，成功的解决了这个需求，下面就具体看看修改后的代码吧~

## 编写 TCP 客户端代码
目前拍摄的需求已经通过默认的 camera 示例代码实现了，下面要实现的就是如何把照片上传到云端。搞过开发的同学应该都大致了解 socket 这个东西，我们各种网络通信的基础就是 socket，我们用 socket 也可以很快搭建一个 tcp 服务器，这样就相当于我们的摄像头模块是 tcp 客户端，部署了代码的云服务器是 tcp 服务器端，两端连通以后，就可以实现将照片传输到云端啦~

下面先看一下 TCP 客户端具体代码

主要用到的就是官方 `demo\socket\async\asyncSocket` 的案例和 `demo\camera` 这两个案例，我们按照 socket 案例的 main 文件修改 camera 案例的 main 文件，修改后如下

```lua
--必须在这个位置定义PROJECT和VERSION变量
--PROJECT：ascii string类型，可以随便定义，只要不使用,就行
--VERSION：ascii string类型，如果使用Luat物联云平台固件升级的功能，必须按照"X.X.X"定义，X表示1位数字；否则可随便定义
PROJECT = "CAMERA"
VERSION = "2.0.0"

--加载日志功能模块，并且设置日志输出等级
--如果关闭调用log模块接口输出的日志，等级设置为log.LOG_SILENT即可
require "log"
LOG_LEVEL = log.LOGLEVEL_TRACE
--[[
如果使用UART输出日志，打开这行注释的代码"--log.openTrace(true,1,115200)"即可，根据自己的需求修改此接口的参数
如果要彻底关闭脚本中的输出日志（包括调用log模块接口和Lua标准print接口输出的日志），执行log.openTrace(false,第二个参数跟调用openTrace接口打开日志的第二个参数相同)，例如：
1、没有调用过sys.opntrace配置日志输出端口或者最后一次是调用log.openTrace(true,nil,921600)配置日志输出端口，此时要关闭输出日志，直接调用log.openTrace(false)即可
2、最后一次是调用log.openTrace(true,1,115200)配置日志输出端口，此时要关闭输出日志，直接调用log.openTrace(false,1)即可
]]
--log.openTrace(true,1,115200)

require "sys"
require "utils"
require "patch"
require "pins"

require "net"
--每1分钟查询一次GSM信号强度
--每1分钟查询一次基站信息
-- net.startQueryAll(60000, 60000)
--8秒后查询第一次csq
net.startQueryAll(8 * 1000, 60 * 1000)

--此处关闭RNDIS网卡功能
--否则，模块通过USB连接电脑后，会在电脑的网络适配器中枚举一个RNDIS网卡，电脑默认使用此网卡上网，导致模块使用的sim卡流量流失
--如果项目中需要打开此功能，把ril.request("AT+RNDISCALL=0,1")修改为ril.request("AT+RNDISCALL=1,1")即可
--注意：core固件：V0030以及之后的版本、V3028以及之后的版本，才以稳定地支持此功能
ril.request("AT+RNDISCALL=0,1")

--加载控制台调试功能模块（此处代码配置的是uart1，波特率115200）
--此功能模块不是必须的，根据项目需求决定是否加载
--使用时注意：控制台使用的uart不要和其他功能使用的uart冲突
--使用说明参考demo/console下的《console功能使用说明.docx》
--require "console"
--console.setup(1, 115200)

--加载硬件看门狗功能模块
--根据自己的硬件配置决定：1、是否加载此功能模块；2、配置Luat模块复位单片机引脚和互相喂狗引脚
--合宙官方出售的Air201开发板上有硬件看门狗，所以使用官方Air201开发板时，必须加载此功能模块
--[[
require "wdt"
wdt.setup(pio.P0_30, pio.P0_31)
]]

--加载网络指示灯和LTE指示灯功能模块
--根据自己的项目需求和硬件配置决定：1、是否加载此功能模块；2、配置指示灯引脚
--合宙官方出售的Air720U开发板上的网络指示灯引脚为pio.P0_1，LTE指示灯引脚为pio.P0_4
require "netLed"
pmd.ldoset(2,pmd.LDO_VLCD)
netLed.setup(true,pio.P0_1,pio.P0_4)
--网络指示灯功能模块中，默认配置了各种工作状态下指示灯的闪烁规律，参考netLed.lua中ledBlinkTime配置的默认值
--如果默认值满足不了需求，此处调用netLed.updateBlinkTime去配置闪烁时长

--加载错误日志管理功能模块【强烈建议打开此功能】
--如下2行代码，只是简单的演示如何使用errDump功能，详情参考errDump的api
require "errDump"
errDump.request("udp://ota.airm2m.com:9072")

--加载远程升级功能模块【强烈建议打开此功能】
--如下3行代码，只是简单的演示如何使用update功能，详情参考update的api以及demo/update
--PRODUCT_KEY = "v32xEAKsGTIEQxtqgwCldp5aPlcnPs3K"
--require "update"
--update.request()

require"color_lcd_spi_st7735"
--require"color_lcd_spi_gc9106l"
require"testCamera"

-- 系统工具
require "misc"
require "testSocket"
require "ntp"

ntp.timeSync(1,function()log.info("----------------> AutoTimeSync is Done ! <----------------")end)

--启动系统框架
sys.init(0, 0)
sys.run()
```

然后在 camera 案例下添加一个 `testSocket.lua` 文件，编写代码如下

```lua
--- testSocket
-- @module asyncSocket
-- @author AIRM2M
-- @license MIT
-- @copyright openLuat.com
-- @release 2018.10.27
require "socket"
module(..., package.seeall)

-- 此处的IP和端口请填上你自己的socket服务器和端口
-- local ip, port, c = "180.97.80.55", "12415"
local ip, port, c = "xxx.xxx.xxx.xxx", "9999"

-- 异步接口演示代码
local asyncClient
sys.taskInit(function()
    while true do
        while not socket.isReady() do sys.wait(1000) end
        asyncClient = socket.tcp()
        while not asyncClient:connect(ip, port) do sys.wait(2000) end
        while asyncClient:asyncSelect() do end
        asyncClient:close()
    end
end)

-- 测试代码,用于发送消息给socket
function sendFile(size)
sys.taskInit(
    function()
        while not socket.isReady() do sys.wait(2000) end
        local fileHandle = io.open("/testCamera.jpg","rb")
        if not fileHandle then
            log.error("testALiYun.otaCb1 open file error")
            return
        end
        log.info("-----------------------------------------------start send photo")
        asyncClient:asyncSend(size)
        while true do
            local data = fileHandle:read(size)
            if not data then break end
            asyncClient:asyncSend(data)
        end
        log.info("-----------------------------------------------end send photo")
        fileHandle:close()
    end
)
end
```

注意把上面的 ip 地址换成你后面部署 tcp 服务器端的云服务器的 ip 地址

这个文件编写完成以后，就可以在 `testCamera.lua` 文件里面调用这个函数了，`testCamera.lua` 文件具体编辑如下，其中中间省略了一些没有修改的代码

```lua
--- 模块功能：camera功能测试.
-- @author openLuat
-- @module fs.testFs
-- @license MIT
-- @copyright openLuat
-- @release 2018.03.27

module(...,package.seeall)

require"pm"
require"scanCode"
require"utils"
require"common"
require"testUartSentFile"
require"testSocket"

local WIDTH,HEIGHT = disp.getlcdinfo()
local DEFAULT_WIDTH,DEFAULT_HEIGHT = 320,240

-- 扫码结果回调函数
-- @bool result，true或者false，true表示扫码成功，false表示超时失败
-- @string[opt=nil] codeType，result为true时，表示扫码类型；result为false时，为nil；支持QR-Code和CODE-128两种类型
-- @string[opt=nil] codeStr，result为true时，表示扫码结果的字符串；result为false时，为nil
local function scanCodeCb(result,codeType,codeStr)
    ...
end

local bf302A_sdr =
{
	...
}

local gc6153 =
{
	...
}

local gc0310_ddr =
{
	...
}

local gc0310_ddr_big =
{
	....
}

local gc0310_sdr =
{
	...
}

function scan()
    ...
end

-- 拍照并显示
function takePhotoAndDisplay()
    ...
end

-- 拍照并通过uart1发送出去
function takePhotoAndSendToUart()
    ...
end

-- 拍照并通过socket发送出去
function takePhotoAndSendToSocket()
    --唤醒系统
    pm.wake("testTakePhoto")
    --打开摄像头
    disp.cameraopen(1,0,0,1)
    --disp.cameraopen(1,0,0,0)  --因目前core中还有问题没解决，所以不能关闭隔行隔列
    --打开摄像头预览
    --如果有LCD，使用LCD的宽和高
    --如果无LCD，宽度设置为240像素，高度设置为320像素，240*320是Air268F支持的最大分辨率
    disp.camerapreview(0,0,0,0,DEFAULT_WIDTH,DEFAULT_HEIGHT)
    --设置照片的宽和高像素并且开始拍照
    --此处设置的宽和高和预览时的保持一致
    disp.cameracapture(DEFAULT_WIDTH,DEFAULT_HEIGHT)
    --设置照片保存路径
    disp.camerasavephoto("/testCamera.jpg")
    log.info("-----------------------------------------------testCamera.takePhotoAndSendToSocket fileSize",io.fileSize("/testCamera.jpg"))
    --关闭摄像头预览
    disp.camerapreviewclose()
    --关闭摄像头
    disp.cameraclose()
    --允许系统休眠
    pm.sleep("testTakePhoto")

    testSocket.sendFile(io.fileSize("/testCamera.jpg"))

    sys.timerStart(takePhotoAndSendToSocket,1*60*1000)
end


-- sys.timerStart(takePhotoAndDisplay,1000)
-- sys.timerStart(takePhotoAndSendToUart,1000)
sys.timerStart(takePhotoAndSendToSocket,10000)
-- sys.timerStart(scan,1000)
```

修改完这三个文件之后，我们就可以把这个案例烧录到 Air724UG 模块上了，这样我们 TCP 客户端就弄好了，下面来看下 TCP 服务器端的代码吧~

## 编写 TCP 服务端代码
这里 socket 的编程可以用 python 写，也可以用 go 或其他语言写，因为我最近在学 go，所以我就用 go 来编写 tcp 服务器端的代码啦，具体 `main.go` 文件编写如下

```go
package main

import (
	"bytes"
	"encoding/binary"
	"encoding/hex"
	"fmt"
	"log"
	"net"
	"os"
	"strconv"
	"time"
)

func GetDetailTime() string {
	now := time.Now()
	return fmt.Sprintf("%02d%02d%02d%02d%02d%02d", now.Year(), int(now.Month()),
		now.Day(), now.Hour(), now.Minute(), now.Second())
}

func handleClient(conn *net.TCPConn) {
	var buf [256]byte
	var imageData [10 * 1024]byte
	for {
		n, _ := conn.Read(buf[0:])
		fmt.Println("------------------------receive bytes--------------------", n, string(buf[0:n]))
		size, _ := strconv.Atoi(string(buf[0:n]))
		fmt.Println("------------------------file size--------------------", size)

		i := 0
		for i < size {
			n, _ := conn.Read(imageData[i:])
			i += n
		}
		encodedStr := hex.EncodeToString(imageData[0:i])
		fmt.Println("------------------------received bytes--------------------", i)
		fmt.Println(encodedStr)

		imgName := fmt.Sprintf("%s.jpg", GetDetailTime())
		byte2image(imageData, i, imgName)
	}
}

func byte2image(b [10 * 1024]byte, n int, path string) {
	fp, err := os.Create(path)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer fp.Close()

	buf := new(bytes.Buffer)
	binary.Write(buf, binary.LittleEndian, b[0:n])
	fp.Write(buf.Bytes())
}

func main() {
	address := net.TCPAddr{
		IP:   net.ParseIP("0.0.0.0"), // 把字符串IP地址转换为net.IP类型
		Port: 9999,
	}
	fmt.Println("v2.0 server listen at ", address.IP, address.Port)
	listener, err := net.ListenTCP("tcp4", &address) // 创建TCP4服务器端监听器
	if err != nil {
		log.Fatal(err) // Println + os.Exit(1)
	}
	for {
		conn, err := listener.AcceptTCP()
		if err != nil {
			log.Fatal(err) // 错误直接退出
		}
		fmt.Println("remote address:", conn.RemoteAddr())
		// go echo(conn)
		go handleClient(conn)
	}
}
```

编写完成之后，可以通过在当前目录下运行如下命令将代码打包成 Linux 可执行文件

```
SET CGO_ENABLED=0
SET GOOS=linux
SET GOARCH=amd64
go build main.go
```

这样就可以在当前目录下生成 `main` 可执行文件了，这也是我喜欢 go 的原因，同样的代码，可以方便的打包成 windows 可执行文件和 linux 可执行文件，十分的方便

将打包生成的 `main` 文件传输到云服务器上，然后执行，TCP 服务器端代码就运行起来了，记得开放云服务器防火墙的对应端口

接下来只要保证 TCP 客户端代码里的 ip 地址和端口正确，照片就可以顺利的上传到云服务器上，然后保存到可执行文件的目录下了~

如果这篇文件对你有帮助，记得给博主点个赞支持一下呀 (✿◡‿◡)
