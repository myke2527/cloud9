# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Bro", 21, "male")
print(student.count("Bro"))  # Count the number of occurrences of "Bro" in the tuple student
print(student.index("male"))  # Find the index of the first occurrence of "male" in the tuple student

for x in student:
    print(x)  # Iterate through the elements of the tuple student and print each element

if "Bro" in student:
    print("Bro is here!")  # Print a message if "Bro" is present in the tuple student