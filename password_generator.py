import random
import string

def generate_password(length=12):
    # Define characters: lowercase, uppercase, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly choose characters for the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("🔐 Password Generator")
    length = int(input("Enter password length: "))
    print("Generated password:", generate_password(length))
