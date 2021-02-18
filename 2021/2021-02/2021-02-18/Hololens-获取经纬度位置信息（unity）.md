# Hololens-获取经纬度位置信息（unity）

  - [环境](#%E7%8E%AF%E5%A2%83)
  - [相关代码](#%E7%9B%B8%E5%85%B3%E4%BB%A3%E7%A0%81)
  - [效果展示](#%E6%95%88%E6%9E%9C%E5%B1%95%E7%A4%BA)
  - [注意事项](#%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9)

## 环境
* Hololen2
* Windows 10
* Unity 2019.4.19f1c1
* Visual Studio 2019
* MRTK 2.5.4

## 相关代码
```csharp
using System.Collections;
using TMPro;
using UnityEngine;

public class LocationService : MonoBehaviour
{

    public TextMeshPro textMeshPro;
    private bool locationAvailable = false;

    private void Start()
    {
        StartGPS()
    }

    public void StartGPS()
    {
        StartCoroutine(EnableGPS());
    }

    IEnumerator EnableGPS()
    {
        if (!Input.location.isEnabledByUser)
        {
            Debug.Log("User location info is disabled");
            yield break; 
        }

        Input.location.Start(10.0f, 10.0f);// 启动定位服务
        int maxWait = 20;
        while (Input.location.status == LocationServiceStatus.Initializing && maxWait > 0)
        {
            // 暂停协同程序的执行(1秒)  
            yield return new WaitForSeconds(1);
            maxWait--;
        }

        if (maxWait < 1)
        {
            Debug.Log("Init GPS service time out");
            yield break;
        }

        if (Input.location.status == LocationServiceStatus.Failed)
        {
            Debug.Log("Unable to determine device location");
            yield break;
        }
        else
        {
            SceneManager.Instance.PrintMessage("Enable Location Service Success"); // 自定义组件
            locationAvailable = true;
            StartCoroutine(GetLocationInfo());
        }
    }

    IEnumerator GetLocationInfo()
    {
        while (locationAvailable)
        {
            // 0.5秒更新一次
            yield return new WaitForSeconds(0.5f);
            if (textMeshPro != null)
            {
                textMeshPro.text = "";
                textMeshPro.text += $"Lng: {Input.location.lastData.longitude}\n";
                textMeshPro.text += $"Lat: {Input.location.lastData.latitude}\n";
                textMeshPro.text += $"Alt: {Input.location.lastData.altitude}\n";
                textMeshPro.text += $"HAcc: {Input.location.lastData.horizontalAccuracy}\n";
            }
        }
    }

    public void StopGPS()
    {
        locationAvailable = false;
        Input.location.Stop();
        SceneManager.Instance.PrintMessage("Close GPS"); // 自定义组件
    }
}
```

## 效果展示
[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210218233512.jpg)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210218233512.jpg)

## 注意事项
注意打包 untiy 程序时要设置允许 Location 权限，前面那个捕获照片的也要设置允许 webcam 权限。
