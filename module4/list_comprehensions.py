numbers = [1, 2, 3, 4]
print(numbers)  # Print the list of numbers

numbers = []
for i in range(1, 101):
    numbers.append(i)
print(numbers)  # Create a list of numbers from 1 to 100 using a for loop and append each number to the list

numbers = [i for i in range(1, 101)]
print(numbers)  # Create a list of numbers from 1 to 100 using a list comprehension

numbers = [i for i in range(1, 101) if i % 3 != 0]
print(numbers)  # Create a list of numbers from 1 to 100 excluding multiples of 3 using a list comprehension