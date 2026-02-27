import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

sns.histplot("StudyHours")
plt.show()