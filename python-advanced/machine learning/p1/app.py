from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Load the data

data=pd.read_csv("data.csv")
data=pd.DataFrame(data)

# Prepare the data

X = data['Input']
y = data['output']

# Convert text data to numeric vectors using TfidfVectorizer
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Take input from the user and convert to feature vector
my_in = input("Enter a String: ")
my_in_vectorized = vectorizer.transform([my_in])

# Predict probabilities
l = model.predict_proba(my_in_vectorized)

# Check the probability of class '1'
if l[0][1] > 0.5:
    print("Doing Google Search")
    
else:
    print("I can't see right now, I will get updated.")
