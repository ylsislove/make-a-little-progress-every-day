---
title: PyTorch学习笔记（7）ResNet实战
date: 2023-07-19 21:52:53
categories:
 - [人工智能, 机器学习修炼之PyTorch]
tags: 
 - PyTorch
---

## Lenet5 网络模型

```python
import  torch
from    torch import nn
from    torch.nn import functional as F

class Lenet5(nn.Module):
    """
    for cifar10 dataset.
    """
    def __init__(self):
        super(Lenet5, self).__init__()

        self.conv_unit = nn.Sequential(
            # x: [b, 3, 32, 32] => [b, 16, ]
            nn.Conv2d(3, 16, kernel_size=5, stride=1, padding=0),
            nn.MaxPool2d(kernel_size=2, stride=2, padding=0),
            #
            nn.Conv2d(16, 32, kernel_size=5, stride=1, padding=0),
            nn.MaxPool2d(kernel_size=2, stride=2, padding=0),
            #
        )
        # flatten
        # fc unit
        self.fc_unit = nn.Sequential(
            nn.Linear(32*5*5, 32),
            nn.ReLU(),
            # nn.Linear(120, 84),
            # nn.ReLU(),
            nn.Linear(32, 10)
        )

        # [b, 3, 32, 32]
        tmp = torch.randn(2, 3, 32, 32)
        out = self.conv_unit(tmp)
        # [b, 16, 5, 5]
        print('conv out:', out.shape)

        # # use Cross Entropy Loss
        # self.criteon = nn.CrossEntropyLoss()

    def forward(self, x):
        """

        :param x: [b, 3, 32, 32]
        :return:
        """
        batchsz = x.size(0)
        # [b, 3, 32, 32] => [b, 16, 5, 5]
        x = self.conv_unit(x)
        # [b, 16, 5, 5] => [b, 16*5*5]
        x = x.view(batchsz, 32*5*5)
        # [b, 16*5*5] => [b, 10]
        logits = self.fc_unit(x)

        # # [b, 10]
        # pred = F.softmax(logits, dim=1)
        # loss = self.criteon(logits, y)

        return logits

def main():

    net = Lenet5()

    tmp = torch.randn(2, 3, 32, 32)
    out = net(tmp)
    print('lenet out:', out.shape)

if __name__ == '__main__':
    main()
```

## ResNet 网络模型

```python
import  torch
from    torch import  nn
from    torch.nn import functional as F


class ResBlk(nn.Module):
    """
    resnet block
    """
    def __init__(self, ch_in, ch_out, stride=1):
        """

        :param ch_in:
        :param ch_out:
        """
        super(ResBlk, self).__init__()

        # we add stride support for resbok, which is distinct from tutorials.
        self.conv1 = nn.Conv2d(ch_in, ch_out, kernel_size=3, stride=stride, padding=1)
        self.bn1 = nn.BatchNorm2d(ch_out)
        self.conv2 = nn.Conv2d(ch_out, ch_out, kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(ch_out)

        self.extra = nn.Sequential()
        if ch_out != ch_in:
            # [b, ch_in, h, w] => [b, ch_out, h, w]
            self.extra = nn.Sequential(
                nn.Conv2d(ch_in, ch_out, kernel_size=1, stride=stride),
                nn.BatchNorm2d(ch_out)
            )

    def forward(self, x):
        """

        :param x: [b, ch, h, w]
        :return:
        """
        out = F.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        # short cut.
        # extra module: [b, ch_in, h, w] => [b, ch_out, h, w]
        # element-wise add:
        out = self.extra(x) + out
        out = F.relu(out)
    
        return out

class ResNet18(nn.Module):

    def __init__(self):
        super(ResNet18, self).__init__()

        self.conv1 = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, stride=3, padding=0),
            nn.BatchNorm2d(64)
        )
        # followed 4 blocks
        # [b, 64, h, w] => [b, 128, h ,w]
        self.blk1 = ResBlk(64, 128, stride=2)
        # [b, 128, h, w] => [b, 256, h, w]
        self.blk2 = ResBlk(128, 256, stride=2)
        # # [b, 256, h, w] => [b, 512, h, w]
        self.blk3 = ResBlk(256, 512, stride=2)
        # # [b, 512, h, w] => [b, 1024, h, w]
        self.blk4 = ResBlk(512, 512, stride=2)

        self.outlayer = nn.Linear(512*1*1, 10)

    def forward(self, x):
        """

        :param x:
        :return:
        """
        x = F.relu(self.conv1(x))

        # [b, 64, h, w] => [b, 1024, h, w]
        x = self.blk1(x)
        x = self.blk2(x)
        x = self.blk3(x)
        x = self.blk4(x)


        # print('after conv:', x.shape) #[b, 512, 2, 2]
        # [b, 512, h, w] => [b, 512, 1, 1]
        x = F.adaptive_avg_pool2d(x, [1, 1])
        # print('after pool:', x.shape)
        x = x.view(x.size(0), -1)
        x = self.outlayer(x)

        return x

def main():

    blk = ResBlk(64, 128, stride=4)
    tmp = torch.randn(2, 64, 32, 32)
    out = blk(tmp)
    print('block:', out.shape)

    x = torch.randn(2, 3, 32, 32)
    model = ResNet18()
    out = model(x)
    print('resnet:', out.shape)

if __name__ == '__main__':
    main()
```

## 模型训练

```python
import  torch
from    torch.utils.data import DataLoader
from    torchvision import datasets
from    torchvision import transforms
from    torch import nn, optim

from    lenet5 import Lenet5
from    resnet import ResNet18

def main():
    batchsz = 128

    cifar_train = datasets.CIFAR10('cifar', True, transform=transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ]), download=True)
    cifar_train = DataLoader(cifar_train, batch_size=batchsz, shuffle=True)

    cifar_test = datasets.CIFAR10('cifar', False, transform=transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ]), download=True)
    cifar_test = DataLoader(cifar_test, batch_size=batchsz, shuffle=True)


    x, label = iter(cifar_train).next()
    print('x:', x.shape, 'label:', label.shape)

    device = torch.device('cuda')
    # model = Lenet5().to(device)
    model = ResNet18().to(device)

    criteon = nn.CrossEntropyLoss().to(device)
    optimizer = optim.Adam(model.parameters(), lr=1e-3)
    print(model)

    for epoch in range(1000):

        model.train()
        for batchidx, (x, label) in enumerate(cifar_train):
            # [b, 3, 32, 32]
            # [b]
            x, label = x.to(device), label.to(device)


            logits = model(x)
            # logits: [b, 10]
            # label:  [b]
            # loss: tensor scalar
            loss = criteon(logits, label)

            # backprop
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        print(epoch, 'loss:', loss.item())

        model.eval()
        with torch.no_grad():
            # test
            total_correct = 0
            total_num = 0
            for x, label in cifar_test:
                # [b, 3, 32, 32]
                # [b]
                x, label = x.to(device), label.to(device)

                # [b, 10]
                logits = model(x)
                # [b]
                pred = logits.argmax(dim=1)
                # [b] vs [b] => scalar tensor
                correct = torch.eq(pred, label).float().sum().item()
                total_correct += correct
                total_num += x.size(0)
                # print(correct)

            acc = total_correct / total_num
            print(epoch, 'test acc:', acc)

if __name__ == '__main__':
    main()

```
