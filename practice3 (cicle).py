# Task 1

for x in range(1, 51):
    if x % 2 == 0:
        print(x)

# Task 2

print(sum(range(1, 101)))

# alternative
x = 0
for y in range(1, 101):
    x += y
print(x)

# Task 3

num = int(input('Введите натуральное число:\n'))
flag = True

if num < 2:
    flag = False
else:
    for x in range(2, num):
        if num % x == 0:
            flag = False
            break


if flag:
    print('Число простое.')
else:
    print('Число не простое.')

# Task 4

num = int(input('Введите натуральное число:\n'))
y = 1
for x in range(1, num + 1):
    y *= x
print(y)

# Task 5
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# там же было про вывод, а не про расчет?

# fibonachi = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# for index, x in enumerate(fibonachi, 1):
#     print(index, '–', x)

# альтернатива
a, b = 0, 1
for _ in range(10):
    print(a)
    a, b = b, a + b

# Task 6

for x in range(10, 0, -1):
    print(x)

# Task 7

phrase = input('Введите фразу:\n')
# присвоение букв к единому регистру (нижнему)
# тогда не придется перечислять заглавные и строчные буквы
# phrase = phrase.lower()
# присвоение букв к единому регистру (верхнему)
# phrase = phrase.upper()
count = 0
letter = ['а', 'я', 'и', 'у', 'е', 'э', 'о', 'ы', 'ё', 'ю',
          'А', 'Я', 'И', 'У', 'Е', 'Э', 'O', 'Ё', 'Ю']
sets = set(letter)
for letters in phrase:
    if letters in sets:
        count += 1
print(count)

# Task 8

# num = int(input('Введите число:\n'))
# if 1000 > num > 100:
#     num1 = num % 10
#     num2 = num // 100
#     num3 = num % 100 // 10
#     mult = num1 + num2 + num3
#     print(mult)
# elif num > 10:
#     num1 = num % 10
#     num2 = num // 10
#     mult = num1 + num2
#     print(mult)
# else:
#     print('Число меньше десяти или больше тысячи')
# в задаче не стоит определенное условие, но без циклов вижу так
# иначе это будет бесконечное условие elif
# надо как-то оформить в циклах...

# циклы?
num = input('Введите число:\n')
total = 0
for digit in num:
    total += int(digit)
print(f'Сумма чисел: {total}')

# Task 9

for x in range(1, 11):
    for y in range(1, 11):
        print(f'{x} * {y} = {x * y}')
    print()

# Task 10

num = [-14, -6, -3, -1, 0, 1, 2, 5, 8, 10]
result = []
for x in num:
    if abs(x) > 5:
        result.append(x)

print(result)


# alternative
num = [-14, -6, -3, -1, 0, 1, 2, 5, 8, 10]
result = [x for x in num if abs(x) >5]
print(result)

# Task 11

letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'

for letter in letters:
    if letters.upper() == letters:
        letters.replace(letter, '')

print(letters.lower())

'''
Из задачи не совсем ясно, должны быть удалены буквы или переведены в строчные
Выше перевод в строчные, но цикл тут не особо нужен тогда
Ниже альтернатива с удалением
'''

letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
res = ''

for letter in letters:
    if letter.islower():
        res += letter

print(res)

# Task 12

nickname_friends = ('Мавпродош', 'Лорнектиф', 'Древерол', 'Фиригарпиг', 'Клодобродыч')

while True:
    nickname = input('Укажи свой ник:\n')
    if nickname in nickname_friends:
        print(f'Ты – свой. Приветствую, любезный {nickname}!')
        break
    else:
        print('Тут ничего нет. Еще есть вопросы?')

# Task 13

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэуя'

for position in range(11):
    print('^' * 27)
    for letter in alphabet:
        if alphabet.index(letter) % 11 == position:
            print(f"|  {letter.upper()} {letter}  |", end='')
    print()
print('^' * 27)


# для сравнения

print('^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('|  А а  ||  К к  ||  Х х  |')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('|  Б б  ||  Л л  ||  Ц ц  |')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('|  В в  ||  М м  ||  Ч ч  |')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('|  Г г  ||  Н н  ||  Ш ш  |')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('|  Д д  ||  О о  ||  Щ щ  |')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('|  Е е  ||  П п  ||  Ъ ъ  |')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('|  Ё ё  ||  Р р  ||  Ы ы  |')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('|  Ж ж  ||  С с  ||  Ь ь  |')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('|  З з  ||  Т т  ||  Э э  |')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('|  И и  ||  У у  ||  Ю ю  |')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('|  Й й  ||  Ф ф  ||  Я я  |')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^')

# Task 14