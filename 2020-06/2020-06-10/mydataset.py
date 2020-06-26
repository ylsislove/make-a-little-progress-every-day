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
        return img, torch.from_numpy(label).float(), fn

    # 这个函数也必须要写，它返回的是数据集的长度，也就是多少张图片，要和loader的长度作区分
    def __len__(self): 
        return len(self.imgs)


def main():
    
    train_data = MyDataset(filepath='./data/Train.txt', transform=transforms.ToTensor())
    # test_data = MyDataset(filepath='./data/Test.txt', transform=transforms.ToTensor())

    # print(train_data[0])

    train_loader = torch.utils.data.DataLoader(train_data, batch_size=2, shuffle=True)
    # test_loader = torch.utils.data.DataLoader(test_data, batch_size=32, shuffle=True)

    x, label = iter(train_loader).next()
    print('x:', x.shape, 'label:', label.shape)

    for i in label:
        arr = list(i)
        print([arr[0].item(), arr[1].item(), arr[2].item()])

    # img = x[0]
    # img = img.numpy()
    # img = np.transpose(img, (1, 2, 0))
    # plt.imshow(img)
    # plt.show()


if __name__ == "__main__":
    main()

