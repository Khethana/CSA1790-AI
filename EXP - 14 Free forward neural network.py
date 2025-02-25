import math

# Activation Function (Sigmoid)
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Input values (Example: two inputs)
inputs = [1, 1]

# Weights for each input (randomly initialized)
weights = [0.5, -0.5]

# Bias term
bias = 0.2

# Compute Weighted Sum
weighted_sum = inputs[0] * weights[0] + inputs[1] * weights[1] + bias

# Apply Activation Function
output = sigmoid(weighted_sum)

# Print the final output
print("Feedforward Neural Network Output:", output)
