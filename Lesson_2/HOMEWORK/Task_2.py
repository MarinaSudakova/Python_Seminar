# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

number = int(input('Write a number: '))

factorial = [1]
for i in range(1, number+1):
    factorial.append(i*factorial[i-1])
    i+=1

print(f'{number} --> {factorial}')