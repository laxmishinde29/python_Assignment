import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def main():
    DatasetPath = "student_performance_ml.csv"
    df = pd.read_csv(DatasetPath)

    plt.figure(figsize=(7,6))

    for sp in df["FinalResult"].unique():
        temp = df[df["FinalResult"] == sp]
        plt.scatter(temp["SleepHours"], temp["FinalResult"], label = sp)

    plt.xlabel("SleepHours")
    plt.ylabel("FinalResult")

    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()