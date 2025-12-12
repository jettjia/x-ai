import torch

# 创建一个张量
x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])

# 使用 torch.var() 计算方差
var_value = torch.var(x)

print("输入张量：")
print(x)
print("方差：", var_value)