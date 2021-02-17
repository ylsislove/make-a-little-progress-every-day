# Hololens-捕获照片到磁盘（unity）

## 环境
* Windows 10
* Unity 2019.4.19f1c1
* Visual Studio 2019
* MRTK 2.5.4

## 相关代码
```c#
using System;
using System.IO;
using System.Linq;
using UnityEngine;
using UnityEngine.Windows.WebCam;

public class MyPhotoCapture : MonoBehaviour
{
    PhotoCapture photoCaptureObject = null;

    internal string filePath = string.Empty;
    internal bool captureIsActive;

    private void Start()
    {
        // Clean up the LocalState folder of this application from all photos stored
        DirectoryInfo info = new DirectoryInfo(Application.persistentDataPath);
        var fileInfo = info.GetFiles();
        foreach (var file in fileInfo)
        {
            try
            {
                file.Delete();
            }
            catch (Exception)
            {
                Debug.LogFormat("Cannot delete file: ", file.Name);
            }
        }

        SceneManager.Instance.SetCameraStatus("Ready");

        //StartCapture();
    }

    public void StartCapture()
    {
        if (!captureIsActive)
        {
            captureIsActive = true;
            SceneManager.Instance.SetCameraStatus("Capturing Image");
            PhotoCapture.CreateAsync(false, OnPhotoCaptureCreated);
        }
        else
        {
            captureIsActive = false;
            SceneManager.Instance.SetCameraStatus("Ready");
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
            pixelFormat = CapturePixelFormat.BGRA32
        };

        captureObject.StartPhotoModeAsync(cameraParams, OnPhotoModeStarted);

    }

    private void OnPhotoModeStarted(PhotoCapture.PhotoCaptureResult result)
    {
        if (result.success)
        {
            string filename = string.Format(@"CapturedImage_{0}.jpg", DateTime.Now.ToString("yyyyMMddHHmmss"));
            filePath = Path.Combine(Application.persistentDataPath, filename);
            Debug.Log(filename);
            Debug.Log(filePath);
            photoCaptureObject.TakePhotoAsync(filePath, PhotoCaptureFileOutputFormat.JPG, OnCapturedPhotoToDisk);
            //photoCaptureObject.TakePhotoAsync(OnCapturedPhotoToMemory);
        }
        else
        {
            Debug.LogError("Unable to start photo mode!");
        }
    }

    void OnCapturedPhotoToDisk(PhotoCapture.PhotoCaptureResult result)
    {
        if (result.success)
        {
            Debug.Log("Saved Photo to disk!");
            photoCaptureObject.StopPhotoModeAsync(OnStoppedPhotoMode);
        }
        else
        {
            Debug.Log("Failed to save Photo to disk");
        }
    }

    void OnStoppedPhotoMode(PhotoCapture.PhotoCaptureResult result)
    {
        Debug.Log("销毁");
        photoCaptureObject.Dispose();
        photoCaptureObject = null;

        SceneManager.Instance.SetCameraStatus("Uploading Image");
        StartCoroutine(CustomVisionAnalyser.Instance.AnalyseLastImageCaptured(filePath));
    }
}
```
