import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def main():
    DatasetPath = "student_performance_ml.csv"
    df = pd.read_csv(DatasetPath)

    plt.figure(figsize=(7,5))

    for sp in df["FinalResult"].unique():
        temp = df[df["FinalResult"] == sp]
        plt.scatter(temp["StudyHours"], temp["PreviousScore"], label = sp)

    plt.xlabel("StudyHours")
    plt.ylabel("PreviousScore")

    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()