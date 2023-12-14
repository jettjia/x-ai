import torch

# 创建一个 3x3 的对称矩阵
A = torch.tensor([[4, 1, -2], [1, 6, 0], [-2, 0, 5]], dtype=torch.float32)

# 使用 PyTorch 的 eig 函数进行特征值分解
eigenvalues, eigenvectors = torch.linalg.eig(A, eigenvectors=True)

print("eigenvalues:",eigenvalues)