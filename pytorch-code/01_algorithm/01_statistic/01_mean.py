import torch

# 创建一个张量
x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])

# 使用 torch.mean() 计算均值
mean_value = torch.mean(x)

print("input:")
print(x)
print("out:")
print(mean_value)