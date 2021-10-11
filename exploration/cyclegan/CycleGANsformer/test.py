import torch
from cyclegansformer import CycleGANsformer

x = torch.rand(1, 256, 256, 3) # your input image
cgf = CycleGANsformer()

output_img = cgf(x) # can be viewed using matplotlib

print(output_img)