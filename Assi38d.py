import pandas as pd

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

counts = df["FinalResult"].value_counts()
print("Distribution of final result",counts)

total = len(df)

print("\nPercentage of Pass students:")
pass_student = (df["FinalResult"] == 1).sum() / total
print(pass_student * 100)

print("\nPercentage of Fail students:")
fail_student = (df["FinalResult"] == 0).sum() / total
print(fail_student * 100)

