import torch

# 创建一个张量
x = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=torch.long)

# 将张量转换为浮点型
x = x.float()

# 使用 torch.histc() 计算离散直方图
hist_value = torch.histc(x, bins=4)

print("输入张量：")
print(x)
print("离散直方图：")
print(hist_value)