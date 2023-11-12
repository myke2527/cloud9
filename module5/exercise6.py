while True:
    answer = int(input('When was Python 1.0 released?'))  # Prompt the user to input the release year of Python 1.0 and convert it to an integer
    if answer > 1994:
        print('It was earlier than that!')  # Print a message if the entered year is later than 1994
    elif answer < 1994:
        print('It was later than that!')  # Print a message if the entered year is earlier than 1994
    else:
        print('Correct!')  # Print a message if the entered year is correct (1994) and break out of the loop
        break