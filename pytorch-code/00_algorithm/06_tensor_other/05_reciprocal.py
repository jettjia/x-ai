import torch

# 创建一个张量
x = torch.tensor([1, 2, 3, 4, 5])
print("x = ")
print(x)

# 使用 torch.reciprocal() 计算倒数
y = torch.reciprocal(x)
print("y = ")
print(y)