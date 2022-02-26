import pandas  as pd 
import numpy  as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib


data=pd.read_csv('heart.csv')
X=data.drop('target',axis=1)
y=data['target']

x_train,x_test,y_train,y_test=train_test_split(X,y,random_state=42,test_size=0.2)


model=RandomForestClassifier(n_estimators=40)
model.fit(x_train,y_train)

joblib.dump(model,'hearttrain.pkl')


loaded_model=joblib.load('hearttrain.pkl')

age=int(input("Enter Age"))
gender=int(input("Enter Gender"))
cp=int(input("Enter cp"))
trestbps=int(input("Enter  trestbps"))
chol=int(input("Enterchol"))
fbs=int(input("Enter fbs"))
restecg=int(input("Enter restecg"))
thalach=int(input("Enter Thalach"))
exang=int(input("Enter exang"))
oldpeak=float(input("Enter old peak"))
slope=int(input("Enter slope "))
ca=int(input("Enter  ca "))
thal=int(input("Ente thal"))


input_data=[[age,gender,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]
prediction = loaded_model.predict_proba(input_data)

# Print the prediction result
if prediction[0][1] > 0.5:
    print("Based on the provided information, you have a higher risk of developing diabetes in the future.")
else:
    print("Based on the provided information, you have a lower risk of developing diabetes in the future.")


