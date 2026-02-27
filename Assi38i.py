import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def main():
    DatasetPath = "student_performance_ml.csv"
    df = pd.read_csv(DatasetPath)

    plt.figure(figsize=(8,9))

    for sp in df["FinalResult"].unique():
        temp = df[df["FinalResult"] == sp]
        plt.scatter(temp["AssignmentsCompleted"], temp["FinalResult"], label = sp)

    plt.xlabel("AssignmentsCompleted")
    plt.ylabel("FinalResult")

    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()