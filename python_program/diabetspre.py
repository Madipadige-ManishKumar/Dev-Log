import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the CSV file
data = pd.read_csv('diabetes.csv')

# Separate features (X) and target (y)
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # The Testing is 20% and training is 80% 

# Create and train a Random Forest classifier model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'diabetes_risk_model.pkl')

# Load the model
loaded_model = joblib.load('diabetes_risk_model.pkl')

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
input_data = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]]
prediction = loaded_model.predict_proba(input_data)

# Print the prediction result
if prediction[0][1] > 0.5:
    print("Based on the provided information, you have a higher risk of developing diabetes in the future.")
else:
    print("Based on the provided information, you have a lower risk of developing diabetes in the future.")
