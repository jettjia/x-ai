import torch

# 创建两个张量
x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
y = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
print("x = ")
print(x)
print("y = ")
print(y)

# 使用 torch.atan2() 计算反正切值
z = torch.atan2(y, x)
print("z = ")
print(z)