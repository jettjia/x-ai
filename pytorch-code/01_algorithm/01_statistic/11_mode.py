import torch

# 创建一个张量
x = torch.tensor([1, 2, 2, 3, 3, 3])

# 使用 torch.mode() 找到众数元素的索引
mode_indices = torch.mode(x)

print("输入张量：")
print(x)
print("众数元素的索引：", mode_indices)