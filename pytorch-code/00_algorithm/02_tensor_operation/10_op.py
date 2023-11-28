import torch

a = torch.rand(2, 2)
a = a * 10
print(a)

print(torch.floor(a))
print(torch.ceil(a))
print(torch.round(a))
print(torch.trunc(a))
print(torch.frac(a))
print(a % 2)
b = torch.tensor([[2, 3], [4, 5]],
                 dtype=torch.float)
print(torch.fmod(a, b))
print(torch.remainder(a, b))
