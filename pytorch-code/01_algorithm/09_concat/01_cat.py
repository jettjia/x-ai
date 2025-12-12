import torch

a = torch.zeros((2, 4))
b = torch.ones((2, 4))

out = torch.cat((a,b),dim=0)
print(out)

out = torch.cat((a,b),dim=1)
print(out)