# Python-实现录音小程序

## 安装
```powershell
pip install pyaudio
```

如果你是 Python3.7 的版本，可能会有报错，安装不成功，解决办法如下：

首先要下载安装相应的 whl 文件，下载地址是 [https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)，在这里选择 PyAudio‑0.2.11‑cp37‑cp37m‑win_amd64.whl（其中cp37代表python版本号3.7，amd64代表64位）。

[![图片可能因为网络原因掉线了，请刷新或直接点我查看图片~](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210206004602.png)](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20210206004602.png)

下载之后在终端切换到下载的 whl 文件目录，直接用 pip 安装刚刚下载好的 PyAudio‑0.2.11‑cp37‑cp37m‑win_amd64.whl

```powershell
pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
```

操作完毕，启动 Python，导入 `from pyaudio import PyAudio, paInt16`，未报错则安装成功。

## 代码如下
```python
import wave
from pyaudio import PyAudio, paInt16

# 参数设定
framerate = 8000
NUM_SAMPLES = 2000
channels = 1
sampwidth = 2
TIME = 2

# 写 Wav 文件
def save_wave_file(filename, data):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b''.join(data))
    wf.close()

# 录音
def my_record():
    pa = PyAudio()
    stream = pa.open(format=paInt16,
                     channels=1,
                     rate=framerate,
                     input=True,
                     frames_per_buffer=NUM_SAMPLES)
    my_buf = []
    count = 0
    # 控制录音时间
    while count < TIME * 20:
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
    print(my_buf)
    save_wave_file('01.wav', my_buf)
    stream.close()

# 播放音频
chunk = 2014
def play():
    wf = wave.open(r'01.wav', 'rb')
    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    while True:
        data = wf.readframes(chunk)
        if data == '':
            break
        stream.write(data)
    stream.close()
    p.terminate()

if __name__ == '__main__':
    my_record()
    print('over')
    play()

```
