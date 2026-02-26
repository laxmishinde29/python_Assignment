import pandas as pd

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

print("Total number of student in the dataset:")
print(len(df))

print("Number of students is passed :")
print((df["FinalResult"]==1).sum())

print("Number of students is failed :")
print((df["FinalResult"]==0).sum())