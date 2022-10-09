# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.



def rle_code(data: str):
    count = 1
    encoding = ''
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            prev_char = data[i]
            encoding += str(count) + data[i - 1]
            # print(count, data[i - 1])
            count = 1
    encoding += str(count) + data[i]
    return encoding

print(rle_code(string))