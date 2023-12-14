import torch

a = torch.rand(4, 4)
print(a)
out = torch.index_select(a, dim=0,
                   index=torch.tensor([0, 3, 2]))

print(out, out.shape)