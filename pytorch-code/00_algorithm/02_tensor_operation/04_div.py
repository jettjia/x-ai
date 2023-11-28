import torch

a = torch.rand(2, 3)
b = torch.rand(2, 3)

print(a/b)
print(torch.div(a, b))
print(a.div(b))
print(a.div_(b))
print(a)