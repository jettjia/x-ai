import torch
import numpy as np

a = np.zeros([2, 2])
out = torch.from_numpy(a)
print(out)