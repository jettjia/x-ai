import torch

# 创建一个 4x4 的随机矩阵
A = torch.randn(4, 4)

# 使用 PyTorch 的 svd 函数进行奇异值分解
U, S, V = torch.svd(A)

print("U:")
print(U)

print("S:")
print(S)

print("V:")
print(V)