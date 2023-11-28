import torch

a = torch.rand(2, 3)
b = torch.rand(2, 3)

print(a - b)
print(torch.sub(a, b))
print(a.sub(b))
print(a.sub_(b))
print(a)