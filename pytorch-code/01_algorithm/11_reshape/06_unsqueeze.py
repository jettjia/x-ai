import torch

a = torch.rand(1, 2, 3)

out = torch.unsqueeze(a, -1) # -1就是在最后一个维度上进行扩展
print(out.shape)