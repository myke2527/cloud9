if __name__ == '__main__':
    n = int(input().strip() )  # Read an integer input and assign it to the variable 'n'
    if n % 2 != 0:
        print("Weird")  # Print "Weird" if n is odd
    elif n in range(2, 6):
        print("Not Weird")  # Print "Not Weird" if n is even and in the range [2, 6)
    elif n in range(6, 21):
        print("Weird")  # Print "Weird" if n is even and in the range [6, 21)
    elif n > 20:
        print("Not Weird")  # Print "Not Weird" if n is even and greater than 20