# Write code that reads in three numbers and writes all in ascending sorted order

i = 3
mas = []
while i != 0:
    a = int(input('Enter a number: '))
    mas.append(a)
    i -= 1

# Bubble sorting
for i in range(len(mas)-1):
    if mas[i] > mas[i+1]:
        mas[i], mas[i+1] = mas[i+1], mas[i]

print(mas)