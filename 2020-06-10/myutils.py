import  os
import  time
import  shutil
import  sys
import  math
from    matplotlib import pyplot as plt
import  numpy as np
import  csv

# 获取格式化时间
def getTime(fat='%m%d%H%M'):
    return time.strftime(fat, time.localtime(time.time()))

# 实时进度条显示
def progressBar(cur, total, msg=''):
    str1 = '####################'
    str2 = '--------------------'
    if cur >= total:
        sys.stdout.write('\r{} {}/{} {}'.format(str1, total, total, msg))
        sys.stdout.write('\r\n')
    else:
        cur_len = math.floor((cur * len(str1)) / total)
        sys.stdout.write('\r{}{} {}/{} {}'.format(str1[:cur_len], str2[cur_len:], cur, total, msg))
    sys.stdout.flush()

# 绘制Loss和Mae的折线图
def show_loss_and_mae(_record):
    record = np.array(_record)
    plt.plot(record[:, 0:2])
    plt.legend(['Train Loss', 'Valid Loss'])
    plt.xlabel('Epoch Number')
    plt.ylabel('Loss')
#     plt.ylim(0, 0.3)
    plt.savefig('loss.png')
    plt.show()
    
    plt.plot(record[:, 2:4])
    plt.legend(['Train MAE', 'Valid MAE'])
    plt.xlabel('Epoch Number')
    plt.ylabel('MAE')
#     plt.ylim(0, 0.5)
    plt.savefig('mae.png')
    plt.show()

# 判断文件是否存在，存在返回True，否则返回False
def fileExists(_path):
    return os.path.exists(_path)


# 写 csv
def write_csv(filepath, data, head=None):
    if head:
        data = [head] + data
    with open(filepath, mode='w') as f:
        writer = csv.writer(f)
        for i in data:
            writer.writerow(i)


            
# 读 csv
def read_csv(filepath):
    data = []
    if os.path.exists(filepath):
        with open(filepath, mode='r') as f:
            lines = csv.reader(f)
            for line in lines:
                data.append(line)
        return data
    else:
        print('filepath is wrong')
        return []


def read_txt(filepath):
    data = []
    if os.path.exists(filepath):
        with open(filepath, mode='r') as f:
            while True:
                line = f.readline().strip()
                if not line:
                    break
                data.append(line.split())
        return data
    else:
        print('filepath is wrong')
        return []

    

if __name__ == "__main__":
#     print(getTime())
    # for i in range(1, 12):
    #     progressBar(i, 10)
    #     time.sleep(0.5)
    pass