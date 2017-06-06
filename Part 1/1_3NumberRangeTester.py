""" Write pseudo code that performs the following:\
Ask a user to enter a number. 
If the number is between 0 including and 10 excluding, write the word blue. 
If the number is between 10 including and 20 excluding, write the word red. 
If the number is between 20 including and 30 excluding, write the word green. 
If it is any other number, write that it is not a correct color option
"""

a = int(input('Enter a number: '))

if 0 <= a < 10:
    print('blue')
elif 10 <= a < 20:
    print('red')
elif 20 <= a < 30:
    print('green')
else:
    print('It is not a correct number!')
