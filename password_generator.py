import random
import string

def generate_password(length):
    # Define character sets
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        # Get user input for password length
        length = int(input("Enter the desired password length: "))
        
        # Validate input
        if length < 1:
            print("Password length must be at least 1.")
        else:
            # Generate and display password
            password = generate_password(length)
            print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
