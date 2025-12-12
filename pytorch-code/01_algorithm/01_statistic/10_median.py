import torch

# 创建一个张量
x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])

# 使用 torch.median() 计算中位数
median_value = torch.median(x)

print("输入张量：")
print(x)
print("中位数：", median_value)