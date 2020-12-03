import torch
from torch.nn import functional as F

a = torch.linspace(-100, 100, 10)
print(a)

b = torch.sigmoid(a)
print(b)

c = torch.tanh(a)
print(c)

a = torch.linspace(-1, 1, 10)
print(a)
b = torch.tanh(a)
print(b)

print("===================================")
a = torch.linspace(-1, 1, 10)
print(a)
b = torch.relu(a)
print(b)
b = F.relu(a)
print(b)



