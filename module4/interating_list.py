top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
for city in top_cities:
    print('Current city', city)  # Iterate through each city in top_cities and print the current city

for city_index in range(len(top_cities)):
    print('Current index:', city_index, '| Current city:', top_cities[city_index])
    # Iterate through the indices and elements of top_cities and print the current index and city

spendings = [32.45, 18.65, 23.45, 78.32, 5.23]
sum = 0.0
for spending in spendings:
    sum += spending
print('Money spent:', sum)  # Calculate and print the sum of the spendings