import torch

a = torch.tensor([1, 2],
                 dtype=torch.float32)
print(a.type())
print(torch.exp(a))
print(torch.exp_(a))
print(a.exp())
print(a.exp_())