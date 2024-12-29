import random

def generate_password(length):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "!@#$%^&*()_+-=[]\{\}|;:,.<>?/"
    #Declaration of the letters,digits,symbols
    # Combine all characters
    all_characters = letters + digits + symbols
    
    password = ""
    
    # Generate password using a loop and random
    for _ in range(length):
        password += random.choice(all_characters)
    
    return password

# User's requirement asking section
def password_length():
    pass_length = int(input("Enter the desired password length: "))
    if pass_length < 3:
        print("Password length must be at least 4.")
    else:
        return pass_length
pass_length=password_length()   
random_password = generate_password(pass_length)
print(f"Generated Password: {random_password}")
