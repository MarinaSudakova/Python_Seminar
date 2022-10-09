
# 2. Дан список чисел. Создайте список, в который попадают числа, #    
# описываемые возрастающую последовательность. 
#     Порядок элементов менять нельзя.

from random import choices

def fill_list(count: int):
    my_list = choices(range(1, count * 2), k = count)
    return my_list

c = fill_list(10)
print(c)

def range_nums(new_list: list):
    range_list = []
    for i in range(len(new_list)):
        f = new_list[i]
        list_new =[f]
        for g in range(i + 1, len(new_list)):
            if new_list[g] > f:
                f = new_list[g]
                list_new.append(f)
        if len(list_new) > 1:
            range_list.append(list_new)
    return range_list


print(range_nums(c))