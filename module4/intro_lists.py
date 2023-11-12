for char in 'happy message':
    print(char)  # Iterate through each character in the string 'happy message' and print the current character

invited_guest = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name?  ')
if name in invited_guest:
    print('Welcome!')  # Print a welcome message if the entered name is in the invited_guest list
else:
    print('You are not invited!')  # Print a message if the entered name is not in the invited_guest list

# not in

invited_guest = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name?  ')
if name not in invited_guest:
    print('You are not invited!')  # Print a message if the entered name is not in the invited_guest list
else:
    print('Welcome!')  # Print a welcome message if the entered name is in the invited_guest list