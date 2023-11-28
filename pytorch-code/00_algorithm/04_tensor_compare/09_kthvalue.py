import torch

a = torch.tensor([[2, 4, 3, 1, 5],
                  [2, 3, 5, 1, 4]])
print(torch.kthvalue(a, k=1, dim=1))
# print(torch.kthvalue(a, k=2, dim=1))