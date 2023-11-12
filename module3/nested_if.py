answer_a = input('Do you like traveling? y/n:')  # Prompt the user to answer whether they like traveling
if answer_a == 'y':
    print('Good!')  # Print a positive message if the answer is 'y'
else:
    print('Sorry to hear that!')  # Print a message if the answer is not 'y'

# Nested If statement
answer_a = input('Do you like traveling? y/n:')  # Prompt the user to answer whether they like traveling
if answer_a == 'y':
    answer_b = input('And do you like Asia? y/n ')  # Nested prompt about liking Asia
    if answer_b == 'y':
        print('Excellent! You can win a ticket to Thailand!')  # Print a message if both answers are 'y'
else:
    print('Sorry to hear that!')  # Print a message if the initial answer is not 'y'
