# Hololens-捕获照片到内存并上传至服务器（unity）

## 环境
* Hololen2
* Windows 10
* Unity 2019.4.19f1c1
* Visual Studio 2019
* MRTK 2.5.4

## 相关代码
```csharp
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using UnityEngine;
using UnityEngine.Windows.WebCam;

public class MyPhotoCapture : MonoBehaviour
{
    PhotoCapture photoCaptureObject = null;

    internal bool captureIsActive;

    private void Start()
    {
        //StartCapture();
    }

    public void StartCapture()
    {
        if (!captureIsActive)
        {
            captureIsActive = true;
            PhotoCapture.CreateAsync(false, OnPhotoCaptureCreated);
        }
        else
        {
            captureIsActive = false;
        }
    }

    void OnPhotoCaptureCreated(PhotoCapture captureObject)
    {
        photoCaptureObject = captureObject;

        var cameraResolution = PhotoCapture.SupportedResolutions
                .OrderByDescending((res) => res.width * res.height)
                .First();

        var cameraParams = new CameraParameters()
        {
            hologramOpacity = 0f,
            cameraResolutionWidth = cameraResolution.width,
            cameraResolutionHeight = cameraResolution.height,
            pixelFormat = CapturePixelFormat.JPEG
        };

        captureObject.StartPhotoModeAsync(cameraParams, OnPhotoModeStarted);

    }

    private void OnPhotoModeStarted(PhotoCapture.PhotoCaptureResult result)
    {
        if (result.success)
        {
             
            photoCaptureObject.TakePhotoAsync((photoCaptureResult, frame) =>
            {
                if (photoCaptureResult.success)
                {
                    Debug.Log("Photo capture done.");

                    var buffer = new List<byte>();
                    frame.CopyRawImageDataIntoBuffer(buffer);
                    StartCoroutine(CustomVisionAnalyser.Instance.AnalyseLastImageCaptured(buffer.ToArray()));
                }
                photoCaptureObject.StopPhotoModeAsync(OnStoppedPhotoMode);
            });
        }
        else
        {
            Debug.LogError("Unable to start photo mode!");
        }
    }

    void OnStoppedPhotoMode(PhotoCapture.PhotoCaptureResult result)
    {
        photoCaptureObject.Dispose();
        photoCaptureObject = null;

        captureIsActive = false;
    }
}
```

```csharp
using System.Collections;
using System.IO;
using UnityEngine;
using UnityEngine.Networking;

public class CustomVisionAnalyser : MonoBehaviour
{

    public static CustomVisionAnalyser Instance;
    private string predictionEndpoint = "http://192.168.0.103:5000/upload";

    private void Awake()
    {
        Instance = this;
    }

    /// <summary>
    /// Call the Computer Vision Service to submit the image.
    /// </summary>
    public IEnumerator AnalyseLastImageCaptured(byte[] imageBytes)
    {
        WWWForm webForm = new WWWForm();

        // 将图片byte数组添加进表单
        webForm.AddBinaryData("file", imageBytes, "photo.jpg");

        // 将图片上传到服务器
        using (UnityWebRequest unityWebRequest = UnityWebRequest.Post(predictionEndpoint, webForm))
        {
            // The download handler will help receiving the analysis from Azure
            unityWebRequest.downloadHandler = new DownloadHandlerBuffer();

            // Send the request
            yield return unityWebRequest.SendWebRequest();

            if (unityWebRequest.isHttpError || unityWebRequest.isNetworkError)
            {
                Debug.Log(unityWebRequest.error);
            }
            else
            {
                string response = unityWebRequest.downloadHandler.text;
                Debug.Log(response);
            }
        }
    }
}
```
