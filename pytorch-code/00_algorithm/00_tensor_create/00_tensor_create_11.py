import torch

a = torch.Tensor([[1, 2],[3, 4]])
d = torch.linspace(10, 2, 3)
print(d.type())
print(d.type_as(a))
