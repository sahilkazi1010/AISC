#P-XOR

def activation(sum):
    if sum >= 0:
        return 1
    else:
        return 0

x1 = int(input("Enter x1 (0 or 1): "))
x2 = int(input("Enter x2 (0 or 1): "))

# Hidden layer: OR
h1 = activation(x1 + x2 - 0.5)

# Hidden layer: NAND
h2 = activation(-x1 - x2 + 1.5)

# Output layer: AND
output = activation(h1 + h2 - 1.5)

print("Hidden Neuron H1 (OR) =", h1)
print("Hidden Neuron H2 (NAND) =", h2)
print("XOR Output =", output)
