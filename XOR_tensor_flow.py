```xor tenserflow 
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# XOR input and output
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Define the model
model = Sequential()
model.add(Dense(4, input_dim=2, activation='tanh'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(
    loss='binary_crossentropy',
    optimizer=Adam(learning_rate=0.01),
    metrics=['accuracy']
)

# Train the model
history = model.fit(X, y, epochs=2000, verbose=0)

# Predict the output
predictions = model.predict(X, verbose=0)

print("\nPredictions for XOR:")
for i in range(4):
    print(
        f"Input: {X[i]} -> Predicted: {predictions[i][0]:.4f} "
        f"-> Rounded: {round(float(predictions[i][0]))}"
    )

# Plot training loss
plt.plot(history.history['loss'])
plt.title('Training Loss Curve')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True)
plt.show()
