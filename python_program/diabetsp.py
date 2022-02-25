import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

# Load the CSV file
data = pd.read_csv('diabetes.csv')   # Reading the Diabetes.csv File Using the pandas 

# Separate features (X) and target (y)
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create and train a logistic regression model
model = LogisticRegression()
model.fit(X_scaled, y)

# Saving the tranied model 
joblib.dump(model, 'diabetes_model.pkl')    # The Model is saved into diabetes_model.pkl   i.e pickle 

# Load the model
loaded_model = joblib.load('diabetes_model.pkl')  # The Save model which is in the diabetes_model.pkl  is now loaded in loaded_model variable 

# Get user input for feature values
pregnancies = float(input("Enter number of pregnancies: "))
glucose = float(input("Enter glucose level: "))
blood_pressure = float(input("Enter blood pressure: "))
skin_thickness = float(input("Enter skin thickness: "))
insulin = float(input("Enter insulin level: "))
bmi = float(input("Enter BMI: "))
diabetes_pedigree = float(input("Enter diabetes pedigree function: "))
age = float(input("Enter age: "))

# Prepare input data for prediction   
# Creating an array using the numpy
input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
input_data_scaled = scaler.transform(input_data)

# Predict using the loaded model
prediction = loaded_model.predict(input_data_scaled)

# Print the prediction result
if prediction[0] == 0:
    print("Based on the provided information, you are predicted to be non-diabetic.")
else:
    print("Based on the provided information, you are predicted to have diabetes.")
