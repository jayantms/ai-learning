import torch

# Create tensors
x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
y = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)

# Basic math
print(x + y)          # elementwise addition
print(x @ y)          # matrix multiplication
print(x.mean())       # mean value
print(x.shape)        # tensor dimensions

#-------------------- 

device = "cuda" if torch.cuda.is_available() else "cpu"

x = torch.randn((3, 3), device=device)
y = torch.randn((3, 3), device=device)
z = x + y

print(z)
print("Running on:", device)

# ---------------------

x = torch.tensor([2.0, 3.0], requires_grad=True)

# Define function y = x^2 + 3x + 1
y = x ** 2 + 3 * x + 1

# Compute gradients dy/dx
y.sum().backward()

print(x.grad)  # ➜ tensor([7., 9.])