import torch

# 创建两个矩阵
A = torch.tensor([1, 2])
B = torch.tensor([5, 6])

# 执行矩阵乘法
C = torch.matmul(A, B)

print(C)