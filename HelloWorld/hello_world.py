# This is a Python script that prints a greeting message

def get_username():
    # Function to get user's name
    username = input("Enter your name: ")
    return username

def greet_user(name):
    # Function to greet the user
    print(f"Hello, {name}! Welcome to the world of Python.")

def main():
    # Main function
    user_name = get_username()
    greet_user(user_name)

if __name__ == "__main__":
    # Check if the script is run as the main program
    main()
