import torch

# 创建一个随机的 tensor
x = torch.randn(3, 3)
print("x = ")
print(x)

# 使用 torch.abs 计算绝对值
y = torch.abs(x)
print("y = ")
print(y)