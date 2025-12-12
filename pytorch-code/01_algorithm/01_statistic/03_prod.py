import torch

# 创建一个张量
x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])

# 使用 torch.prod() 计算所有元素的乘积
product_value = torch.prod(x)

print("输入张量：")
print(x)
print("所有元素的乘积：")
print(product_value)