import torch

a = torch.rand(1, 2, 3)
out = torch.unbind(a, dim=1)

print(out)