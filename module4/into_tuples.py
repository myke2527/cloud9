empty_tuple = ()
print(empty_tuple)  # Print an empty tuple

one_element_tuple_a = (1,)
print(one_element_tuple_a)  # Print a tuple with one element

three_element_tuple = 1, 2, 3,
print(three_element_tuple)  # Print a tuple with three elements

user_data = ('John', 'American', 1964)
print(user_data)  # Print the tuple user_data

# Tuple cannot append
# user_data.append('teacher')
# The commented lines above would raise an AttributeError because tuples are immutable and do not support append operations.

# Tuple does not support item deletion
# del user_data[0]
# The commented lines above would raise a TypeError because tuples do not support item deletion.

print(user_data[0])  # Print the first element of the tuple user_data
