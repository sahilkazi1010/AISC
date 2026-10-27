#P-AND

def activation(sum):
    if sum >= 0:
        return 1
    else:
        return 0

x1 = int(input("Enter x1 (0 or 1): "))
x2 = int(input("Enter x2 (0 or 1): "))

w1 = 1.0
w2 = 1.0
bias = -1.5

sum = x1 * w1 + x2 * w2 + bias
output = activation(sum)

print("Weighted Sum =", sum)
print("AND Gate Output =", output)
