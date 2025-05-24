'''
Циклы

Цикл for используется, когда известно количество повторений.
while <condition>
  <action>

for <item> in <sequence>
   <action>
'''
from itertools import count

# цикл while

i = 1
while i < 6:
    print(i)
    i += 1

n = 5
while n > 0:
    n -= 1
    print(n)
'''
Цикл while становится бесконечным, когда условие цикла никогда не становится ложным.
Пример бесконечного цикла (не запускать).

num = 1
while num < 10:
    print ('Бесконечный цикл')
'''

# Прерывание цикла while

i = 1
while 1 < 6:
    print(i)
    if i == 3:
        break
    i += 1

# break – прерывание цикла
# continue – прерывание итерации

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue # если i равно 3, то вывода значения не будет
    print(i)

# for используется, когда известно необходимо количество итераций.
# используется преимущественно для итерации по последовательности (list, tuple, dict и т. д.)

for x in 'banana':
    print(x)

word = 'Слово'
for letter in word:
    print(letter)

# for со словарем

seasons = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
for s in seasons:
    print(s == 1)

# range – применяется, чтобы выполнить действие заданное количество раз (начинает с 0)

for x in range(3):
    print(x)

'''
может использоваться для повторения фраз
равносильно for i in 0, 1, 2, 3

range(finish)
range (start, finish)
range (start, finish, step)
start – первый элемент последовательности (включительно)
finish – последний (не включительно)

Можно указать значение приращения, добавив третий параметр
range(2, 30, 3)
'''

for x in range (2, 30, 3):
    print(x)

# можно установить отрицательное число

for x in range (50, 44, -1):
    print(x)

'''
enumerate – считает, сколько цикл был запущен
может принимать не обязательный аргумент (по умолчанию 0)
'''

mylist = ['milk', 'eggs', 'breat']
for c, value in enumerate(mylist, 1):
    print(c, value)

for index, item in enumerate(['one', 'two', 'three']):
    print(index, '::', item)

'''
Вложенный цикл – цикл в цикле
Запускается при каждой итерации основного цикла 
'''

fruit = ['apple', 'pineapple', 'orange']
adj = ['yellow', 'sour', 'sweet']

for x in adj:
    for y in fruit:
        print(x, y)

mytext = 'Посчитаем количество символов с пробелами'
'''
С помощью цикла for посчитаем количество в строке
Зададим счетчик
'''
count = 0
'''
Будем посимвольно обходить текст
'''

for letter in mytext:
    count +=1

'''
На каждой новой итерации в переменной letter будет храниться следующий символ предложения
увеличиваем счетчик на один (строка 130)
Выводим значение
'''

print(count)

# Посчитаем количество слов в строке
s = 'Посчитаем количество слов в строке'
count = 0
flag = 0
for i in range(len(s)):
    if s[i] != ' ' and flag == 0:
        count += 1
        flag = 1
    else:
        if s[i] == ' ':
            flag = 0

print(count)