# Write code to print all multiples of 5 between 1 and 100 (including both 1 and 100)

for num in range(1,101):
    if num % 5 == 0:
        print(num, end=' ')
