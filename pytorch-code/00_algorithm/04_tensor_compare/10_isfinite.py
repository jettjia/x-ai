import torch

a = torch.rand(2, 3)
print(a)
print(a/0)
print(torch.isfinite(a))
print(torch.isfinite(a/0))