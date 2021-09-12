# YOLOv5-模型部署

## 模型转换
进入 `C:\Program Files (x86)\Intel\openvino_2021.4.582\deployment_tools\model_optimizer` 目录下，运行：
```
pip install -r requirements_onnx.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
python .\mo_onnx.py --input_model E:/code/python/yolov5/fruit_training/best.onnx
```

目前第二条命令运行失败，后续寻找其他学习资料，看能不能解决
