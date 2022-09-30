# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
#    Напишите программу, которая определит индекс второго вхождения строки в списке
#    либо сообщит, что её нет.

from cgitb import reset
from random import choices

def fill_list (count, word):
    list = []
    for i in range(count):
        a = choices(word, k=3)
        list.append(''.join(a))
    return list

def search(list, key):
    if list.count(key) > 1:
        first_find = list.index(key)
        second_find = list.index(key, first_find+1)
        print(second_find)
    else:
        print('-1')

result = fill_list(15, 'abc')
print(result)
search(result, input())

