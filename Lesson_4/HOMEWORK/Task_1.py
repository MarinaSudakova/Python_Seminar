 # Вычислить число c заданной точностью d

from decimal import Decimal, getcontext

def  accuracy (num: str, count: str):
    if len(count) < 3:
        print('Error')
        return
    number = Decimal(num)
    print(number.quantize(Decimal(count)))


accuracy(input('Enter a real number: '), input('Enter the required accuracy "0.0001": '))



# number = Decimal('9.3622939')
# print(number.quantize(Decimal('1.000')))


