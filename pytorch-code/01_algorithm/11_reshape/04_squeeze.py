import torch

a = torch.rand(1, 2, 3)
out = torch.squeeze(a)
print(out)
print(out.shape)