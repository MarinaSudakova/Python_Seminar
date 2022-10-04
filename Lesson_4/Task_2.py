# 1. Задайте строку из набора чисел. Напишите программу,
#    которая покажет большее и меньшее число.
#    В качестве символа-разделителя используйте пробел.

line = input()
list_1 = [int(x.strip(',.*:;')) for x in line.split() if x.isdigit()]
print(f'Min: {min(list_1)}')
print(f'Max: {max(list_1)}')