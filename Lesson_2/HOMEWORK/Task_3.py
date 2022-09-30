# Задайте список из n чисел, заполненный по формуле 
# (1 + 1/n) ** n и выведите на экран их сумму.

number = int(input('Write a number: '))
list = []
sum = 0

for i in range(1, number+1):
    list.append(round((1+1/i)**i))

for num in list:
    sum += num

print(f'{list} --> {sum}')