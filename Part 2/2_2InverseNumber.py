# Given an integer, reverse its digits

a = input('Enter a number: ')

a = list(a)
b = []

# Hard solution
for i in range(len(a)-1, -1, -1):
    b.append(a[i])
b = ''.join(b)

print(b)