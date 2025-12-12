import torch

# 生成随机数据
x = torch.randn(100, 5)

# 计算均值并进行中心化
mean = torch.mean(x, dim=0)
x = x-mean

# 计算数据的协方差矩阵
cov = torch.mm(x.t(), x) / (x.size(0)-1)

# 使用svd分解，计算主成分
u,s,v = torch.svd(cov)

# 将数据投影到前两个主成分上
x_pca = torch.mm(x,u[:, :2])

print("Projected data shape:", x_pca.shape)
print("--------------")
print(x_pca)