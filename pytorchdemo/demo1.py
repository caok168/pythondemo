import torch
import numpy as np

a = torch.randn(1, 2, 3, 4, 5)
res = torch.numel(a)
print(res)

a = torch.zeros(4,4)
print(torch.numel(a))

print(torch.eye(3))

a = np.array([1, 2, 3])
t = torch.from_numpy(a)
print(t)

t = torch.LongTensor([1, 2, 3])
t[0] = -1
print(a)

print(torch.linspace(3, 10, steps=5))

print(torch.linspace(-10, 10, steps=5))

print(torch.linspace(start=-10, end=10, steps=5))

print(torch.logspace(start=-10, end=10, steps=5))

print(torch.logspace(start=0.1, end=1.0, steps=5))

print(torch.ones(2, 3))
print(torch.ones(5))

print(torch.rand(4))
print(torch.rand(2, 3))

print(torch.randn(4))
print(torch.randn(2, 3))

print(torch.randperm(4))

print(torch.arange(1, 4))
print(torch.arange(1, 2.5, 0.5))

