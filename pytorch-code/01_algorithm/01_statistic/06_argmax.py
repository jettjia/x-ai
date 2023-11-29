import torch

# 创建一个张量
x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])

# 使用 torch.argmax() 找到最大值的索引
max_index = torch.argmax(x)

print("输入张量：")
print(x)
print("最大值的索引：", max_index)