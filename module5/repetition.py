import random 

number = random.randint(1, 10)

counter = 0
while number != 7:
    number = random.randint(1,10)
    counter += 1
    if counter > 12:
        break
   
    print(counter,number)