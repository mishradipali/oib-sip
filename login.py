# //  Create a simple login authentication system using a 
# // programming language of your choice (e.g., Python, JavaScript, Java, etc.) 
# // that allows users to register, login, and access a secured page.

# Initialize an empty dictionary to store user credentials (username: password)
user_credentials = {}

def register():
    username = input("Enter a username: ")
    password = input("Enter a passwordB: ")
    user_credentials[username] = password
    print("Registration successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username in user_credentials and user_credentials[username] == password:
        print("Login successful!")
        return True
    else:
        print("Login failed. Invalid username or password.")
        return False

def secured_page():
    print("Welcome to the secured page!")


# Main program loop
while True:
    print("\nOptions:")
    print("1. Register")
    print("2. Login")
    print("3. Access Secured Page")
    print("4. Quit")
    
    choice = input("Select an option: ")
    
    if choice == "1":
        register()
    elif choice == "2":
        if login():
            secured_page()
    elif choice == "3":
        if login():
            secured_page()
    elif choice == "4":
        break
    
    else:
        print("Invalid choice. Please select a valid option.")
