import write

def convert(name: str):
    with open(name, "r", encoding="utf-8") as file:
        for i in file:
            surname, name, phone, enough = i.split()
            print('Перенесено', surname, name, phone, enough)
            write.init_surname(surname)
            write.init_name(name)
            write.init_phone(phone)
            write.init_enough(enough)
            write.write_from()
            
