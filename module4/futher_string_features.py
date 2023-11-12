av_band = 'Green Day'
print(fav_band[6])  # Print the character at index 6 of the string fav_band

fav_band = 'Green Day'
print(fav_band[:6])  # Print the substring from the start to index 5 (excluding) of the string fav_band

# print(fav_band[6] = 'M')
# The commented line above returns an error because strings are immutable in Python, so individual characters cannot be changed.

text = 'please capitalise me'
text_cap = text.upper()
print(text_cap)  # Convert the string text to uppercase and print it