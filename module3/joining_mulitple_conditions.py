#Boolean Operators 
# and, or, not

#user_age = int(input('What is your age? '))
#user_country = input('What is your country? ')

#if user_age < 25 and user_country == 'Germany':
    #print("you can apple for a German student exchange program")
#else:
    #print("Sorry, you do not qualify")
    
#user_country = input ('What is your country')

#if user_country == 'Sweden' or user_country == 'Denmark' or user_country == 'Norway':
    #print('You can apple for a Scandinavian student exchange program')
#else:
    #print('Sorry, you do not qualify')
    
#user_country = input('Where do you come from? ')
#if not user_country == 'Germany':
    #print('You are not from Germany!')
#else:
    #print('You are from Germany!')
    

user_age = int(input('What is your age? '))  # Prompt the user to enter their age
user_country = input('What is your country? ')  # Prompt the user to enter their country

if ((not user_country == 'Germany') and user_age < 25) or \
   (user_country == 'Germany' and user_age < 23):
    print('You qualify')  # Print a message if the user qualifies
else:
    print('You don\'t qualify')  # Print a message if the user doesn't qualify