# Initialize a dictionary called 'grades'
grades = {}

# Add a key-value pair to the 'grades' dictionary
grades['John'] = 'A-'
grades['Anne'] = 'B'

# Print the 'grades' dictionary
print(grades)

# Update the grade for 'John' in the 'grades' dictionary
grades.update({'John':'A'})

# Print the 'grades' dictionary again
print(grades)

# Calculate and print the length of the 'grades' dictionary
len(grades)
print(grades, 'length is', len(grades))

# Check if 'John' is in the 'grades' dictionary and print his grade if found
if 'John' in grades:
    print('John got:', grades['John'])

# Commented out code to delete the entry for 'John' in the 'grades' dictionary
#del grades ['John']
#print(grades)

# Iterate through the keys (names) in the 'grades' dictionary and print them
for el in grades:
    print(el)

# Iterate through the keys (names) in the 'grades' dictionary using .keys() method and print them
for el in grades.keys():
    print(el)

# Iterate through the 'grades' dictionary and print each person's name and grade
for person, grade in grades.items():
    print(person, 'got', grade)