import torch

# 创建一个张量
x = torch.tensor([1, 2, 3, 4, 5])

# 获取张量的属性
print(x.shape)  # 输出：torch.Size([5])
print(x.dtype)  # 输出：torch.int32
print(x.device)  # 输出：cpu
print(x.is_sparse)  # 输出：False

# 修改张量的属性
x = x.to(device='cuda')  # 将张量移动到GPU上
print(x.device)  # 输出：cuda:0

x = x.float()  # 将张量的数据类型转换为float32
print(x.dtype)  # 输出：torch.float32