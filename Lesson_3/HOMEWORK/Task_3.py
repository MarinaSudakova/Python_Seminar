# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

def convert(number):
    list = []
    while number:
        list.append(number % 2)
        number //= 2
    list.reverse()
    print(''.join(map(str,list)))
    return

a = int(input('Write a number: '))
convert(a)