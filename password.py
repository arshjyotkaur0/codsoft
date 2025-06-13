import random
import string

length = int(input("Enter the desired password length: "))


uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation


all_characters = uppercase_letters + lowercase_letters + digits + symbols

password = ''.join(random.choice(all_characters) for _ in range(length))

print(f"Your generated password is: {password}")
