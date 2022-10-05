# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов
#  исходной последовательности в том же порядке.

from random import choices

def fill_list(count):
    if count < 0:
        return 'Error'
    list_numbers = choices(range(1, 11), k=count)
    print(list_numbers)
    return list_numbers

def delete_copy(list):
    my_list = []
    for i in list:
        if list.count(i) == 1:
            my_list.append(i)
    print(my_list)
    return my_list

new_list = fill_list(int(input('Write size list: ')))
delete_copy(new_list)