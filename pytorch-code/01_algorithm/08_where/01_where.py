import torch

a = torch.rand(4, 4)
b = torch.rand(4, 4)

print(a)
print(b)

out = torch.where(a > 0.5, a, b)

print(out)