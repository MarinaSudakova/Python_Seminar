# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.

from random import uniform

def fill_list(count):
    if count <= 0:
        print('Error')
    numbers = []
    for i in range(count):
        numbers.append(round(uniform(0, 20), 2))
    return numbers

def min_max(numbers):
    min = 1
    max = 0
    for find in numbers:
        if find % 1 > max:
            max = round(find % 1, 2)
        elif find % 1 < min:
            min = round(find % 1, 2)
    print(f'Maximum is {max}, minimum is {min}, difference is {max-min}')

a = int(input('Write count of elements: '))
my_list = fill_list(a)
print(my_list)

min_max(my_list)