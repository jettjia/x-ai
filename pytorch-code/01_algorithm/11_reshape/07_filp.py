import torch

a = torch.rand(1, 2, 3)

print(a)
print(torch.flip(a, dims=[2, 1]))