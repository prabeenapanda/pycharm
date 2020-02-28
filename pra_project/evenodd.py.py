from functions import input_int

num = input_int("Please enter a number to check even or odd: ")
print(f'{num} is even') if num % 2 == 0 else print(f'{num} is odd')


