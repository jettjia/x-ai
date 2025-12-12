import torch

a = torch.linspace(1, 6, 6).view(2, 3)
b = torch.linspace(7, 12, 6).view(2, 3)
print(a, b)

out = torch.stack((a, b), dim=0)
print(out)
print(out.shape)