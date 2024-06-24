import random
import string

def generate_password(length):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

     # Generate the password by randomly selecting characters from the character set
    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password

# Get the desired password length from the user
password_length = int(input("Enter the desired password length: "))

# Generate the password
password = generate_password(password_length)

# Print the generated password
print("Generated Password:", password)