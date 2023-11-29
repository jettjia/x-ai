import torch

# 创建一个张量
x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
print("x = ")
print(x)

# 使用 torch.acos() 计算反余弦值
y = torch.acos(x)
print("y = ")
print(y)