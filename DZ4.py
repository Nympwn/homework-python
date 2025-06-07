def greet_and_count(name):
    print(f'Привет, {name}! Добро пожаловать!')

username = input('Введите имя пользователя:\n')

greet_and_count(username)

count = username.replace(' ', '')
print(f'В твоем имени {len(count)} символов (не считая пробелов).')