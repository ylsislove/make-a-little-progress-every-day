# YOLOv5-模型训练与检测

  - [下载 OIDv4_ToolKit 数据集](#%E4%B8%8B%E8%BD%BD-oidv4_toolkit-%E6%95%B0%E6%8D%AE%E9%9B%86)
  - [下载 Apple 和 Orange 的数据集](#%E4%B8%8B%E8%BD%BD-apple-%E5%92%8C-orange-%E7%9A%84%E6%95%B0%E6%8D%AE%E9%9B%86)
  - [转换标签格式](#%E8%BD%AC%E6%8D%A2%E6%A0%87%E7%AD%BE%E6%A0%BC%E5%BC%8F)
  - [编写 dataset.yaml 文件](#%E7%BC%96%E5%86%99-datasetyaml-%E6%96%87%E4%BB%B6)
  - [编写 yolov5s.yaml 文件](#%E7%BC%96%E5%86%99-yolov5syaml-%E6%96%87%E4%BB%B6)
  - [开始训练](#%E5%BC%80%E5%A7%8B%E8%AE%AD%E7%BB%83)
  - [查看训练过程](#%E6%9F%A5%E7%9C%8B%E8%AE%AD%E7%BB%83%E8%BF%87%E7%A8%8B)
  - [进行检测](#%E8%BF%9B%E8%A1%8C%E6%A3%80%E6%B5%8B)
  - [模型转换](#%E6%A8%A1%E5%9E%8B%E8%BD%AC%E6%8D%A2)

## 下载 OIDv4_ToolKit 数据集
```bash
git clone https://github.com/EscVM/OIDv4_ToolKit.git
# 安装依赖
pip install -r .\requirements.txt
```

## 下载 Apple 和 Orange 的数据集
```bash
python .\main.py downloader --classes Apple Orange --type_csv all
```

## 转换标签格式
编写 python 脚本如下：
```python
from genericpath import isfile
import  os
import  cv2 as cv

root_dir = "E:\\code\\github\\OIDv4_ToolKit\\OID\Dataset"
valid_label_dir = "E:\\code\\python\\openvino_utils\\data\\labels\\valid"

def read_annotation(data_type = "train", class_type = "Apple"):
    current_dir = os.path.join(root_dir, data_type, class_type)
    print(current_dir)
    files = os.listdir(current_dir)
    for f in files:
        if (os.path.isfile(os.path.join(current_dir, f))):
            image = cv.imread(os.path.join(current_dir, f))
            label_file = os.path.join(current_dir, "label", f.replace(".jpg", ".txt"))
            yolo_label = f.replace(".jpg", ".txt")
            data_label_text_f = os.path.join(valid_label_dir, yolo_label)
            file_write_obj = open(data_label_text_f, 'w')

            with open(label_file) as f:
                boxes = [line.strip() for line in f.readlines()]

            class_index = -1
            for box in boxes:
                anno_info = box.split(" ")
                print("class name: ", anno_info[0])
                x1 = float(anno_info[1])
                y1 = float(anno_info[2])
                x2 = float(anno_info[3])
                y2 = float(anno_info[4])

                if anno_info[0] == "Apple":
                    class_index = 0
                else:
                    class_index = 1
                
                h, w, c = image.shape
                cx = (x1 + x2) / (2 * w)
                cy = (y1 + y2) / (2 * h)
                sw = (x2 - x1) / w
                sh = (y2 - y1) / h
                file_write_obj.write("%d %f %f %f %f\n" % (class_index, cx, cy, sw, sh))

            file_write_obj.close()

if __name__ == "__main__":
    read_annotation(data_type="validation", class_type="Orange")
```

转换完毕后，将标签和图片数据放在 yolov5 目录下的 fruit_training 下的 data 目录下，没有目录就创建

## 编写 dataset.yaml 文件
参考 `yolov5\data\VOC.yaml` 文件，在 `yolov5\fruit_training\` 目录下创建 `dataset.yaml` 文件，编写内容如下：
```yaml
train: fruit_training/data/images/train/
val: fruit_training/data/images/valid

nc: 2

names: ['Apple', 'Orange']
```

## 编写 yolov5s.yaml 文件
参考 `yolov5\models\yolov5s.yaml` 文件，拷贝到 `yolov5\fruit_training\` 目录下，修改 nc 为 2。文件内如下：
```yaml
# YOLOv5 🚀 by Ultralytics, GPL-3.0 license

# Parameters
nc: 2  # number of classes
depth_multiple: 0.33  # model depth multiple
width_multiple: 0.50  # layer channel multiple
anchors:
  - [10,13, 16,30, 33,23]  # P3/8
  - [30,61, 62,45, 59,119]  # P4/16
  - [116,90, 156,198, 373,326]  # P5/32

# YOLOv5 backbone
backbone:
  # [from, number, module, args]
  [[-1, 1, Focus, [64, 3]],  # 0-P1/2
   [-1, 1, Conv, [128, 3, 2]],  # 1-P2/4
   [-1, 3, C3, [128]],
   [-1, 1, Conv, [256, 3, 2]],  # 3-P3/8
   [-1, 9, C3, [256]],
   [-1, 1, Conv, [512, 3, 2]],  # 5-P4/16
   [-1, 9, C3, [512]],
   [-1, 1, Conv, [1024, 3, 2]],  # 7-P5/32
   [-1, 1, SPP, [1024, [5, 9, 13]]],
   [-1, 3, C3, [1024, False]],  # 9
  ]

# YOLOv5 head
head:
  [[-1, 1, Conv, [512, 1, 1]],
   [-1, 1, nn.Upsample, [None, 2, 'nearest']],
   [[-1, 6], 1, Concat, [1]],  # cat backbone P4
   [-1, 3, C3, [512, False]],  # 13

   [-1, 1, Conv, [256, 1, 1]],
   [-1, 1, nn.Upsample, [None, 2, 'nearest']],
   [[-1, 4], 1, Concat, [1]],  # cat backbone P3
   [-1, 3, C3, [256, False]],  # 17 (P3/8-small)

   [-1, 1, Conv, [256, 3, 2]],
   [[-1, 14], 1, Concat, [1]],  # cat head P4
   [-1, 3, C3, [512, False]],  # 20 (P4/16-medium)

   [-1, 1, Conv, [512, 3, 2]],
   [[-1, 10], 1, Concat, [1]],  # cat head P5
   [-1, 3, C3, [1024, False]],  # 23 (P5/32-large)

   [[17, 20, 23], 1, Detect, [nc, anchors]],  # Detect(P3, P4, P5)
  ]
```

## 开始训练
运行命令：`python .\train.py --data fruit_training/dataset.yaml --cfg fruit_training/yolov5s.yaml --weights yolov5s.pt --batch-size 1 --epochs 2`

## 查看训练过程
运行命令：`tensorboard --logdir=E:\code\python\yolov5\runs\train\exp`

## 进行检测
下载几个苹果和橘子的图片放到 fruit_training 目录下，运行检测命令：
```bash
python .\detect.py --source .\fruit_training\apple.jpeg --weights .\fruit_training\best.pt --conf 0.25
```

哦对，还要把训练好的 `best.pt` 模型也放到 fruit_training 目录下

## 模型转换
看 `requirements.txt` 文件里是否有安装 `coremltools` 和 `onnx` 这两个第三方库，没有的话就安装：
```bash
pip install coremltools>=4.1 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install onnx>=1.9.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

安装完成后，运行下面命令进行模型转换：
```bash
python .\export.py --weights .\fruit_training\best.pt --img 640 --batch 1
```
