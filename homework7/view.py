
commands = ['Открыть файл', 
            'Сохранить файл', 
            'Показать все контакты', 
            'Создать контакт', 
            'Удалить контакт', 
            'Изменить контакт', 
            'Найти контакт', 
            'Выход из программы']


def main_menu():
    print('Главное меню:')
    for i, item in enumerate(commands, 1):
        print(F'\t{i}. {item}')
    while True:
        try:
            choice = int(input('Выберите пункт меню: '))
            if 0 < choice < 9:
                return choice
            else:
                print('Введите число от 1 до 8')
        except ValueError:
            print('Введите число от 1 до 8')

def show_contacts(phone_list: list):
    if len(phone_list) <1:
        print('Тел.книга пуста или не открыта')
    else:
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}. {contact[0]:27} {contact[1]:13} {contact[2]:20}')



def input_error():
    print('Некорректный ввод. Введите корректный пункт меню. ')

def empry_request():
    print('Контакт не найден.')

def many_request():
    print('Введите более точные данные. Найдено более одного контакта.')



def create_new_contact():
    name = input('Введите ФИО: ')
    phone = input('Введите номер: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment

def find_contact():
    find = input('Введите искомый эллемент: ')
    return find

def select_contact(massege: str):
    contact = input(massege)
    return contact

def change_contact():
    print('Введите новые данные. Если изменения не требуются, нажмите Enter')
    name = input('Введите ФИО: ')
    phone = input('Введите номер: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment


def delete_confirm(contact: str):
    result =input(f'Вы действительно хотите удалить контакт {contact}? (y/n)').lower()
    if result == 'y':
        return True
    else:
        return False