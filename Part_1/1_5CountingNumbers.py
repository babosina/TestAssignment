# Write code that will count all the even numbers up to (and including) a user defined stopping point

# start = int(input('Enter a start point: '))
stop = int(input('Enter a stopping point: '))

# starts from 0
for num in range(0, stop + 1):
    if num % 2 == 0:
        print(num, end=' ')

# starts from user defined point
# for num in range(start, stop + 1):
#     if num % 2 == 0:
#         print(num, end=' ')
