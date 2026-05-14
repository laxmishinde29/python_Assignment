# customer stay/leave Prediction using Feedforward Neural Network

# Import required libraries
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report

# ------------------------------------------------------------
# Step 1: Prepare the dataset
# Each row contains:
# [Age, Monthly Charges, Tenure, Number of complaints, customer support calls]
# Output:
# 0 = Customer will stay
# 1 = Customer will leave
# ------------------------------------------------------------

X = [
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 1500, 5, 6, 10],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12], 
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7],
]

y = [0, 0, 1, 1, 0, 0, 1, 1, 0, 1]

# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# ------------------------------------------------------------
# Step 3: Create the Feedforward Neural Network model
# hidden_layer_sizes=(5,) means 1 hidden layer with 5 neurons
# activation='relu' is used in hidden layer
# max_iter=1000 means training runs up to 1000 times if needed
# ------------------------------------------------------------

model = MLPClassifier(
    hidden_layer_sizes=(5,),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)

# ------------------------------------------------------------
# Step 4: Train the model
# The model learns patterns from training data
# ------------------------------------------------------------

model.fit(X_train, y_train)

# ------------------------------------------------------------
# Step 5: Predict using test data
# ------------------------------------------------------------

y_pred = model.predict(X_test)

# ------------------------------------------------------------
# Step 6: Check model accuracy
# ------------------------------------------------------------

print("Actual Output   :", y_test)
print("Predicted Output:", y_pred.tolist())

accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy of model:", accuracy)

# Detailed report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ------------------------------------------------------------
# Step 7: Test with new student data
# Example:
# Study Hours = 5
# Attendance = 75
# Assignment Score = 60
# ------------------------------------------------------------

new_customer = [[46, 1450, 5, 6, 9]]
prediction = model.predict(new_customer)

if prediction[0] == 1:
    print("\nNew customer: Leave")
else:
    print("\n New customer: Stay")