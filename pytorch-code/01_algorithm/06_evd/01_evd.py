import torch

# 创建一个 3x3 的矩阵
A = torch.tensor([[4, 1, -2], [1, 6, 0], [-2, 0, 5]], dtype=torch.float32)

# 使用 PyTorch 的 linalg.eig() 函数进行特征值分解
eigenvalues, eigenvectors = torch.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:")
print(eigenvectors)