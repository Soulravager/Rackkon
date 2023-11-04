import sys

import psycopg2
import time

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="alpha123"
)
cursor = conn.cursor()
print("Please select an option:")
print("\n1. Insert values to User Data ")
print("2. Insert values to username&Password")
print("3. exit")


while True:
    choice = input("\nEnter your choice : ")
    if choice == "1":
        print("\nYou selected to insert User data .")
        x = input("\nEnter Owner Name:")
        y = input("\nEnter Registration Number:")
        sql = """INSERT INTO users (lc_number, User_name)
                 VALUES (%s,%s)"""
        data = (y, x)
        print("data added to Database")
        cursor.execute(sql, data)
        time.sleep(1)
        print("Data from Users")
        cursor.execute("SELECT * FROM users")  # FOR USER DATA

    elif choice == "2":
        print("You selected to insert User login data")
        x = input("\nEnter Login_id:")
        y = input("\nEnter Password:")
        sql = """INSERT INTO login (user_id, password)
                 VALUES (%s,%s)"""
        data = (x, y)
        print("data added to Database")
        cursor.execute(sql, data)
        time.sleep(1)
        print("Data from Login")
        cursor.execute("SELECT * FROM login")  # FOR LOGIN USERNAME AND PASSWORD3
        conn.commit()
        cursor.close()
        conn.close()
    elif choice == "3":
        print("exiting...")
        sys.exit()




    else:

        print("\033[31mInvalid choice.Please Enter option 1 or 2 !!\033[0m")

rows = cursor.fetchall()
print([desc[0] for desc in cursor.description])

for row in rows:
    print(row)


conn.commit()
cursor.close()
conn.close()
