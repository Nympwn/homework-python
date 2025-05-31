'''
Строка – неизменяемый тип данных
Может быть только перезаписана
'''
from dataclasses import replace

my_num = 123
my_str = str(my_num)
print(my_str)

'''
Операции над строками
Общие: 
x in s 
s[i]
s[i, j] – вывод диапазона символов i <= k < j
min(s)
s.count(x) – найти количество символов в строке x
s + t – "склеивание" символов
s * n – повторение несколько раз (n)
len(s) – длина последовательности (списка)
s.index(x) – возвращает индекс подстроки (какое место занимает в списке от 0)

Дополнительные:
s.capitalize – переводит первую букву в заглавную
s.title – первые буквы становятся заглавными в каждом слове
s.upper – все буквы становятся заглавными
s.lower – все буквы становятся строчными
s.swapcase – замена регистра (меняются зеркально)
s.isupper – true, если все буквы во фразе заглавные, false в других случаях
s.islower – true, если все буквы во фразе строчные, false в других случаях
s.istitle – true, если каждое слово начинается с заглавной буквы, false в других случаях
s.find(sub) – находит в строке s подстроку sub, возвращает индекс первого значения.
Если подстрока не найдена, индекс будет -1. Регистрозависим. 
Считает индекс букв, не слов.
s.replaсe(old, new) – заменяет строки old на new, регистрозависим
s.split – разбивает строку на части, используя разделитель (по умолчанию разделитель пробел)
s.startswith(x) – возвращает true, если начинается с префикса (x)
s.endwish(x) – возвращает true, если заканчивается с префикса (x)
Обе команды регистрозависимы

s.join(iterable) – возвращает строку, поддерживающую итерирование, вставляется между строками (словами, предложениями)
s.partision(x) – принимает какой-то разделитель в качестве аргумента, ищет первый разделитель и делит строку на три части 
Первая часть – до разделителя
Вторая часть – разделитель
Третья часть – после разделителя
Возвращает кортеж из трех элементов
'''

a = [1, 2, 3, 5, 7, -7, 3]
print(a.index(7))
print(a.count(3))

string = 'Hello world'
print(string.count('o'))

string = 'hello World, How are You?'
print(string.capitalize())
print(string.title())
print(string.upper())
print(string.lower())
print(string.swapcase())
print(string.islower())
print(string.isupper())

print(' - '.join(['Apple', 'Pear']))

words = ['Hello', 'world']
result = ' '.join(words)
print(result)

nums = [1, 2, 3]
print('-'.join(map(str, nums)))
# map – применяет указанную функцию ко всем элементам

print([str(x) for x in nums])
print(string.split(', '))
print(string.partition(', '))
print(string.startswith('hello World'))
print(string.endswith('are you?'))

print(string.find('hello'))
print(string.find('World'))
print(string.find('r'))
print(string.find('r', 5)) # можно задать поиск с определенного индекса (5)
print(string.find('o', 8, 23)) # можно задать интервал индексов для поиска (8-23)

print(string.replace('World', 'Portugal'))
print('Hello world, goodbye world'.replace('world', 'Portugal'))
print('Hello World, goodbye world'.replace('world', 'Portugal'))