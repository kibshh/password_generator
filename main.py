import random

print("Welcome to Kibsh's password generator!")

letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "1234567890"
symbols = "!@#$%^&*"

while True:
    try:
        num_letters = int(input("How many letters would you like your password to have? "))
        break
    except ValueError:
        print("Invalid input, please enter a valid integer.")

while True:
    try:
        num_symbols = int(input("How many symbols would you like your password to have? "))
        break
    except ValueError:
        print("Invalid input, please enter a valid integer.")

while True:
    try:
        num_numbers = int(input("How many numbers would you like your password to have? "))
        break
    except ValueError:
        print("Invalid input, please enter a valid integer.")

password = []

for letter in range(num_letters):
    rand_index = random.randint(0, len(letters) - 1)
    password.append(letters[rand_index])
for num in range(num_numbers):
    rand_index = random.randint(0, len(numbers) - 1)
    password.append(numbers[rand_index])
for symbol in range(num_symbols):
    rand_index = random.randint(0, len(symbols) - 1)
    password.append(symbols[rand_index])

random.shuffle(password)

final_password = ""
for a in password:
    final_password += a

print(f"Your generated password is: {final_password}")
