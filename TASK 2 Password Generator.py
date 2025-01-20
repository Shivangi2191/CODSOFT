import random

# User can manually enter password length 
length = int(input("How long do you want the password to be: "))

# Different character to be used in making password
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

# Combine all character types
all_characters = letters + numbers + symbols

# Generate the password by picking random characters
password = ""
for _ in range(length):
    password += random.choice(all_characters)

# Show the generated password
print("Your password is: ", password)
