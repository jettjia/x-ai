import torch

a = torch.rand(2, 3)
b = torch.rand(2, 3)

print(a)
print(b)

print(a + b)
print(a.add(b))
print(torch.add(a, b))
print(a)
print(a.add_(b)) # 会改变a的值
print(a)