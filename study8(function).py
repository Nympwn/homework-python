'''
Функции – это подпрограммы.
Подпрограммы:
– избавляют от повторяющихся кусков кода;
– улучшают структуру программы;
– распределение больших задач между разработчиками или стадиями проекта;
– повышает устойчивость к ошибкам и непредвиденным последствиям.

Процедуры – выполняют действия.
Функции – выполняют действия, возвращают некоторый результат.

В Python между данными видами нет разницы.

def – определитель.

def name_procedure(parametrs):
    body_procedure

Что отличает функцию от процедуры:
def name_function(parametrs):
    body_function
    return(result)

Глобальная переменная – переменные, введенные в основной программе.
Их могут использовать все подпрограммы.

Локальные – используются внутри процедуры или функции.
К ним обращение возможно только внутри программы, другие подпрограммы их не видят.
Называется инкапсуляцией.
Локальная создается только при вызове процедуры или функции.
Как только работа подпрограммы будет закончена, все локальные переменные удаляются из памяти.

'''
#
# def printline():
#     print('----------------')
#
# # параметры
#
# def printline(n):
#     print('=) '*n)
#
# n = int(input('n = '))
# printline(n)
#
# def printline(a, n):
#     print(a*n)
#
# a = str(input('a = '))
# n = int(input('n = '))
# print(a,n)
#
# # функции
#
# def Avg(a, b):
#     return (a+b)/2
#
# a = int(input('a = '))
# b = int(input('b = '))
# print(Avg(a, b))
# if Avg(a, b) > 5:
#     print('Yes!')
# else:
#     print('No!')
#
# def f():
#     global a
#     global b
#     b, c = a, b
# def g():
#     global a
#     global d
#     c = '0'
#     a = d + c
#
# a = '2'
# b = '3'
# c = '5'
# d = '7'
# f()
# g()
# f()
# print(a + b + c + d)
#
# # Рекурсия
#
# def F(n):
#     if n > 2:
#         return  F(n - 1) + F(n - 1)
#     else:
#         return 1
#
# n = int(input())
# print(F(n))
#
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# n = int(input('n = '))
# print(factorial(n))
#
# def F(n):
#     if n > 2:
#         return F(n - 1) + G(n - 2)
#     else:
#         return n
#
# def G(n):
#     if n > 2:
#         return G(n - 1) + F(n - 2)
#     else:
#         return n + 1
#
# print(F(4))

'''
Объявление класса
'''

# class name_class():
#     variable = meaning
'''
    variable – переменная
    meaning – значение 
'''

'''
Объявление метода
'''

# def name_methode(self, ...):
#     self.variable = meaning
'''
    self – применяется сам к себе
'''

'''
Создание объекта
'''

# variable = name_class()

'''
Вызов метода
'''

# objects.name_methode()

'''
Атрибуты класса – имена переменных вне функций и имена функций.
Наследуются всеми объектами, созданными на основе данного класса.
'''

'''
Конструктор класса "__init__" автоматически создает атрибуты объекта при вызове класса
Конструктор ___Str__ возвращает строку
'''

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'{self.name} | Number: {self.phone} | E-mail: {self.email}'

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f'Контакт "{contact.name}" добавлен')

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f'Контакт "{name}" удален.')
                return
        print(f'Контакт с именем "{name}" не найден.')

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f'Контакт найден: ')
                print(contact)
                return
            print(f'Контакт с именем "{name}" не найден.')

    def show_contact(self):
        print("\nВаш список контактов:")
        for contact in self.contacts:
            print(contact)
        if not self.contacts:
            print('Список контактов пуст. Добавьте контакт.')

def main():
    manager = ContactManager
    while True:
        print('\n-- Menu --')
        print('1. Add contact.')
        print('2. Remove contact.')
        print('3. Find contact.')
        print('4. Show all contacts.')
        print('5. Exit.')

        choice = input('Select an item from the menu (1 - 5):\n')
        if choice == '1':
            name = input('Name: \n')
            phone = input('Phone: \n')
            email = input('E-mail: \n')
            manager.add_contact(Contact(name, phone, email))

        elif choice == '2':
            name = input('Name contact for remove:\n')
            manager.remove_contact(name)

        elif choice == '3':
            name = input('Name contact for search:\n')
            manager.search_contact(name)

        elif choice == '4':
            manager.show_contact()

        elif choice == '5':
            print('Exit.')
            break

        else:
            print('Not Incorrect choice in the menu.')

main()