# # # import pandas as pd
# # # from sklearn.model_selection import train_test_split
# # # from sklearn.linear_model import LogisticRegression
# # # from sklearn.metrics import accuracy_score

# # # # Load example dataset (replace with your actual data)
# # # data = pd.read_csv('abc.csv')

# # # # Preprocessing: Clean and prepare the data
# # # # You would need to handle missing values, convert categorical variables, and more

# # # # Split the data into features and target variable
# # # X = data.drop(columns=['outbreak'])
# # # y = data['outbreak']

# # # # Split the data into training and testing sets
# # # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # # # Build a logistic regression model (you can use more advanced models)
# # # model = LogisticRegression()

# # # # Train the model on the training data
# # # model.fit(X_train, y_train)

# # # # Make predictions on the test data
# # # predictions = model.predict(X_test)

# # # # Evaluate the model
# # # accuracy = accuracy_score(y_test, predictions)
# # # print(f"Accuracy: {accuracy:.2f}")




# # # stock predictor 
# import yfinance as yf
# # import pandas as pd
# # import numpy as np
# # from sklearn.model_selection import train_test_split
# # from sklearn.linear_model import LinearRegression
# # import matplotlib.pyplot as plt
# # from tabulate import tabulate

# # # Fetch historical stock data
# # stock_symbol = "AAPL"  # Change this to your desired stock symbol
# # start_date = "2010-01-01"
# # end_date = "2020-12-31"
# # stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# # # Calculate daily returns
# # stock_data['Daily_Return'] = stock_data['Adj Close'].pct_change()

# # # Drop missing values
# # stock_data.dropna(inplace=True)

# # # Features and target variable
# # X = stock_data[['Open', 'High', 'Low', 'Volume']]
# # y = stock_data['Adj Close']

# # # Splitting the data into training and testing sets
# # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # # Creating and training the model
# # model = LinearRegression()
# # model.fit(X_train, y_train)

# # # Predicting stock prices
# # y_pred = model.predict(X_test)

# # # Create a table
# # table_data = {
# #     'Date': y_test.index,
# #     'Actual Prices': y_test.values,
# #     'Predicted Prices': y_pred
# # }

# # table = tabulate(table_data, headers='keys', tablefmt='grid')

# # # Create a figure with subplots
# # fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# # # Plot actual prices
# # axs[0].plot(y_test.index, y_test.values, label='Actual Prices')
# # axs[0].set_xlabel('Date')
# # axs[0].set_ylabel('Stock Price')
# # axs[0].set_title('Actual Stock Prices')
# # axs[0].legend()

# # # Plot predicted prices
# # axs[1].plot(y_test.index, y_pred, label='Predicted Prices', linestyle='dashed', color='orange')
# # axs[1].set_xlabel('Date')
# # axs[1].set_ylabel('Stock Price')
# # axs[1].set_title('Predicted Stock Prices')
# # axs[1].legend()

# # # Save figures as image files
# # fig.savefig('stock_prices.png')
# # plt.close(fig)  # Close the figure to release memory

# # # Display the table
# # print(table)



# # import numpy as np
# # import pandas as pd
# # from sklearn.model_selection import train_test_split
# # from sklearn.preprocessing import StandardScaler
# # from sklearn.ensemble import RandomForestClassifier
# # from sklearn.metrics import accuracy_score, classification_report

# # # Load data
# # data = pd.read_csv("heart.csv")
# # X = data.drop("target", axis=1)
# # y = data["target"]

# # # Split data into training and testing sets
# # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # # Feature scaling
# # scaler = StandardScaler()
# # X_train_scaled = scaler.fit_transform(X_train)
# # X_test_scaled = scaler.transform(X_test)

# # # Build and train the model
# # model = RandomForestClassifier(n_estimators=100, random_state=42)
# # model.fit(X_train_scaled, y_train)

# # # Make predictions
# # y_pred = model.predict(X_test_scaled)

# # # Evaluate the model
# # accuracy = accuracy_score(y_test, y_pred)
# # report = classification_report(y_test, y_pred)

# # print(f"Accuracy: {accuracy:.2f}")
# # print("Classification Report:\n", report)



# import seaborn as sns

# # Load the Heart Disease dataset
# heart_data = sns.load_dataset("heart")

# # Display the first few rows of the dataset
# print(heart_data.head())

print ("hello")

print("hello world")