import torch
import torch.fft

# 创建一个信号张量
x = torch.tensor([1, 2, 3, 4, 5, 6])

# 对信号张量进行傅里叶变换
y = torch.fft.fft(x)

# 打印傅里叶变换结果
print(y)