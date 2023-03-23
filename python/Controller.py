import Function as f
import View as v


def run():
    input_from_user = ''
    while input_from_user != 'exit':
        v.menu()
        input_from_user = input().strip()
        if input_from_user == 'all':
            f.show('all')
        if input_from_user == 'add':
            f.add()
        if input_from_user == 'delete':
            f.show('all')
            f.id_edit_del_show('del')
        if input_from_user == 'edit':
            f.show('all')
            f.id_edit_del_show('edit')
        if input_from_user == 'date':
            f.show('date')
        if input_from_user == 'id':
            f.show('id')
            f.id_edit_del_show('show')
        if input_from_user == 'exit':
            v.goodbye()
            break