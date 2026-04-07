import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

def LoadDataset(datapath):
    print("Step 1 : loading the dataset")

    df = pd.read_csv(datapath)

    print("Data set loaded successfully")

    Display(df)

def Display(df):
    #print(message)

    print("First five rows of dataset")
    print(df.head())

    print("Count of Null values from each column:")
    print(df.isnull().sum())

    print("Statistics of dataset:")
    print(df.describe())

    sns.boxplot(x=["Otcome"])

    plt.show()

    DataPreprocessing(df)

def DataPreprocessing(df):
    # Replacing 0 with mean
    print("Zero values in Glucose column :")
    print((df["Glucose"]==0).sum())
    mean = df["Glucose"].replace(0,np.nan).mean()
    df["Glucose"].replace(0,mean)

    # replaing 0 with nan
    print("Zero values in BloodPressure column:")
    print((df["BloodPressure"]==0).sum())
    mean = df["BloodPressure"].replace(0,np.nan)

    #split dataset into X and Y

    X = df.drop(columns=["Outcome"])
    Y = df["Outcome"]

    print("Shape of Independent variables :",X.shape)
    print("Shape of dependent variables :",Y.shape)

    print("Input columns :",X.columns.tolist())
    print("Output columns :'Outcome")

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)

    ModelBuilding(X_train_scaled,X_test_scaled,Y_train,Y_test)


def ModelBuilding(X_train_scaled, X_test_scaled, Y_train, Y_test):
    model1 = LogisticRegression()
    model1.fit(X_train_scaled,Y_train)

    model2 = KNeighborsClassifier()
    model2.fit(X_train_scaled,Y_train)

    print("Model training done successfully")

    ModelPrediction(X_test_scaled,Y_test,model1,model2)

def ModelPrediction(X_test_scaled,Y_test,model1,model2):

    Y_pred1 = model1.predict(X_test_scaled)
    print("Prediction Output from LogisticRegression")
    print(Y_pred1)

    Y_pred2 = model2.predict(X_test_scaled)
    print("Prediction Output from KNeighborsClassifier")
    print(Y_pred2)

    predictions_df = pd.DataFrame({
        "LogisticRegression_Prediction": Y_pred1,
        "KNeighborsClassifier_Prediction": Y_pred2
    })

    predictions_df.to_csv("model_predictions.csv",index = False)

def main():
    LoadDataset("diabetes.csv")

if __name__ == "__main__":
    main()