# Напишите программу, удаляющую из текста все слова, 
# содержащие "абв". В тексте используется разделитель пробел.

from random import sample, choice

def list_words(count: int):
    if count < 1:
        print('Error')
    words = ''
    for i in range(count + 1):
        words += '{}{}'.format("".join(sample('абв', 3)), ' ')
    print(words)
    return words

def delete_word(word: str):
    new_word = [x for x in word.split() if x != 'абв']
    print(' '.join(new_word))

new_string = list_words(int(input('Write count of words: ')))
delete_word(new_string)

