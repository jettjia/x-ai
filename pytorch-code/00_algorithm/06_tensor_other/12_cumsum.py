import torch

# 创建一个张量
x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])

# 使用 torch.cumsum() 计算累积和
result = torch.cumsum(x, dim=0)

print("Input Tensor: ")
print(x)
print("Result: ")
print(result)