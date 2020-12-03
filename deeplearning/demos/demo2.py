import torch
from torch.nn import functional as F

x = torch.ones(1)
w = torch.full([1], 2)
mse = F.mse_loss(torch.ones(1), x*w)
print(mse)
w.requires_grad
torch.autograd.grad(mse, [w])
