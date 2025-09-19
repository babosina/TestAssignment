# Write code that calculates a running sum.
# A user will enter numbers that will be added to the sum and
# when a negative number is encountered,
# stop adding numbers ands write out the final result.

sum = 0
while True:
    a = int(input('Enter a number: '))
    if a < 0:
        break
    sum += a

print(sum)
