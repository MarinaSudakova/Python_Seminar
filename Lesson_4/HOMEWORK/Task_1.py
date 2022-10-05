from time import time

start = time()


def primfacs(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(n)
    return primfac


print(primfacs(999999999990))
print(time() - start)

# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

start = time()
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 73, 101, 137, 21649, 513239]


def factors(num, prime_numbers):
    if num in prime_numbers: # сразу проверяет простое ли число
        print(f'{num} is prime')
        return
    list_factors = []
    for j in prime_numbers: # находим первый простой множитель и записываемв список
        if num > j and num % j == 0:
            list_factors.append(j)
            list_factors.append(num // j)
            break
    for c in range(10): # работаем с полученным списком, где каждое состаное число разделяем и удаляем его из списка
        if c < len(list_factors):
            for i in range(len(prime_numbers)):
                if list_factors[c] > prime_numbers[i] and list_factors[c] % prime_numbers[i] == 0:
                    list_factors.append(prime_numbers[i])
                    list_factors.append(list_factors[c] // prime_numbers[i])
                    del list_factors[c]
        else:
            break
            
                
    return list_factors

print(factors(999999999990, prime_numbers))
print(time() - start)