# Given array A, create array B containing items from A
# in reversed order

# Simple solution
# a = [1,2,4,6,2]
# b = a[::-1]
# print(b)

# Hard mode solution
a = [2,5,7,1,3]
b = []

for i in range(len(a) - 1, -1, -1):
    b.append(a[i])

print(b)