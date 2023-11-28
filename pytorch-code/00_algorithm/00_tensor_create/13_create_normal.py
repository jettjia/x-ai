import torch

a = torch.Tensor([[1, 2],[3, 4]])
d = torch.normal(mean=torch.rand(5), std=torch.rand(5))
print(d.type())
print(d.type_as(a))
