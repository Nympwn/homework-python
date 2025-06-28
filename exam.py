# Task 1

a = float(input('Введите первое число:\n'))
b = float(input('Введите второе число:\n'))
operacion = input('Выберите действие, которое нужно выполнить:\n'
                  '1. сложение (+)\n'
                  '2. вычитание (-)\n'
                  '3. деление (/)\n'
                  '4. умножения (*)\n').lower()

if operacion == '1' or operacion == '+' or operacion == 'сложение':
    print(f'Сложение: {a} + {b} = {round(a + b, 2)}')
elif operacion == '2' or operacion == 'вычитание' or operacion == '-':
    print(f'Вычитание: {a} - {b} = {round(a - b, 2)}')
elif operacion == '3' or operacion == 'деление' or operacion == '/':
    print(f'Деление: {a} / {b} = {round(a / b, 2)}')
elif operacion == '4' or operacion == 'умножение' or operacion == '*':
    print(f'Умножение: {a} * {b} = {round(a * b, 2)}')
else:
    print('Выбран неверный пункт.')

# Task 4

date = input('Введите дату в формате ДД.ММ.ГГГГ:\n')
date_ex = date.replace('.', '')
if date_ex == date_ex[::-1]:
    print(f'Дата {date} является палиндромом.')
else:
    print(f'Дата {date} не является палиндромом. ')