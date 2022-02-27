import pymysql

# Connection details
host = 'localhost'  # Replace with your MySQL server hostname
user = 'root'  # Replace with your MySQL username
password = 'cme123'  # Replace with your MySQL password
database = 'challenge'  # Replace with your MySQL database name

# Establish a connection
connection = pymysql.connect(host=host, user=user, password=password, database=database)
try:
    cursor = connection.cursor()


    while True:
        print("Press 1 To See The Savings")
        print("Press 2 To See The Risk Coins Of Both ")
        print("Press 3 To Invest In Risk")
        print("Press 4 To See The Result ")
        print("Press  5 To Exit")
        c=int(input("Enter The Choice "))
        if c==5:
            break;
        elif c==1:
             cursor.execute("SELECT savings  FROM Bank where name='Manish'")
             rows = cursor.fetchall()
             print(rows)
        elif c==2:
            cursor.execute("SELECT  risk  FROM Bank")
            rows = cursor.fetchall()
            print("The rows Are ",rows)
            i=0
            for row in rows:
               if i==0:
                   print("oppoent :",row) 
                   i=i+1;
               else:
                   print("Your Coins",row)
        elif c==3:
            inv=int(input("Enter Money To Invest"))
            cursor.execute("SELECT savings FROM Bank where name='Manish'")
            rows = cursor.fetchall()
            rows[0]=int(rows[0]-inv)
            print(rows[0])

        
except  Exception as e:
    print(e)

# try:
#     # Create a cursor object
#     cursor = connection.cursor()

#     # Execute SELECT query
#     cursor.execute("SELECT * FROM Bank")
    
#     # Fetch all the rows returned by the query
#     rows = cursor.fetchall()
    
#     # Process the rows
#     for row in rows:
#         print(row)

# finally:
#     # Close the cursor and connection
#     cursor.close()
#     connection.close()