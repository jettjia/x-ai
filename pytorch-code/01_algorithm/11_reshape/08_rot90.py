import torch

a = torch.rand(1, 2, 3)

print(a)
out = torch.rot90(a) # 旋转90度，默认是逆时针旋转
print(out)
print(out.shape)