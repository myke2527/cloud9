while True:
    name = input('Enter your name or type "EXIT" to exit the program: ')  # Prompt the user to enter their name or exit command
    if name.upper() == 'EXIT':
        break
    print('Hello', name)  # Greet the user by their entered name