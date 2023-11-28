import torch

a = torch.tensor([1, 2])
print(torch.pow(a, 3))
print(a.pow(3))
print(a**3)
print(a.pow_(3))
print(a)