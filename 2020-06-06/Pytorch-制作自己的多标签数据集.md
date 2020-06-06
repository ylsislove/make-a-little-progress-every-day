# Pytorch-制作自己的多标签数据集

  - [需求](#%E9%9C%80%E6%B1%82)
  - [代码](#%E4%BB%A3%E7%A0%81)
  - [输出结果](#%E8%BE%93%E5%87%BA%E7%BB%93%E6%9E%9C)

## 需求
![Train.txt](https://cdn.jsdelivr.net/gh/ylsislove/image-home/test/20200606170421.png)

如图所示，想通过Pytorch加载自己的数据集，每一张图片后面有三个标签。该如何实现呢？看下面

## 代码
```python
from    PIL import Image
import  torch
from    torchvision import transforms
import  numpy as np
from    matplotlib import pyplot as plt

# 创建自己的类：MyDataset,这个类是继承的torch.utils.data.Dataset
class MyDataset(torch.utils.data.Dataset): 
    def __init__(self, filepath, transform=None, target_transform=None):
        super(MyDataset, self).__init__()

        # 按照传入的路径打开这个文本，并读取内容
        fh = open(filepath, 'r') 
        imgs = []
        for line in fh:                # 按行循环txt文本中的内容
            line = line.rstrip()       # 删除 本行string 字符串末尾的指定字符，这个方法的详细介绍自己查询python
            words = line.split()       # 通过指定分隔符对字符串进行切片，默认为所有的空字符，包括空格、换行、制表符等
            # 三分类问题，所以label有三个
            imgs.append((words[0], [float(words[1]), float(words[2]), float(words[3])]))
            # imgs.append((words[0], float(words[1])))

        self.imgs = imgs
        self.transform = transform
        self.target_transform = target_transform

    # 这个方法是必须要有的，用于按照索引读取每个元素的具体内容
    def __getitem__(self, index):
        # 读取文件路径和标签
        fn, label = self.imgs[index]
        # 读取图片信息
        img = Image.open(fn).convert('RGB')
        # list转numpy
        label = np.array(label)

        # 是否进行transform
        if self.transform is not None:
            img = self.transform(img)

        # return很关键，return回哪些内容，那么我们在训练时循环读取每个batch时，就能获得哪些内容
        return img, torch.from_numpy(label)

    # 这个函数也必须要写，它返回的是数据集的长度，也就是多少张图片，要和loader的长度作区分
    def __len__(self): 
        return len(self.imgs)


def main():
    
    train_data = MyDataset(filepath='./data/Train.txt', transform=transforms.ToTensor())
    train_loader = torch.utils.data.DataLoader(train_data, batch_size=2, shuffle=True)

    x, label = iter(train_loader).next()
    print('x:', x.shape, 'label:', label.shape)

    # 显示一张图片
    img = x[0]
    img = img.numpy()
    img = np.transpose(img, (1, 2, 0))
    plt.imshow(img)
    plt.show()



if __name__ == "__main__":
    main()
```

## 输出结果
因为我 batch_size 设为 2，所以一个 iterator 随机取出两张图片，所以输出结果的第一个维度是 batch_size，大小为 2
```python
# [batch_size, channel, h, w]   [batch_size, label]
x: torch.Size([2, 3, 320, 480]) label: torch.Size([2, 3])
```