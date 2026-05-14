import numpy as np

# ---------------------------------------------------------
# 1. Take Input Values
# ---------------------------------------------------------
# You can change these values
actual = [1, 0, 1, 1]
predicted = [0.9, 0.2, 0.8, 0.7]

# ---------------------------------------------------------
# 2. Mean Squared Error (MSE)
# ---------------------------------------------------------
def mean_squared_error(actual, predicted):
    actual = np.array(actual)
    predicted = np.array(predicted)
    return np.mean((actual - predicted) ** 2)

# ---------------------------------------------------------
# 3. Binary Cross Entropy (BCE)
# ---------------------------------------------------------
def binary_cross_entropy(actual, predicted):
    actual = np.array(actual)
    predicted = np.array(predicted)
    
    # To avoid log(0)
    epsilon = 1e-10
    predicted = np.clip(predicted, epsilon, 1 - epsilon)
    
    return -np.mean(
        actual * np.log(predicted) + 
        (1 - actual) * np.log(1 - predicted)
    )

# ---------------------------------------------------------
# 4. Calculate Loss
# ---------------------------------------------------------
mse_loss = mean_squared_error(actual, predicted)   #MSE calculates the average of squared differences between actual and predicted values.
                                                   #It is mainly used in regression problems where output is continuous.
                                                   
bce_loss = binary_cross_entropy(actual, predicted) #BCE measures the difference between actual labels (0/1) and predicted probabilities (0–1).
                                                   #It is used in binary classification problems.

# ---------------------------------------------------------
# 5. Display Output
# ---------------------------------------------------------
print("Actual Values       :", actual)
print("Predicted Values    :", predicted)
print("Mean Squared Error  :", mse_loss)
print("Binary Cross Entropy:", bce_loss)