import torch
import torch.nn as nn

class MySigmoid(nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, x):
        return 1 / (1 + torch.exp(-x))
    
my_sigmoid = MySigmoid()

x = torch.tensor([1, 5, -4, 3, -2])

output = my_sigmoid(x)
print(output)