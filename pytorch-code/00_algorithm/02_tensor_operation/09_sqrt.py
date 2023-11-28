import torch

a = torch.tensor([10, 2],
                 dtype=torch.float32)
print(torch.sqrt(a))
print(torch.sqrt_(a))

print(a.sqrt())
print(a.sqrt_())