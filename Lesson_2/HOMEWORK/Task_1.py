# Напишите программу, которая принимает на 
# вход вещественное число и показывает сумму его цифр.

number = float(input('Write a number: '))

number = number * 10 ** len(str(number))

sum = 0
number = int(number)

while number >= 1:
    sum += number % 10
    number //= 10

print(sum)