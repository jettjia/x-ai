import torch

a = torch.rand((10, 4))
print(a)
out = torch.split(a, 3, dim=0)
print(len(out))
for t in out:
    print(t.shape)