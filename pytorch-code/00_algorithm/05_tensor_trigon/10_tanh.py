import torch

# 创建一个张量
x = torch.tensor([0, 1, 2, 3, 4])
print("x = ")
print(x)

# 使用 torch.tanh() 计算双曲正切值
y = torch.tanh(x)
print("y = ")
print(y)