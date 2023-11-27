import torch

a = torch.Tensor([[1, 2],[3, 4]])
d = torch.zeros(2,3)
d = torch.zeros_like(d)
print(d.type())
print(d.type_as(a))
