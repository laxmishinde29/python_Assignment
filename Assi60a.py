# Import numpy for numerical operations
import numpy as np
import math

# ---------------------------------------------------------
# STEP 1 : Define Input Features
# ---------------------------------------------------------
# These are the inputs coming to the neuron (x1, x2, x3)

inputs = np.array([2, 3])

# ---------------------------------------------------------
# STEP 2 : Define Weights
# ---------------------------------------------------------
# Each input has a corresponding weight (w1, w2, w3)
# Weights represent importance of each input

weights = np.array([0.4,0.6])

# ---------------------------------------------------------
# STEP 3 : Define Bias
# ---------------------------------------------------------
# Bias is an additional parameter that helps shift the output
# It allows the model to fit data better

bias = 0.5

# ---------------------------------------------------------
# STEP 4 : Calculate Weighted Sum (Z)
# ---------------------------------------------------------
# Formula:
# Z = (x1*w1 + x2*w2 + x3*w3) + bias
# Using numpy dot product for efficient calculation

weighted_sum = np.dot(inputs, weights) + bias


# ---------------------------------------------------------
# STEP 5 : Activation Function (ReLU)
# ---------------------------------------------------------
# ReLU (Rectified Linear Unit):
# If value > 0 → return value
# If value <= 0 → return 0

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# ---------------------------------------------------------
# STEP 6 : Final Output
# ---------------------------------------------------------
# Pass the weighted sum through activation function

output = sigmoid(weighted_sum)

# ---------------------------------------------------------
# STEP 7 : Display Results
# ---------------------------------------------------------

print("Inputs          :", inputs)
print("Weights         :", weights)
print("Bias            :", bias)
print("Weighted Sum (Z):", weighted_sum)
print("Final Output    :", output)