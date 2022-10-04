# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def negafibo(number):
    fibonachi = [-1, 1, 0, 1, 1]
    for i in range(1, number+1):
        fibonachi.append(i + fibonachi[i+2])

    return fibonachi
   


a = int(input('Write a number: '))
print(f'{a} --> {negafibo(a)}')