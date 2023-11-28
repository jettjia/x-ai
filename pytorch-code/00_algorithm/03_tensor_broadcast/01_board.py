import torch

a = torch.rand(2, 2)
b = torch.rand(1, 2)
# a, 2*1
# b, 1*2
# c, 2*2
# 2*4*2*3
c = a + b
print(a)
print(b)
print(c)
print(c.shape)
