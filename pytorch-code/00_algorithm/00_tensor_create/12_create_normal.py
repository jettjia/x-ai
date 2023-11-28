import torch

b = torch.Tensor(2, 2)
dd = torch.normal(mean=0, std=1, size=(2, 3), out=b)
print(b)
print(dd)
