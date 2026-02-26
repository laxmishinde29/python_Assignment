import pandas as pd

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

print("Average StudyHours:")
print(df["StudyHours"].mean())

print("Average Attendance:")
print(df["Attendance"].mean())

print("Maximum PreviousScore:")
print(df["PreviousScore"].max())

print("Minimum SleepHours:")
print(df["SleepHours"].min())