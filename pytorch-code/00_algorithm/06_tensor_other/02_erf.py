import torch

# 创建一个张量
x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
print("x = ")
print(x)

# 使用 torch.erf() 计算误差函数
y = torch.erf(x)
print("y = ")
print(y)