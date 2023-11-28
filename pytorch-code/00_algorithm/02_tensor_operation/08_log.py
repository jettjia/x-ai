import torch

a = torch.tensor([10, 2],
                 dtype=torch.float32)
print(torch.log(a))
print(torch.log_(a))
print(a.log())
print(a.log_())