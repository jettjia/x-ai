import torch

a = torch.Tensor([[1, 2],[3, 4]])
d = torch.eye(2, 2)
print(d.type())
print(d.type_as(a))
