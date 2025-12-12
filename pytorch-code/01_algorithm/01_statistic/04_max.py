import torch

# 创建一个张量
x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])

# 使用 torch.max() 找到张量中的最大值
max_value = torch.max(x)

print("输入张量：")
print(x)
print("最大值：", max_value)