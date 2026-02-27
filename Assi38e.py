import pandas as pd

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

print("\nAverage StudyHours by Result:")
print(df.groupby("FinalResult")["StudyHours"].mean())

print("\nAverage Attendance by Result:")
print(df.groupby("FinalResult")["Attendance"].mean())