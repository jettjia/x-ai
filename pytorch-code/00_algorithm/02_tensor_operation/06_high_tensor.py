import torch

a = torch.ones(1, 2, 3, 4)
b = torch.ones(1, 2, 4, 3)
print(a.matmul(b).shape)