import  matplotlib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv('diabetes.csv')

X = data.drop('Outcome', axis=1)
y = data['Outcome']

x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2)#,random_state=10)

# Random_state= will keep the data set constant 
print(len(x_train))

print(x_test)