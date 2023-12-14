import torch

a = torch.linspace(1, 16, 16).view(4, 4)
mask = torch.gt(a, 8)
print(a)
print(mask)
out = torch.masked_select(a, mask)
print(out) # 将a中大于8的值打印出来