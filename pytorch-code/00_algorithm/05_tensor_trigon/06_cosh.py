import torch

# 创建一个张量
x = torch.tensor([0, 1, 2, 3, 4])
print("x = ")
print(x)

# 使用 torch.cosh() 计算双曲余弦值
y = torch.cosh(x)
print("y = ")
print(y)