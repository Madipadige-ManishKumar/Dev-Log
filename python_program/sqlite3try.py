# import sqlite3
# import os
# curdir = os.path.dirname(os.path.abspath(__file__))

# class posts:
#     def slug_method(self, S):
#         conn, cursor = get_db_connection()
#         self.name = cursor.execute("SELECT post_name FROM posts WHERE slug=?", (S,)).fetchone()
#         self.content = cursor.execute("SELECT post_content FROM posts WHERE slug=?", (S,)).fetchone()
#         self.img = cursor.execute("SELECT post_img FROM posts WHERE slug=?", (S,)).fetchone()
#     def fetchall_m(self):
#         conn, cursor = get_db_connection()

#         self.name = cursor.execute("SELECT post_name FROM posts").fetchall()
#         self.content = cursor.execute("SELECT post_content FROM posts ").fetchall()
#         self.img = cursor.execute("SELECT post_img FROM posts ").fetchall()
# def get_db_connection():
#     db_path = os.path.join(curdir, "flaskadvance.db")
#     connection = sqlite3.connect(db_path)
#     cursor = connection.cursor()
#     return connection, cursor

# post=posts()
# post.fetchall_m()

# print(post.name[2])


# for i in range( len(post.name)):
#     post.name[i]

number1 = 5.0
number2 = 5.001

# Define the maximum allowed difference (you can adjust this as needed)
max_difference = 0.01

# Check if the numbers are close
if abs(number1 - number2) <= max_difference:
    print("The numbers are close.")
else:
    print("The numbers are not close.")