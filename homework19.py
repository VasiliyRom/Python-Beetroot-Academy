import json
import sys
from typing import Union, Tuple, List, Dict, Iterable, Iterator, Any, Optional
'''print(sys.argv)
if len(sys.argv) < 2:
    print('Будь ласка виберіть json файл')
    exit()
filename = sys.argv[1]
json_file = open(filename)
try:
    phonebook = json.load(json_file)
except json.decoder.JSONDecodeError:
    print('Невдається прочитати JSON файл!')
    phonebook = []
json_file.close() '''

json_file = open('phonebook.json')
try:
    phonebook = json.load(json_file)
except json.decoder.JSONDecodeError:
    print('Невдається прочитати JSON файл!')
    phonebook = []
json_file.close()


def new_contact(first_name: str, last_name: str, number: str,
                city: str) -> Dict[str, str]:
    user_info = {
        "first_name": first_name,
        "last_name": last_name,
        "full_name": first_name + " " + last_name,
        "number": number,
        "city": city
    }

    app(user_info, phonebook)
    return user_info


def app(user_info, phonebook):
    phonebook.append(user_info)


def remove(item):
    phonebook.remove(item)


def search_con(query: str, arg, phonebook) -> None:
    for item in phonebook:
        if query == item[arg]:
            print('\nІм\'я: ' + str(item['first_name']))
            print('Прізвище: ' + str(item['last_name']))
            print('Повне iм\'я: ' + str(item['full_name']))
            print('Номер тел: ' + str(item['number']))
            print('Місто: ' + str(item['city'] + '\n'))
        else:
            print('Запису неіснує!')
    return item


try:
    while True:
        print('''
        Додати запис_____________________________(1)
        Пошук____________________________________(2)
        Видаліть запис для номера телефону_______(3)
        Оновіть запис для номеру телефону________(4)
        Вийти з програми_________________________(exit, q)\n''')

        operator: str = input('Головне меню: ').strip().lower()

        if operator == '1':
            first_name: str = input('Введіть ім\'я: ').strip().capitalize()
            last_name: str = input('Введіть Прізвище: ').strip().capitalize()
            number_alp: str = input('Введіть номер тел: ').strip()
            while True:
                if number_alp.isdigit():
                    number = number_alp
                    break
                else:
                    print('Номер має містити тільки цифри!')
                    number_alp = input('Введіть номер тел: ').strip()

            city: str = input('Введіть місто: ').strip().capitalize()

            new_contact(first_name, last_name, number, city)

        elif operator == '2':
            print('''Пошук за імені___________________________(1)
    Пошук за прізвищу________________________(2)
    Пошук за повним іменем___________________(3)
    Пошук за номером телефону________________(4)
    Пошук по місту___________________________(5)
    Назад в головне меню_____________________(6)\n''')
            search: str = input('Пошук: ')
            if search == '1':
                query: str = input('Введіть ім\'я: ').strip().capitalize()
                atr = 'first_name'
                search_con(query, atr, phonebook)

            elif search == '2':
                query = input('Введіть прізвище: ').strip().capitalize()
                atr = 'last_name'
                search_con(query, atr, phonebook)
            elif search == '3':
                query = input('Введіть повне ім\'я: ').capitalize()
                atr = 'full_name'
                search_con(query, atr, phonebook)
            elif search == '4':
                query = input('Введіть номер телефону: ').strip()
                if query.isalpha():
                    print('Номер має містити тільки цифри!')
                else:
                    atr = 'number'
                    search_con(query, atr, phonebook)
            elif search == '5':
                query = input('Введіть місто: ').strip().capitalize()
                atr = 'city'
                search_con(query, atr, phonebook)
            elif search == '6':
                continue
        elif operator == '3':
            query = input('Введіть номер телефону: ').strip()
            for item in phonebook:
                if query in item['number']:
                    print('''Ви дійсно бажаєте видалити дані?
    Так - 1
    Ні - 2 \n''')
                    question: str = input('Ваш вибір: ')
                    if question == '1':
                        remove(item)
                        break
                else:
                    print('Номеру телефону неіснує!')
                    break

        elif operator == '4':
            query = input('Введіть номер телефону: ').strip()
            for item in phonebook:
                if query == item['number']:
                    print('''Ви дійсно бажаєте оновити дані?
    Так - 1
    Ні - 2 \n''')
                    question = input('Ваш вибір: ')
                    if question == '1':
                        first_name = input(
                            'Введіть ім\'я: ').strip().capitalize()
                        last_name = input(
                            'Введіть Прізвище: ').strip().capitalize()
                        full_name = (f'{first_name} {last_name}')
                        number = query.strip()
                        city = input('Введіть місто: ').strip().capitalize()
                        new_contact(first_name, last_name, number, city)
                        remove(item)
                else:
                    print('Номеру телефону неіснує!')
                    break

        elif operator == 'exit' or operator == 'q':
            print('До побачення!')
            break
except Exception as e:
    print('Unexpected error.')
    print(e)
finally:
    with open('phonebook.json', 'w') as filee:
        json.dump(phonebook, filee, indent=4, ensure_ascii=False)
        print('Збережено!')