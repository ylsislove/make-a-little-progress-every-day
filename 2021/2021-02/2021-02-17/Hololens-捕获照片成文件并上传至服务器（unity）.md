# Hololens-捕获照片成文件并上传至服务器（unity）

## 环境
* Hololen2
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
            photoCaptureObject.TakePhotoAsync(filePath, PhotoCaptureFileOutputFormat.JPG, OnCapturedPhotoToDisk);
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
        photoCaptureObject.Dispose();
        photoCaptureObject = null;

        captureIsActive = false;
        StartCoroutine(CustomVisionAnalyser.Instance.AnalyseLastImageCaptured(filePath));
    }
}
```

```c#
using System.Collections;
using System.IO;
using UnityEngine;
using UnityEngine.Networking;

public class CustomVisionAnalyser : MonoBehaviour
{

    public static CustomVisionAnalyser Instance;
    private string predictionEndpoint = "http://192.168.0.103:5000/upload";

    /// <summary>
    /// Byte array of the image to submit for analysis
    /// </summary>
    [HideInInspector] public byte[] imageBytes;

    private void Awake()
    {
        Instance = this;
    }

    /// <summary>
    /// Call the Computer Vision Service to submit the image.
    /// </summary>
    public IEnumerator AnalyseLastImageCaptured(string imagePath)
    {
        WWWForm webForm = new WWWForm();

        // Gets a byte array out of the saved image
        imageBytes = GetImageAsByteArray(imagePath);

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

    /// <summary>
    /// Returns the contents of the specified image file as a byte array.
    /// </summary>
    static byte[] GetImageAsByteArray(string imageFilePath)
    {
        FileStream fileStream = new FileStream(imageFilePath, FileMode.Open, FileAccess.Read);
        BinaryReader binaryReader = new BinaryReader(fileStream);
        return binaryReader.ReadBytes((int)fileStream.Length);
    }
}
```
