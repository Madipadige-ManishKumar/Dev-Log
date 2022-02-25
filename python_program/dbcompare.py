import mysql.connector

# Define your database connection parameters
db_config = {
    "host": "localhost",    
    "user": "root",
    "password": "cme123",
    "database": "db1",
}

# Establish a database connection
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Define the input string
input_string = input("Enter The String ")

# Execute a query to retrieve the data as a string
query = "SELECT name FROM verfi"
cursor.execute(query)
result = cursor.fetchone()

if result:
    # Convert the retrieved data to a string
    retrieved_string = result[0]

    # Compare the retrieved string with the input string
    if retrieved_string == input_string:
        print("Strings are equal.")
    else:
        print("Strings are not equal.")
else:
    print("No data found in the database.")

# Close the database connection
conn.close()
