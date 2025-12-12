import torch

# 创建三个张量
x = torch.tensor([1.0, 2.0, 3.0])
y = torch.tensor([4.0, 5.0, 6.0])
z = torch.tensor([2.0, 2.0, 2.0])

# 使用 torch.addcmul() 执行元素级的加法、乘法和减法操作
result = torch.addcmul(x, y, z)

print("x Tensor: ")
print(x)
print("y Tensor: ")
print(y)
print("z Tensor: ")
print(z)
print("Result: ")
print(result)