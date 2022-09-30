# Напишите программу, которая принимает на вход 2 числа. 
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях(не индексах).

a = int(input('Write a number '))
pos_1 = int(input('Write a first position '))
pos_2 = int(input('Write a second position '))

list = []

if a > 0:
    for i in range(a*-1, a+1):
        list.append(i)
else:
    for i in range(a, a*-1+1):
        list.append(i)


if pos_1 <= len(list) and pos_2 <= len(list):
    print(list, list[pos_1-1] * list[pos_2-1], end=' ')
else:
    print('Not in list')
