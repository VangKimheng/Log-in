# User login system

# Dictionary to store user credentials
users = {'username': 'password'}

def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    users[username] = password
    print("Registration successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("Login successful! Welcome, " + username + "!")
    else:
        print("Login failed. Please check your username and password.")

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
