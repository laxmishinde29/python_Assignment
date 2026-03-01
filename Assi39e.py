import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


# Load dataset
dataset = pd.read_csv("student_performance_ml.csv")

# Separate features and label
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Create model object
model = DecisionTreeClassifier()

# Train model
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Model trained successfully")

print("Predicted values:", y_pred)
print("Actual values   :", y_test.values)

train_accuracy = model.score(X_train, y_train)
test_accuracy = model.score(X_test, y_test)

print("Training Accuracy:", train_accuracy * 100)
print("Testing Accuracy :", test_accuracy * 100)