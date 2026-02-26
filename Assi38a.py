import pandas as pd

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

print("First Five records of dataset:")
print(df.head())

print("Last five record of dataset:")
print(df.tail())

print("Total number of rows and column :")
print(df.shape)

print(df.dtypes)