# Swapping values using a temporary variable
# first = input('Enter first number:')
# second = input('Enter second number:')
# print('Before swapping:', first, second)
# temporary = first
# first = second
# second = temporary
# print('After swapping:', first, second)

# Swapping values using tuple unpacking
# first = input('Enter first number:')
# second = input('Enter second number:')
# print('Before swapping:', first, second)
# first, second = second, first
# print('After swapping:', first, second)

top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)  # Swap the first and last elements in the list

top_cities.sort()
print(top_cities)  # Sort the list in ascending order

random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort()
print(random_numbers)  # Sort the list in ascending order

random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort(reverse=True)
print(random_numbers)  # Sort the list in descending order

# list_names.sort(): sorts the original list
# sorted(list_names): gives back a new sorted list, keeps the original unchanged
print(sorted(top_cities))
# print(top_cities)