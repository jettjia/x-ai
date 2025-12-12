import torch

torch.manual_seed(1)

mean = torch.rand(1, 2)
std  = torch.rand(1, 2)

print(torch.normal(mean, std)) # mean=std