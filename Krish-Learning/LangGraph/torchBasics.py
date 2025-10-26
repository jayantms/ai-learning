import torch

# Create tensors (GPU-enabled arrays)
x = torch.tensor([2.0, 3.0], requires_grad=True)
y = x ** 2 + 3 * x + 1

# Compute gradients (backpropagation)
y.sum().backward()
print(x.grad)  # prints gradients: tensor([7., 9.])