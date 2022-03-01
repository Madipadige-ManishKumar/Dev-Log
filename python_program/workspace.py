import pandas as pd
import numpy as np 
from  sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
data=pd.read_csv('diabetes.csv')
import joblib
X=data.drop('Outcome',axis=1)
y=data['Outcome']

x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=RandomForestClassifier(n_estimators=40)
model.fit(x_train,y_train)

joblib.dump(model,'trainedmodel.pkl')
loaded_model=joblib.load('trainedmodel.pkl')

# Get user input for feature values
pregnancies = float(input("Enter number of pregnancies: "))
glucose = float(input("Enter glucose level: "))
blood_pressure = float(input("Enter blood pressure: "))
skin_thickness = float(input("Enter skin thickness: "))
insulin = float(input("Enter insulin level: "))
bmi = float(input("Enter BMI: "))
diabetes_pedigree = float(input("Enter diabetes pedigree function: "))
age = float(input("Enter age: "))



input_data = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]]

precdition =loaded_model.predict_proba(input_data)
print(precdition)