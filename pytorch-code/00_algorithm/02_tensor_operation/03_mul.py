import torch

a = torch.rand(2, 3)
b = torch.rand(2, 3)

print(a * b)
print(torch.mul(a, b))
print(a.mul(b))
print(a)
print(a.mul_(b))
print(a)