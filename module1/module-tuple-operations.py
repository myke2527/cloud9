user_data = ('John', 'American', 1964)  # Define user data with name, nationality, and birth year
print(user_data)

user_data = ('John', 'American', 1964)
if 'American' in user_data:  # Check if 'American' is in user_data
    print('This person comes from the US!')

user_data = ('John', 'American', 1964)
for element in user_data:  # Iterate through elements in user_data
    print(element)

user_data = ('John', 'American', 1964) + ('teacher', 'male')  # Concatenate additional information
print(user_data)

numbers = (0, 1) * 10  # Repeat the tuple (0, 1) ten times
print(numbers)

male_names = ['Adam', 'Jerry', 'Mark']  # List of male names
print(male_names)