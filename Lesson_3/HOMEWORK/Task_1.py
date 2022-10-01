# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётных позициях(не индексах).

from random import sample

def sum_elements(count):
    if count <= 0:
        print('Error')
    sum = 0
    ind = 0
    list_numbers = sample(range(1, count * 2), count)
    print(list_numbers)
    while ind < count:
        sum += list_numbers[ind]
        ind += 2
    print(f'Sum of elements is {sum}')

a = int(input('Write count of elements: '))
sum_elements(a)