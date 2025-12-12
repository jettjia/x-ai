import torch

# 创建一个张量
x = torch.tensor([1, 2, 2, 3, 3, 3])

# 使用 torch.bincount() 计算每个值出现的次数
counts = torch.bincount(x)

print("输入张量：")
print(x)
print("每个值出现的次数：", counts)