import torch

if torch.cuda.is_available():
    device = torch.device("cuda")
    x = torch.ones(5, device=device)
    y= torch.ones_like(x, device=device) # 直接创建一个在GPU上的张量
    x = x.to(device) # 等价于 .to("cuda")
    z = x + y
    print(z)
    print(z.to("cpu", torch.double)) # to()还可以同时更改数据类型
