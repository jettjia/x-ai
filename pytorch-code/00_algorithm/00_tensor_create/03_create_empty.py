import torch

a = torch.Tensor([[1, 2],[3, 4]])
d = torch.empty(2,3)
print(d.type())
print(d)
print(d.type_as(a))