# NLP-使用NVIDIA开源NeMo模型进行语音识别和生成
## 前言
> 会话式人工智能正在改变我们与计算机的交互方式。它包括三个令人兴奋的人工智能研究领域：自动语言识别（Automatic Speech Recognition，ASR）、自然语言处理（Natural Language Processing，NLP）和语言合成（或文本到语音，Text-to-Speech，TTS）。NVIDIA 的目标是通过让研究人员和从业人员更容易地访问、重用和建立这些领域的最新构建模块和预训练模型，使这些领域的进展能够实现民主化并得到加速。

## 安装
```bash
pip install nemo_toolkit[all]==1.0.0b1
```
运行这条命令后它还会在电脑上安装最新版的 pytorch，如果不想用最新版的，可以去 [Pytorch](https://pytorch.org/get-started/locally/) 找到自己想要用的版本，运行自动生成的命令即可，如
```bash
pip3 install torch==1.8.1+cu102 torchvision==0.9.1+cu102 torchaudio===0.8.1 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html
```

运行 `import nemo` 可能会报一个错误是 `ImportError: cannot import name 'Batch' from 'torchtext.data' (xxx\lib\site-packages\torchtext\data\__init__.py)`。这里可能的原因是 torchtext 造成的冲突，直接运行 `pip uninstall torchtext` 将其卸载掉，再次运行 `import nemo` 成功。

## 导入NeMo工具库与相关工具类
```python
import nemo
import nemo.collections.asr as nemo_asr
# import nemo.collections.nlp as nemo_nlp
import nemo.collections.tts as nemo_tts
import soundfile as sf
```
把 `nemo_nlp` 注掉是因为导入失败了，会报 `ModuleNotFoundError: No module named 'transformers.tokenization_bert` 错误。头秃，暂时还没找到解决办法，所以只能先不用这个模块了

## 加载相关模型
```python
# 加载语音识别模型- QuartzNet
quartznet = nemo_asr.models.EncDecCTCModel.from_pretrained(model_name="QuartzNet15x5Base-En")
# 加载神经机器翻译模型
# nmt_model = nemo_nlp.models.MTEncDecModel.from_pretrained(model_name="nmt_en_zh_transformer6x6").cuda()
# 加载从文本到频谱生成模型
spectrogram_generator = nemo_tts.models.Tacotron2Model.from_pretrained(model_name="Tacotron2-22050Hz")
# 加载声码器
vocoder = nemo_tts.models.WaveGlowModel.from_pretrained(model_name="WaveGlow-22050Hz")
```

## 定义函数从文字到语音
```python
def text_to_audio(text):
    parsed = spectrogram_generator.parse(text)
    spectrogram = spectrogram_generator.generate_spectrogram(tokens=parsed)
    audio = vocoder.convert_spectrogram_to_audio(spec=spectrogram)
    return audio.to('cpu').detach().numpy()
```

## 文字转语音
```python
# 输入文字
print(f"Input your favorite sentence ")
text = input()
# 生成音频文件写入磁盘并播放
sf.write("speech.wav", text_to_audio(text)[0], 22050)
```

## 参考链接
* [使用英伟达NeMo让你的文字会说话，零基础即可实现自然语音生成任务 | 附代码](https://mp.weixin.qq.com/s/pZkB1mhZ1Em0WXUEUY670w)
* [NVIDIA开源NeMo：基于PyTorch，允许快速创建会话式人工智能模型](https://aijishu.com/a/1060000000144270)
