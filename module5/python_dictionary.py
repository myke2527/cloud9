# dictionary = A changeable, unordered collection of unique key:value pairs 
# Fast because they use hashing, allow us to access a value quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China' : 'Beijing',
            'Russia' : 'Moscow'}
            
print(capitals['Russia'])  # Print the capital of Russia using the key 'Russia'

# print(capitals['Germany'])  # The commented line above would raise a KeyError because 'Germany' is not in the dictionary

print(capitals.get('Germany'))  # Print None as 'Germany' is not in the dictionary, but no error is raised

print(capitals.keys())  # Print the keys of the dictionary capitals

print(capitals.values())  # Print the values of the dictionary capitals

print(capitals.items())  # Print the key:value pairs of the dictionary capitals

for key, value in capitals.items():
    print(key, value)  # Iterate through key:value pairs and print them

capitals.update({'Germany': 'Berlin'})  # Add a new key:value pair to the dictionary capitals

for key, value in capitals.items():
    print(key, value)

capitals.update({'USA': 'Las Vegas'})  # Update the value of an existing key in the dictionary capitals

for key, value in capitals.items():
    print(key, value)

capitals.pop('China')  # Remove the key 'China' and its corresponding value from the dictionary capitals

for key, value in capitals.items():
    print(key, value)
