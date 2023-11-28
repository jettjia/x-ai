import torch

a = torch.rand(2, 3)
print(torch.isinf(a/0))