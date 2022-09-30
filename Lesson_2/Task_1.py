# # 1. Напишите программу, которая принимает на вход 
# число N и выдаёт последовательность из N членов.

number = int(input('Write count: '))
m = 1
for i in range(number):
    print(m, end=' ')
    m *= -3

# или

number = int(input('Write count: '))
for i in range(number):
    print((-3)**i, end=' ')
