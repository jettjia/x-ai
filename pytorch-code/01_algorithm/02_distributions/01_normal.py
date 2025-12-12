import torch
import torch.distributions as D

# 设置正态分布的均值和标准差
mean = 0.0
std = 1.0

# 创建正态分布对象
dist = D.Normal(mean, std)

# 生成正态分布的随机样本
sample = dist.sample((5,))
print("Sample:", sample)

# 计算正态分布的概率密度函数值
log_prob = dist.log_prob(sample)
prob = torch.exp(log_prob)
print("Log Probability:", log_prob)
print("Probability:", prob)