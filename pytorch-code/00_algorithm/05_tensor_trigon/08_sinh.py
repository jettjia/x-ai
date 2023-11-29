import torch

# 创建一个张量
x = torch.tensor([0, 1, 2, 3, 4])
print("x = ")
print(x)

# 使用 torch.sinh() 计算双曲正弦值
y = torch.sinh(x)
print("y = ")
print(y)