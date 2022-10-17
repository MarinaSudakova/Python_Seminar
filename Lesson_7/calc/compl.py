def init_complex():
    while True:
        a = (input("Введите действительную часть числа: "))
        b = (input("Введите мнимую часть числа: "))
        if not a.isdigit() or b.isdigit():
            print('Ошибка. Повторите ввод')
            continue
        a, b = int(a), int(b)
        break
    return complex(a, b)