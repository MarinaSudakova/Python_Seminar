# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, 
# записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

from random import choice, randint

def equation (degree: int):
    if degree < 1:
        print('Error')
    my_list = range(degree, 1, -1)
    with open ('Equation1.txt', 'a', encoding='utf-8') as my_f:
        for i in my_list:
            r = randint(0, 10)
            ch = choice('+-')
            if r == 0:
                continue
            my_f.write(f'{r}*x^{i} {ch} ')
        my_f.write(f'{r} = 0\n')

for i in range(3):
    equation(int(input("Write a degree: ")))
    print()