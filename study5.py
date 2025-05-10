import math
# from math import sqrt – импорт определенной функции
# from math import * – как первая строка, импортирует все

# abs – модуль числа (положительное число)

print(abs(-89))
print(abs(2.4))
print(abs(67))

# pow – возведение в степень
# pow(base, exp[, mod]) – возвращает base в степени exp

print(pow(2, -2)) #0.25
print(pow(2, 10)) #1024
print(pow(64, 0.5)) #8
print(64 ** 0.5) # равноценно предыдущей строке

# При аргументе mod функция вернет остаток по модулю (возведет число в степень и найдет остаток от деления числа mod)
print(pow(5, 2, 5)) # 25/5 = 0

#round – округляет число с точностью n знаков после запятой
print(round(5.56)) # округлить до целого
print(round(5.56, 1)) # округлить до первого знака после запятой
print(round(4.75466, 3))

# модуль math – математические функции (import math в первой строке обязателен)

# math.ceil – округление к большему значению
print(math.ceil(5.7)) # 6
print(math.ceil(5.2)) # 6
# math.floor – округление к меньшему значению
print(math.floor(5.8)) # 5
print(math.floor(5.3)) # 5

# math.log – вычисление логарифма, x – число, base – основание
print(math.log(25, 2))

# math.sqrt – вычисление квадратного корня из числа
print(math.sqrt(25))

# условный оператор if (если)
# общая неполная форма записи
a = 5
b = 5
if a == b:
    print('a=b')
# полная форма записи
a = 8
b = 5
if a<b:
    print('a<b')
else:
    print('a>b')
# if – если; условие if не является правдивым – выводится else

cost = 2000
if cost < 1000:
    print('no discount')
if cost < 3000:
    print('discount 5%')
if cost < 5000:
    print('discount 7%')
else:
    print('discount 10%')