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

new_data = pd.DataFrame([{
    "StudyHours":6,
    "Attendance":85,
    "PreviousScore":66,
    "AssignmentsCompleted":7,
    "SleepHours":7
}])

y_pred = model.predict(new_data)

if(y_pred==0):
    print("Student is fail")
else:
    print("Student is pass")