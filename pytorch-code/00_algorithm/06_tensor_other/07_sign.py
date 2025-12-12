import torch

# 创建一个张量
x = torch.tensor([1, -2, 3, -4, 5])
print("x = ")
print(x)

# 使用 torch.sign() 计算符号
y = torch.sign(x)
print("y = ")
print(y)