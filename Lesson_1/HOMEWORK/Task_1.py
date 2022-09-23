# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

print('Write a number of day: ')
date = int(input())

if date >= 1 and date < 6:
    print("Working day")
elif date == 6 or date == 7:
        print('Weekend:)')
else:
    print("Error")

