import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="alpha123"
)

cursor = conn.cursor()

print("Please select an option:")
print("\n1. Show User Data ")
print("2. Show Login username&Password")
print("3. Show output data")

while True:
    choice = input("\nEnter your choice : ")
    if choice == "1":
        print("\nYou selected User information .")
        cursor.execute("SELECT * FROM users")  # FOR USER DATA
        break

    elif choice == "2":
        print("\nYou selected User login information.")
        cursor.execute("SELECT * FROM login")  # FOR LOGIN USERNAME AND PASSWORD
        break

    elif choice == "3":
        print("\nYou selected Output data of PMS .")
        cursor.execute("SELECT * FROM output")  # FOR OUTPUT DATA
        break

    else:

        print("\n\033[31mInvalid choice. Please enter 1, 2, or 3.\033[0m")

rows = cursor.fetchall()
print([desc[0] for desc in cursor.description])

for row in rows:
    print(row)

cursor.close()
conn.close()
