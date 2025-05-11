# Кортеж (tuples) – в отличие от списков (list) неизменяемая переменная

mytuple = (78, 89.6, True, 'Строки')
print(mytuple) # полный список
print(mytuple[0]) # вывод первого элемента списка
print(mytuple[1:3]) # вывод элементов со второго по четвертый
print(mytuple[1:]) # вывод элементов со второго

# Словари (dicts = {})
mydict = {"name": "Alina", "role": "QA", 123: 'test-value'}
print(mydict) #вывод всех данных
print(mydict["name"]) # вывод переменной name
print(mydict[123]) # вывод типа переменной
# print(mydict[0]) ошибка из-за отсутствия ключа 0
print(mydict.keys()) # вывод ключей (name, role)
print(mydict.values()) # вывод значений (Alina, QA)

name = 'Alina'
mydict = {
    "name": name,
    'role': 'QA'
}
print(mydict["name"])

# Множество (set)
mylist = [0, 1, 2, 2, 3, 4, 4, 4, 5, 6, 7]
myset = set(mylist)
print(myset)


# преобразование
x = 5.67
x = int(x)
print(x+5)
x = str(x)
print(x+'строка')
x = float(x)
print(x)

a = 'Hello world'
print(a[0])
print(a[1])
print(a[2])
a = list(a)
print(a)

mylist = [0, 1, 2, 2, 3, 4, 4, 4, 5, 6, 7]
myset = set(mylist)
mylist = list(myset)
print(mylist)

mytuple = tuple(mylist)
print(mytuple)

# bin(x)
# hex(x)
# oct(x)

print(chr(5))
print(ord('a'))
print(chr(97))
print(ord('A'))
print(chr(65))

a = 5
b = 10
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) # % – остаточный процент, т. е. число после . Пример: из деления чисел получилось 5, что выведено в результат

# присваивание
a += b
a -= b
a *= b
a **= b
a /= b
a //= b
a %= b

# логический оператор
# and - и
# or - или
# not – нет