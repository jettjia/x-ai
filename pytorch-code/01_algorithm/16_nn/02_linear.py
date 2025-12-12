import torch
import torch.nn as nn

# 定义输入数据
x = torch.randn(3, 5)

# 定义线性层
linear = nn.Linear(5, 3)

# 前向传播
y = linear(x)

print("输入数据：")
print(x)

print("输出数据：")
print(y)