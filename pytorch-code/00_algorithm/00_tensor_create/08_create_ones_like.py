import torch

a = torch.Tensor([[1, 2],[3, 4]])
d = torch.ones(2, 2)
d = torch.ones_like(d)
print(d.type())
print(d.type_as(a))
