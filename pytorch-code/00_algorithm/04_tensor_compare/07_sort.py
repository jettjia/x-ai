import torch

a = torch.tensor([[1, 4, 4, 3, 5],
                  [2, 3, 1, 3, 5]])
print(a.shape)
print(torch.sort(a, dim=1,
                 descending=False))