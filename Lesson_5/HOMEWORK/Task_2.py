# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_code(name: str, name_2: str):
    if '.txt' not in name and '.txt' not in name_2:
        print('error')
        return ''
    with open(name, "r", encoding="utf-8") as my_f_1, \
        open(name_2, "a", encoding="utf-8") as my_f_2:
        data = my_f_1.readline()
        count = 1
        encoding = ''
        for i in range(1, len(data)):
            if data[i] == data[i - 1]:
                count += 1
            else:
                prev_char = data[i]
                encoding += str(count) + data[i - 1]
                count = 1
        encoding += str(count) + data[i]
        my_f_2.write(encoding)
        print(f'Check the file {name_2}')
        return ''


def rle_decode(name: str, name_2: str):
    if '.txt' not in name and '.txt' not in name_2:
        print('error')
        return ''
    with open(name, "r", encoding="utf-8") as my_f_1, \
        open(name_2, "a", encoding="utf-8") as my_f_2:
        data = my_f_1.readline()
        count = ''
        decoding = ''
        for char in data:
            if char.isdigit():
                count += char
            else:
                decoding += char * int(count)
                count = ''
        my_f_2.write(decoding)
        print(f'Check the file {name_2}')
        return ''


# to code take this block 
# print(rle_code(input('Enter the name of the file with the text as text_1.txt: '), \
#     input('Enter the file name to record as text_1.txt: ')))

# to decode take this block 
# print(rle_decode(input('Enter the name of the file with the code as text_1.txt: '), \
#     input('Enter the file name to record as text_1.txt: ')))
