import torch

# 创建一个张量
x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])

# 使用 torch.min() 找到张量中的最小值
min_value = torch.min(x)

print("输入张量：")
print(x)
print("最小值：", min_value)