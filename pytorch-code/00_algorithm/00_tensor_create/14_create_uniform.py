import torch

a = torch.Tensor([[1, 2],[3, 4]])
d = torch.Tensor(2, 2).uniform_(-1, 1)
print(d.type())
print(d.type_as(a))

