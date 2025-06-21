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

def f():
    global a
    global b
    b, c = a, b
def g():
    global a
    global d
    c = '0'
    a = d + c

a = '2'
b = '3'
c = '5'
d = '7'
f()
g()
f()
print(a + b + c + d)

# Рекурсия

def F(n):
    if n > 2:
        return  F(n - 1) + F(n - 1)
    else:
        return 1

n = int(input())
print(F(n))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input('n = '))
print(factorial(n))

def F(n):
    if n > 2:
        return F(n - 1) + G(n - 2)
    else:
        return n

def G(n):
    if n > 2:
        return G(n - 1) + F(n - 2)
    else:
        return n + 1

print(F(4))