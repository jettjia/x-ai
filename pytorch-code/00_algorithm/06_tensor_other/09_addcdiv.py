import torch

# 创建三个张量
x = torch.tensor([1.0, 2.0, 3.0])
y = torch.tensor([4.0, 5.0, 6.0])
z = torch.tensor([2.0, 2.0, 2.0])

# 使用 torch.addcdiv() 执行元素级的加法和除法操作
result = torch.addcdiv(x, y, z)

print("x Tensor: ")
print(x)
print("y Tensor: ")
print(y)
print("z Tensor: ")
print(z)
print("Result: ")
print(result)