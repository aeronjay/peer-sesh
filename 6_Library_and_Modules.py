# 6. Working with Libraries and Modules

# Welcome to the next step in Python!
# Let's explore libraries and modules by solving a simple problem.

# Problem Set: "Random Password Generator"
# Goal: Use standard and third-party libraries to generate secure passwords.

# Step 1: Using Standard Libraries
import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Generated Password:", generate_password(12))

# Step 2: Working with the datetime Module
import datetime

current_time = datetime.datetime.now()
print("Current Date and Time:", current_time)

# Step 3: Installing and Using Third-Party Libraries
# Install 'requests' using: pip install requests


# Summary:
# - Standard libraries like random, string, and datetime offer built-in functionality.
# - Third-party libraries expand Python’s capabilities.
# - The 'requests' library allows us to make web requests.

# Challenge: Modify the program to let users choose the length and complexity of their password!
