import torch

a = torch.linspace(1, 16, 16).view(4, 4)

b = torch.take(a, index=torch.tensor([0, 15, 13, 10]))

print(b)