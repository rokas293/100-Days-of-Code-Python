#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Collect the outputs of each loop into a list
password_list = []

for i in range(0, nr_letters):
    random_Letter = random.choice(letters)
    password_list.append(random_Letter)

for j in range(0, nr_symbols):
    random_Symbol = random.choice(symbols)
    password_list.append(random_Symbol)

for k in range(0, nr_numbers):
    random_Number = random.choice(numbers)
    password_list.append(random_Number)

# Shuffle the combined output
random.shuffle(password_list)

# Print the shuffled list as the final password
password = ''.join(password_list)
print(f"Your generated password is: {password}")


# Check to see password length
if len(password) <= 6:
    print("Your password is weak, try to include at least 8 characters for a stronger password.")
elif len(password) == 7:
    print("Your password is medium, try to include at least 8 characters for a stronger password.")
else:
    print("Your password is strong.")
