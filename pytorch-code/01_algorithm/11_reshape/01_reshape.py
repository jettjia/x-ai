import torch

a = torch.rand(2, 3)

print(a)
out = torch.reshape(a, (3, 2))

print(out)