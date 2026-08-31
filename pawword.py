import random
import string

name = input("Enter your name: ")
surname = input("Enter your surname: ")

# Combine name and surname
user_info = name + surname

# Characters available for the random part
chars = string.ascii_letters + string.digits + string.punctuation

length = 16

# Use part of the user's name in the password
name_part = name[:3]

# Calculate remaining password length
remaining_length = length - len(name_part)

# Generate random characters
random_part = "".join(random.choice(chars) for _ in range(remaining_length))

# Combine the name and random characters
password = name_part + random_part

print("Generated password:", password)