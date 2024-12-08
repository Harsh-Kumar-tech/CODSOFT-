import random
import string
def generate_password(length):
    # Define the character pool
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password of the desired length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("Welcome to the Password Generator!")
    # Get user input for the desired length
    try:
        length = int(input("Enter the desired password length (minimum 6 characters): "))
        if length < 6:
            print("Password length should be at least 6 characters.")
            return
        # Generate and display the password
        password = generate_password(length)
        print(f"Your generated password is: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")
# Run the main function
if __name__ == "__main__":
    main()