import torch

# 创建一个 3x3 的张量
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 创建一个索引张量
indices = torch.tensor([[0, 2], [1, 0], [2, 1]])

# 使用 torch.gather 根据索引从 x 中提取数据
y = torch.gather(x, dim=1, index=indices)

# 打印结果
print(y)