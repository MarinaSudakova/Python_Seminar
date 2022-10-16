# Функция принимает в качестве аргументов строки в формате «Имя Фамилия», 
# возвращает словарь, ключи — первые буквы фамилий, 
# значения — словари, реализованные по схеме предыдущего задания.

def dict_name(name_list: list):
    dict_of_names = {}
    dict_of_surnames = {}
    for name in sorted(name_list):
        first_letter = name[0]
        if first_letter not in dict_of_names:
            dict_of_names[first_letter] = [name]
        else:
            dict_of_names[first_letter].append(name)
    for full_name in name_list:
        surname = (name.split()[1])
        first_l = surname[0]
        if first_l not in dict_of_surnames:
            dict_of_surnames[first_l] = [name]
        else:
            dict_of_names[first_letter].append(name)
     
    return dict_of_surnames





# fio_list = ["Иван Сергеев", "Инна Серова", "Петр Алексеев",
# "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
# "Борис Аркадьев", "Антон Серов", "Павел Анисимов"]

# print(sorted(fio_list))
# a = "Иван Сергеев"
# print(a.split()[1])