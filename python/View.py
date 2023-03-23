import Note

def create_note(comand):
    title = check_len_text_input(
        input('Введите заголовок заметки: '), comand)
    body = check_len_text_input(
        input('Введите тело заметки: '), comand)
    return Note.Note(title=title, body=body)


def menu():
    print("\nЭто программа 'Заметки'. Имеются следующие функции:\n\nall - вывод всех заметок из файла\nadd - добавление заметки\ndelete - удаление заметки\nedit - редактирование заметки\ndate - выборка заметок по дате\nid - показать заметку по id\nexit - выход\n\nВведите название функции: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def goodbye():
    print("exit")