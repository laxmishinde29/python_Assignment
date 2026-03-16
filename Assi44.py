import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def main():

    print("Step 1 : Get data")

    df = pd.read_csv("Advertising.csv")

    print("Few records from data set:")
    print(df.head())

    print("Step 2 : Clean,Prepare and Manipulate")

    print("Shape of dataset before removal:",df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace=True)

    print("Shape of dataset after removal:",df.shape)

    print(Border)
    print("Clean data set is:")
    print(Border)

    print(df.head())

    print("Step 3 : Train data")

    X = df[['TV','radio','newspaper']]
    Y = df['sales']

    print("Shape of independent variables:",X.shape)
    print("Shape of dependent variables:",Y.shape)

    # Split the data set for training and  testing
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    print("X_train shape:",X_train.shape)
    print("X_test shape:",X_test.shape)
    print("Y_train shape:",Y_train.shape)
    print("Y_test shape:",Y_test.shape)

    # Create and train the model
    model = LinearRegression()
    
    model.fit(X_train,Y_train)

    print("Step 4 :  Test the model")

    Y_pred = model.predict(X_test)

    print("Step 5 : Compare the actual and predicted values ")

    Result = pd.DataFrame({
        'Actual sale' : Y_test.values,
        'Predicteed sale' : Y_pred
    })

    print(Result)



if __name__ == "__main__":
    main()
