import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Create a synthetic dataset
data = {
    'Feature1': [1.2, 2.5, 3.0, 4.1, 5.2, 6.0, 7.3, 8.1, 9.5, 10.0],
    'Feature2': [0.8, 1.5, 2.0, 2.7, 3.1, 3.8, 4.2, 5.0, 5.5, 6.2],
    'Target': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
}

# Create a DataFrame from the synthetic data
df = pd.DataFrame(data)

# Display the DataFrame
print("Synthetic Dataset:")
print(df)

# Split the data into features (X) and target variable (y)
X = df[['Feature1', 'Feature2']]
y = df['Target']


print("This is X")
print(X)

print("This is Y")
print(y)
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model on the training data
rf_classifier.fit(X_train, y_train)

# Make predictions on the test data
predictions = rf_classifier.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, predictions)
print(f"\nAccuracy: {accuracy:.2f}")
