# Write code that performs the following:
# Read in 5 separate numbers.
# Calculate the average of the five numbers.
# Find the smallest (minimum) and largest (maximum) of the five entered numbers.
# Write out the results found from steps 2 and 3 with a message describing what they are.

i = 5
mas = []
sum = 0
while i != 0:
    a = int(input('Enter a number: '))
    mas.append(a)
    i -= 1

for i in mas:
    sum += i

avg = sum / 5
minimum = min(mas)
maximum = max(mas)

print('The avarage of the 5 numbers is {}, the minimum is {}, tha maimum is {}'.format(avg, minimum, maximum))
