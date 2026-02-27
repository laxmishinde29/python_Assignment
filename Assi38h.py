import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

sns.boxplot(x=["Attendence"])
plt.show()