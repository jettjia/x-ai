import torch

# 创建一个张量
x = torch.tensor([1, 4, 9, 16, 25])
print("x = ")
print(x)

# 使用 torch.rsqrt() 计算倒数平方根
y = torch.rsqrt(x)
print("y = ")
print(y)