# Задание No2
# В Урок No10. Задание No1 вы создавали словарь с информацией о питомце.
# Теперь нам нужна 'настоящая' база данных для ветеринарной клиники.
# Подробный требуемый функционал будет ниже. Пока что справка:
#
# Создайте функцию create
# Создайте функцию read
# Создайте функцию update
# Создайте функцию delete
# Используйте словарь pets, который будет предоставлен ниже, либо
# создайте свой аналогичный
# Функция create:
# Данная функция будет создавать новую запись с информацией о питомце и
# добавлять эту информацию в наш словарь pets
# Функция read
# Данная функция будет отображать информацию о запрашиваемом питомце в
# виде:
# Это желторотый питон по кличке 'Каа'. Возраст питомца: 19 лет. Имя владельца:
# Саша
# Функция update
# Данная функция будет обновлять информацию об указанном питомцеФункция delete
# Данная функция будет удалять запись о существующем питомце
# Структура результирующего словаря pets будет как и в Урок No10. Задание No1,
# но с небольшим видоизменением:
# Словарь pets
# pets = {
# 1:
# {
# 'Мухтар': {
# 'Вид питомца': 'Собака',
# 'Возраст питомца': 9,
# 'Имя владельца': 'Павел'
# },
# },
# 2:
# {
# 'Каа': {
# 'Вид питомца': 'желторотый питон',
# 'Возраст питомца': 19,
# 'Имя владельца': 'Саша'
# },
# },
# # и так далее
# }
# Здесь, 1 и 2 - это идентификаторы наших питомцев. Это уникальные ключи, по
# которым мы сможем обращаться к нашим записям в 'базе данных'
# Суть будущей программы будет заключаться в следующем:
# ● Программа будет работать с помощью цикла while с условием command
# != 'stop', то есть до тех пор, пока на предложение ввести команду,
# пользователь не введёт слово stop● Перед взаимодействием с 'базой данных' запрашивается одна из
# команд в качестве пользовательского ввода. Пусть это будет
# переменная command
# ● Функция create должна добавлять новую информацию таким образом,
# чтобы идентификатор увеличивался на единицу. Чтобы у вас была
# возможность получать последний ключ в словаре воспользуйтесь
# импортом модуля collections. В начале вашей программы пропишите
# строчку: import collection, а в функции create в первых строках пропишите
# следующий код:
# def create():
# last = collections.deque(pets, maxlen=1)[0]
# last в данном случае и будет число последнего ключа (или в нашей
# логике - идентификатора записи). Именно его и необходимо будет
# увеличивать на единицу при добавлении следующей записи.
# Как вам уже известно - суть функций заключается в том, чтобы использовать
# один и тот же код в нескольких местах. В данной задаче вам предстоит
# получать информацию о питомце несколько раз. Чтобы не повторяться в коде,
# вам нужно создать такие функции
# get_pet(ID):
# def get_pet(ID):
# # функция, с помощью которой вы получите информацию о питомце в виде
# словаря
# # сделайте проверку, если питомца с таким ID нету в нашей 'базе данных'
# # верните в этом случае False
# # а если питомец всё же есть в 'базе данных' - верните информацию о нём
# # выглядеть это может примерно так:
# return pets[ID] if ID in pets.keys() else False
# get_suffix(age):
# def get_suffix(age):
# # функция, с помощью которой можно получить суффикс
# # 'год', 'года', 'лет'
# # реализацию этой функции вам предстоит придумать самостоятельно
# # функция будет возвращать соответствующую строку
# return pets_list():
# def pets_list():
# # Эта функция будет создана для удобства отображения всего списка питомцев
# # Информацию по каждому питомцу можно вывести с помощью цикла for
# Обратите внимание, если ID не существует в словаре с питомцами - будет
# возникать ошибка. Вам можно от неё избавиться, если правильно составить
# проверочное условие. Здесь не потребуется использовать такие конструкции,
# как try, except, чтобы обработать возникшую ошибку
#
# https://github.com/A-l-E-v/PySynergy/blob/main/U-11/petsDB.py
#

import collections
from collections import deque #для проверки пустого словаря


# дефолтный словарь питомцев

pets = {
1:
{
'Мухтар': {
'Вид питомца': 'собака',
'Возраст питомца': 9,
'Имя владельца': 'Павел'
},
},
2:
{
'Каа': {
'Вид питомца': 'желторотый питон',
'Возраст питомца': 19,
'Имя владельца': 'Саша'
},
},
}

def list():
# узнаём размер словаря
    pets_length = len(pets)
# проходимся по каждому если есть, если нет, то переходим на ввод первого
    if (pets_length):
        for pet_id in pets:
            pet = get_pet(pet_id)
            if pet:
                pet_name = [k for k in pet.keys()][0]
                age = pet[pet_name]['Возраст питомца']
                print (f'Это {pet[pet_name]['Вид питомца']} по кличке "{pet_name}". \
Возраст питомца: {age} {get_suffix(age)}. \
Имя владельца: {pet[pet_name]['Имя владельца']}')
    else: 
        print ('БД пуста! Создайте первую запись!')
    return

# функция постановки год(а)/лет
def get_suffix(age):
    if age % 10 == 1 and age != 11 and age % 100 != 11: return 'год'
    elif 1 < age % 10 <= 4 and age != 12 and age != 13 and age != 14: return 'года'
    else: return 'лет'


# функция получения информации по ID питомца
def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False
    


# функция создания записи
def create():

    # по умолчанию увеличиваем ID на единицу от последнего 
    last_pet = last()
    last_pet += 1

    pet_name = input ('Введите имя питомца: ')

    # словарь одного питомца
    a_pet =  {pet_name: dict()}

    a_pet [pet_name]['Вид питомца'] = input ('Введите вид питомца: ')
    a_pet [pet_name]['Возраст питомца'] = int(input ('Введите возраст питомца: '))
    a_pet [pet_name]['Имя владельца'] = input ('Введите имя владельца: ')
    
    # добавляем в словарь нового питомца
    pets[last_pet]=a_pet

    print ('Питомец добавлен!')


# функция чтения записи по ID
def read():
    info()
    pet_id=int(input('Введите ID записи: '))
    pet = get_pet(pet_id)
    print()

    if (pet):
        pet_name = [k for k in pet.keys()][0]
        age = pet[pet_name]['Возраст питомца']
        print (f'Это {pet[pet_name]['Вид питомца']} по кличке "{pet_name}". \
Возраст питомца: {age} {get_suffix(age)}. \
Имя владельца: {pet[pet_name]['Имя владельца']}')
    else:
        print('Питомца с таким ID нет в БД!')
        info()
    

# функция обновления записи по ID
def update():
    info()
    id = int(input('Введите ID питомца для обновления: '))
    if (get_pet(id)):
        pet_name = input ('Введите имя питомца: ')

        # словарь одного питомца
        a_pet =  {pet_name: dict()}

        a_pet [pet_name]['Вид питомца'] = input ('Введите вид питомца: ')
        a_pet [pet_name]['Возраст питомца'] = int(input ('Введите возраст питомца: '))
        a_pet [pet_name]['Имя владельца'] = input ('Введите имя владельца: ')
        
        # добавляем в словарь нового питомца
        pets[id]=a_pet

        print (f'Питомец {id} обновлён!')

    else:
        print ('Такой ID в БД не используется')

# функция удаления записи по ID
def delete():
    info()
    pets_length = len(pets)
    # если есть записи в словаре
    if (pets_length):
        id_allowed = True
        while (id_allowed):
            id = int (input('Введите ID для удаления: '))
            # if id <= last_pet:id_allowed=False
            if (get_pet(id)):id_allowed=False
            else:
                print ('Записи с таким ID не существует.')
        # print ('ДО:',pets)
        del pets[id]
        print()
        # print ('ПОСЛЕ:',pets)
        print (f'Запись под номером {id} была удалена.')
        info()
        print()
    # иначе создаём запись
    else: create()

# функция информации о БД
def info():
# запрашиваем длину словаря
    pets_length = len(pets)
    if (pets_length):
        print (f'Количество записей в БД: {pets_length}')
        print ('Использующиеся ID: ', end='')
        for k in pets.keys():
            print (f'{k} ', end='')
        print()
    else:
        print ('БД пуста! Создайте первую запись!')


# функция получения последней записи в словарь или false, если пусто
def last():
    if bool(deque(pets)):
        records = collections.deque(pets, maxlen=1)[0]
        return records
    else:
        return False


# ------ main () --------

print()
print('--- База данных питомцев ---')
print()

# инициализируем пустую переменную команд
command = ''

# диспетчер команд
while command != 'stop':
    print()
    print ('Введите одну из команд (create, read, update, delete, info или list)')
    command = input('Или stop для выхода: ')
    if command == 'create' : create()
    elif command == 'read' : read()
    elif command == 'update' : update()
    elif command == 'delete' : delete()
    elif command == 'info' : info()
    elif command == 'list' : list()
    elif command != 'stop': print('Нет такой команды!')
    print()