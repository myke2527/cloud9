import random

number = random.randint(0, 10)  # Generate a random integer between 0 and 10 (inclusive)

if number > 6:
    print("Big number")  # Print a message if the generated number is greater than 6

elif number < 6:
    print("Small number")  # Print a message if the generated number is less than 6

print(number)  # Print the generated random number