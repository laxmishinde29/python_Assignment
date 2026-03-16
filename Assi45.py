import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder , StandardScaler
from sklearn.metrics import accuracy_score


def main():
    print("Step 1: Get Data")

    df = pd.read_csv("WinePredictor.csv")

    print("-------------------------------------------------")

    print("Step 2 : clean the data ")

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X :",X.shape)
    print("Shape of Y :",Y.shape)

    print("-------------------------------------------------")

    print("step 3 : clean and test the data")

    X_train, X_test, Y_train , Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = KNeighborsClassifier(n_neighbors = 3)
    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    print("-------------------------------------------------")

    print("Step 4 : Calculate Accuracy")

    accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy:",accuracy)

if __name__ == "__main__":
    main()
