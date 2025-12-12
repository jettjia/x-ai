import torch

# 创建一个张量
x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])

# 使用 torch.std() 计算标准差
std_value = torch.std(x)

print("输入张量：")
print(x)
print("标准差：", std_value)