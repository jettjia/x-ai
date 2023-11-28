import torch

a = torch.rand(2, 3)
b = torch.rand(2, 3)

print(a)
print(b)

print(torch.eq(a, b))