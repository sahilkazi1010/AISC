#Supervised

import numpy as np

print("SUPERVISED LEARNING - DELTA RULE")

# Input patterns
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
], dtype=float)

# Target outputs (OR function)
T = np.array([0, 1, 1, 1], dtype=float)

# Initial weights and bias
weights = np.zeros(2)
bias = 0.0

# Learning rate and epochs
learning_rate = 0.1
epochs = 20

# Training
for epoch in range(epochs):
    total_error = 0

    for i in range(len(X)):
        net = np.dot(X[i], weights) + bias
        error = T[i] - net

        # Update weights and bias
        weights = weights + learning_rate * error * X[i]
        bias = bias + learning_rate * error

        total_error += error ** 2

    print("Epoch:", epoch + 1,
          "Weights:", weights,
          "Bias:", round(bias, 3),
          "Error:", round(total_error, 3))

print("\nFinal Weights:", weights)
print("Final Bias:", bias)

# Testing
print("\nTesting Delta Rule:")

for x in X:
    net = np.dot(x, weights) + bias

    if net >= 0.5:
        output = 1
    else:
        output = 0

    print("Input:", x, "Output:", output)
