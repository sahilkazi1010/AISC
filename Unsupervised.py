#unsupervised

import numpy as np

print("UNSUPERVISED LEARNING - HEBBIAN RULE")

# Input patterns
X = np.array([
    [1, 1],
    [1, -1],
    [-1, 1],
    [-1, -1]
], dtype=float)

# Initial weight matrix
weights = np.zeros((2, 2))
learning_rate = 0.1

# Hebbian Learning
for x in X:
    # Outer product of input vector
    weight_change = learning_rate * np.outer(x, x)

    # Update weights
    weights = weights + weight_change

    print("\nInput:", x)
    print("Updated Weight Matrix:")
    print(weights)

print("\nFinal Hebbian Weight Matrix:")
print(weights)
