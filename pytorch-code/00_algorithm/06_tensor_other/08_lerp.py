import torch

# 创建两个张量
start = torch.tensor([1.0, 2.0, 3.0])
end = torch.tensor([4.0, 5.0, 6.0])

# 使用 torch.lerp() 进行线性插值
lerp_amount = 0.5  # 插值比例，范围为0到1
result = torch.lerp(start, end, lerp_amount)

print("Start Tensor: ")
print(start)
print("End Tensor: ")
print(end)
print("Lerp Amount: ")
print(lerp_amount)
print("Result: ")
print(result)