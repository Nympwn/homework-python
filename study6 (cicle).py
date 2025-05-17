'''
Циклы

Цикл for используется, когда известно количество повторений.
while <condition>
  <action>

for <item> in <sequence>
   <action>
'''

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

