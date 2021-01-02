import  torch
from    torch.utils.data import DataLoader
from    torchvision import datasets
from    torchvision import transforms
from    torch import nn, optim
import  torchvision.models as models

from    matplotlib import pyplot as plt
import  numpy as np

import  mydataset
import  myutils
import  time

def load_model(model_path):
    
    # 初始化模型
    model = models.resnet50()

    # 更改最后一层全连接层
    # 首先获取输入参数
    fc_inputs = model.fc.in_features

    # 添加全连接层，RelU激活函数，Dropout
    model.fc = nn.Sequential(
        nn.Linear(fc_inputs, 256),
        nn.ReLU(),
        nn.BatchNorm1d(256),
        # 注意 pytorch 的 dropout 的参数和 tf 的参数刚好相反
        nn.Dropout(0.3),
        nn.Linear(256, 3),
        nn.Sigmoid()
    )
    
    # 开启GPU加速
    device = torch.device('cuda')
    model.to(device)
    
    # 定义优化器
    optimizer = optim.Adam(model.parameters(), lr=1e-4)
    
    epoch = 0
    record = []
    best_epoch = 0
    best_mae = 100.0
    
    # 预训练模型存在
    if myutils.fileExists(model_path):
        # 加载预训练模型参数
        checkpoint = torch.load(model_path)
        model.load_state_dict(checkpoint['model_state_dict'])
        optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        epoch = checkpoint['epoch']
        record = checkpoint['record']
        best_epoch = checkpoint['best_epoch']
        best_mae = checkpoint['best_mae']
        
    model.to(device)
    
    # 定义损失函数
    loss_func = nn.SmoothL1Loss().to(device)
    mae_func = nn.L1Loss().to(device)
    
    return model, optimizer, loss_func, mae_func, record, {
        'device': device,
        'epoch': epoch,
        'best_epoch': best_epoch,
        'best_mae': best_mae,
    }


def read_data(batchsz=32):

    # 加载训练数据
    test_data = mydataset.MyDataset('./data/test.txt', transform=transforms.Compose([
        # 转换成张量
        transforms.ToTensor(),
        # 数据增强，像素归一化，均值 / 方差
        transforms.Normalize([0.485, 0.456, 0.406],
                             [0.229, 0.224, 0.225])
    ]))
    test_loader = DataLoader(test_data, batch_size=batchsz, shuffle=False)

    
    x, label, fn = iter(test_loader).next()
    print('x:', x.shape, 'label:', label.shape, 'fn:', len(fn))
    print("数据加载完毕...")

    return test_data, test_loader


def predict(model, loss_func, mae_func, device, batchsz=32):
    
    # 加载数据
    test_data, test_loader = read_data(batchsz=batchsz)
    
    test_loss = 0.0
    test_mae = 0.0
    
    result = []
    
    # 切换成验证模式
    model.eval()
    with torch.no_grad():
        # test
        for batchidx, (x, label, fn) in enumerate(test_loader):

            # 获取batch数据
            x, label = x.to(device), label.to(device)

            # 送入模型得到结果 [batch, 3]
            logits = model(x)

            # 记录预测数据
            for index, values in enumerate(logits):
                arr = list(values)
                result.append([fn[index], arr[0].item(), arr[1].item(), arr[2].item()])

            # 计算loss
            loss = loss_func(logits, label)
            batch_mae = mae_func(logits, label)

            # 累加 loss
            test_loss += loss.item() * x.size(0)
            # 累加 mae
            test_mae += batch_mae.item() * x.size(0)

            # 进度条更新进度
            myutils.progressBar(batchsz * (batchidx + 1), len(test_data), 'val_loss: {} val_mae: {}'.format(loss.item(), batch_mae.item()))

    avg_test_loss = test_loss / len(test_data)
    avg_test_mae = test_mae / len(test_data)

    print("test_loss: {:.4f} test_mae: {:.4f}".format(avg_test_loss, avg_test_mae))

    return result

def compare(csv_file_path, txt_file_path):
    result_data = []
    csv_data = myutils.read_csv(csv_file_path)
    txt_data = myutils.read_txt(txt_file_path)
    for i in range(0, len(csv_data), 4):
        if (csv_data[i][0] != txt_data[i][0]):
            print('csv_data img_name is not equal to txt_data img_name')
            return []
        # 得到经纬度信息
        img_name = csv_data[i][0].strip().split('/')[-1]
        lon_lat = img_name.split('_')
        lon, lat = lon_lat[0], lon_lat[1]
        # csv_data 合并不同角度的预测值
        wl_predict = (float(csv_data[i][1]) + float(csv_data[i+1][1]) + float(csv_data[i+2][1]) + float(csv_data[i+3][1])) / 4
        ol_predict = (float(csv_data[i][2]) + float(csv_data[i+1][2]) + float(csv_data[i+2][2]) + float(csv_data[i+3][2])) / 4
        ow_predict = (float(csv_data[i][3]) + float(csv_data[i+1][3]) + float(csv_data[i+2][3]) + float(csv_data[i+3][3])) / 4
        # 真实值
        wl_real = float(txt_data[i][1])
        ol_real = float(txt_data[i][2])
        ow_real = float(txt_data[i][3])
        # 偏差
        wl_error = abs(wl_real - wl_predict)
        ol_error = abs(ol_real - ol_predict)
        ow_error = abs(ow_real - ow_predict)
        # 记录
        result_data.append([lon, lat, wl_real, wl_predict, wl_error, ol_real, ol_predict, ol_error, ow_real, ow_predict, ow_error])
    return result_data


if __name__ == '__main__':
    
    batchsz = 32
    model_path = 'models/model_WL_OL_OW_20.pth'
    
    # 加载模型
    model, optimizer, loss_func, mae_func, record, model_dict = load_model(model_path)
    print(model_dict)
    
    # 绘制曲线图
    myutils.show_loss_and_mae(record)
    
    # 开始预测
    result = predict(model, loss_func, mae_func, model_dict['device'], batchsz)
    
    # 写入预测数据
    file_path = 'predict/predict.csv'
    myutils.write_csv(file_path, result)

    # 对比分析
    txt_path = 'data/test.txt'
    result_data = compare(file_path, txt_path)
    head = ['lon', 'lat', 'wl_real', 'wl_predict', 'wl_error', 'ol_real', 'ol_predict', 'ol_error', 'ow_real', 'ow_predict', 'ow_error']
    myutils.write_csv('predict/compare.csv', result_data, head)
    
    