import torch

# 创建一个张量
x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])

# 使用 torch.cumprod() 计算累积乘积
result = torch.cumprod(x)

print("Input Tensor: ")
print(x)
print("Result: ")
print(result)