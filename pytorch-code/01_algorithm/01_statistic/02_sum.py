import torch

# 创建一个张量
x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])

# 使用 torch.sum() 计算元素之和
sum_value = torch.sum(x)

print("input:")
print(x)
print("out-sum:")
print(sum_value)