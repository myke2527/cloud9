# del delete items from list

top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']

print(top_cities)  # Print the original list of top_cities

del top_cities[2]
print(top_cities)  # Delete the item at index 2 and print the modified list

del top_cities[3:]
print(top_cities)  # Delete items from index 3 onwards and print the modified list

# del top_cities[:]
print(top_cities)  # Uncommenting this line would delete all items in the list and print an empty list