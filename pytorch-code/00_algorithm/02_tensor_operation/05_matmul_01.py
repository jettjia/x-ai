import torch

a = torch.ones(2, 1)
b = torch.ones(1, 2)
print(a @ b)
print(a.matmul(b))
print(torch.matmul(a, b))
print(torch.mm(a, b))
print(a.mm(b))