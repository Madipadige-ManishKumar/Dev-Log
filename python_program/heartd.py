# import tkinter as tk
# from tkinter import ttk
# import joblib

# class HeartDiseaseApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Heart Disease Prediction App")

#         self.age_label = ttk.Label(root, text="Age:")
#         self.age_label.pack()
#         self.age_entry = ttk.Entry(root)
#         self.age_entry.pack()

#         self.sex_label = ttk.Label(root, text="Sex (0: Female, 1: Male):")
#         self.sex_label.pack()
#         self.sex_entry = ttk.Entry(root)
#         self.sex_entry.pack()

#         self.blood_pressure_label = ttk.Label(root, text="Resting Blood Pressure:")
#         self.blood_pressure_label.pack()
#         self.blood_pressure_entry = ttk.Entry(root)
#         self.blood_pressure_entry.pack()

#         # Add more input fields for other features

#         self.predict_button = ttk.Button(root, text="Predict", command=self.predict)
#         self.predict_button.pack()

#     def predict(self):
#         # Load the trained model
#         model = joblib.load("heart_disease_model.pkl")

#         # Get input values from user
#         age = float(self.age_entry.get())
#         sex = float(self.sex_entry.get())
#         blood_pressure = float(self.blood_pressure_entry.get())

#         # You'll need to add more feature inputs and preprocessing here

#         # Create input array
#         input_data = [[age, sex, blood_pressure]]  # Add more feature values

#         # Make prediction
#         prediction = model.predict(input_data)
#         if prediction[0] == 0:
#             result = "No Heart Disease"
#         else:
#             result = "Heart Disease"

#         result_label = ttk.Label(root, text=f"Prediction: {result}")
#         result_label.pack()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = HeartDiseaseApp(root)
#     root.mainloop()



import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib 
import rcParams
import matplotlib.cm import rainbow 
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')
