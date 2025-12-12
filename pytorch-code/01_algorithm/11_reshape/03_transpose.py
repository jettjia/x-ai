import torch

a = torch.rand(1, 2, 3)
print(a)

out = torch.transpose(a, 0, 1)
print(out)
print(out.shape)