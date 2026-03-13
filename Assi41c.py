from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

X = [[2,60],[5,80],[6,85],[1,50]]
Y = [1,2,2,1]

Scalar = StandardScaler()
X_Scaled = Scalar.fit_transform(X)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_Scaled,Y)

X1_new = int(input("Enter StudyHours:"))
X2_new = int(input("Enter attendence:"))

new = [[X1_new,X2_new]]
new_Scaled = Scalar.transform(new)

prediction = model.predict(new_Scaled)[0]

if(prediction == 1):
    print("Student is fail")

else:
    print("Student is pass")