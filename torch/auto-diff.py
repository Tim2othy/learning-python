import torch

x = torch.ones(5)  # input tensor
y = torch.zeros(3)  # expected output
w = torch.randn(5, 3, requires_grad=True)
b = torch.randn(3, requires_grad=True)
z = torch.matmul(x, w) + b
loss = torch.nn.functional.binary_cross_entropy_with_logits(z, y)

print(z.grad_fn)
print(loss.grad_fn)


# We want del loss/ del w
# and

# del loss / del b

# then we can optimize the net

loss.backward()

print(w.grad)
print(b.grad)

z = torch.matmul(x, w) + b
print(z.requires_grad)

with torch.no_grad():
    z = torch.matmul(x, w) + b
print(z.requires_grad)


z = torch.matmul(x, w) + b
print(z.requires_grad)
z_det = z.detach()
print(z_det.requires_grad)
