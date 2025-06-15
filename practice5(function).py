# # Task 1
#
# def symbol(num):
#     print('–' * num)
#     print('–' * num)
#
# n = int(input('Введите число: \n'))
#
# symbol(n)
#
# # Task 2
#
# def rectangle(num):
#     print(f'{"–" * num}')
#     print(f'|{" " * (num - 2)}|')
#     print(f'{"–" * num}')
#
#
# n = int(input('Введите ширину прямоугольника: \n'))
#
# rectangle(n)
#
# # Task 3
#
# def triangle(n):
#     for i in range(1, n+1):
#         print('*' * i)
#
# n = int(input('Введите размер стороны треугольника:\n'))
# triangle(n)
#
# # Task 4
#
# def arif_mean(a, b, c, d, e):
#     print(f'Среднее арифметическое введенных чисел: {(a + b + c + d + e) / 5}')
#
# a = int(input('Введите первое число:\n'))
# b = int(input('Введите второе число:\n'))
# c = int(input('Введите третье число:\n'))
# d = int(input('Введите четвертое число:\n'))
# e = int(input('Введите пятое число:\n'))
#
# arif_mean(a, b, c, d, e)
#
# # Task 5
#
# def count_symbol(n):
#     print(f'В вашем числе {len(str(n))} символов.')
#
# n = int(input('Введите число:\n'))
# count_symbol(n)
#
# # Task 7
# # Перепутала с прямоугольником. Переделаю по возможности
# def perimeter(a, b, c, d):
#     if a > b or c > d:
#         print('Нет верных данных. Расчет невозможен.')
#     elif a < 0 or b < 0 or c < 0 or d < 0:
#         print('Нет верных данных. Расчет невозможен.')
#     else:
#         print(f'Периметр вашего многоугольника равен {((b - a) + (d - c)) * 2}')
#
# a = int(input('Введите начальную координату ширины вершины прямоугольника:\n'))
# b = int(input('Введите конечную координату ширины вершины прямоугольника:\n'))
# c = int(input('Введите начальную координату высоты вершины прямоугольника:\n'))
# d = int(input('Введите конечную координату высоты вершины прямоугольника:\n'))
#
# # ------------------------------------------------------------------------------
#
# perimeter(a, b, c, d)
#
# def distance(x1, y1, x2, y2):
#     return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
#
# def triangle_perimeter(x1, y1, x2, y2, x3, y3):
#     a = distance(x1, y1, x2, y2)
#     b = distance(x2, y2, x3, y3)
#     c = distance(x3, y3, x1, y1)
#     return a + b + c
#
# print(triangle_perimeter(1, 2, 4, 5, 6, 7))
#
# # Task 8
#
# def simple_number():
#     list_numbers = []
#     for x in range(100, 1000):
#         is_simple = True
#         for y in range(x // 2 + 1, 1, -1):
#             if x % y == 0:
#                 is_simple = False
#                 break
#         if is_simple:
#             list_numbers.append(x)
#     print(*list_numbers)
#
# simple_number()
#
# # Task 9
#
# def sum_n(num):
#     sum1 = 0
#     for digit in num:
#         sum1 += int(digit)
#     return sum1
#
# def summa_numbers(number):
#     s = str(number)
#     one_num = s[:3]
#     two_num = s[3:]
#     if sum_n(one_num) == sum_n(two_num):
#         return True
#     else:
#         return False
#
# list_lucky = []
# for num in range(100000, 1000000):
#     if summa_numbers(num):
#         list_lucky.append(num)
#
# print(*list_lucky)
#
# # Task 10
#
# def max_number(a, b, c, d, e, f):
#     max_num = max(a, b, c, d, e, f)
#     print(f'Максимальное число из вашего списка {max_num}.')
#
# a = int(input('Введите первое число:\n'))
# b = int(input('Введите второе число:\n'))
# c = int(input('Введите третье число:\n'))
# d = int(input('Введите четвертое число:\n'))
# e = int(input('Введите пятое число:\n'))
# f = int(input('Введите шестое число:\n'))
#
# max_number(a, b, c, d, e, f)
#
# Task 11

# Task 12

# # Task 13
#
# def side_lateral(a, b, h):
#     side_pif = abs((a - b) / 2)
#     return round((side_pif ** 2 + h ** 2) ** 0.5, 2)
#
# def perimeter(a, b, h):
#     return a + b + side_lateral(a, b, h) * 2
#
# def square(a, b, h):
#     return (a + b) / 2 * h
#
# a1 = int(input('Введите длину первого основания первой трапеции:\n'))
# b1 = int(input('Введите длину второго основания первой трапеции:\n'))
# h1 = int(input('Введите высоту первой трапеции:\n'))
#
# a2 = int(input('Введите длину первого основания второй трапеции:\n'))
# b2 = int(input('Введите длину второго основания второй трапеции:\n'))
# h2 = int(input('Введите высоту второй трапеции:\n'))
#
# print(f'Сумма площадей двух равнобедренных трапеций равна {square(a1, b1, h1) + square(a2, b2, h2)}')
# print(f'Сумма периметров двух равнобедренных трапеций равна {perimeter(a1, b1, h1) + perimeter(a2, b2, h2)}')
#
# # Task 14
#
# def square_triangle(a, h):
#     return (a * h) / 2
#
# def square_rectangle(c, b):
#     return c * b
#
# def square_circle(r):
#     return round(r ** 2 * 3.14, 2)
#
# choices = input('Введите, площадь чего нужно вычислить:\n'
#                 '1) прямоугольник;\n'
#                 '2) треугольник;\n'
#                 '3) круг.\n'
#                 'Ответ: ').lower()
#
# symbol_remove = '.,!?():;"_-'
# for symbol in symbol_remove:
#     choices = choices.replace(symbol, '')
#
# if choices == '1' or choices == 'прямоугольник':
#     c = float(input('Введите длину прямоугольника:\n'))
#     b = float(input('Введите высоту прямоугольника:\n'))
#
#     print(f'Площадь вашего прямоугольника равна {square_rectangle(c, b)}.')
#
# elif choices == '2' or choices == 'треугольник':
#     a = float(input('Введите длину основания треугольника:\n'))
#     h = float(input('Введите высоту треугольника:\n'))
#
#     print(f'Площадь вашего треугольника равна {square_triangle(a, h)}.')
#
# elif choices == '3' or choices == 'круг':
#     r = float(input('Введите радиус круга:\n'))
#
#     print(f'Площадь вашего круга равна {square_circle(r)}.')
#
# else:
#     print('Введены неверные данные.')
#
# # Task 16
#
# def square(n, s):
#     for x in range(1, n + 1):
#         print(s * n)
#
# n = int(input('Введите размер стороны квадрата:\n'))
# s = str(input('Введите символ, из которого будет состоять квадрат:\n'))
#
# square(n, s)
#
# # Task 17
#
# def dividers(n):
#     is_dividers = []
#     for x in range(1, n + 1):
#         if n % x == 0:
#             is_dividers.append(x)
#     print('Список делителей для вашего числа:')
#     print(*is_dividers)
#
# while True:
#     number = int(input('Введите число (0 для выхода из программы):\n'))
#     if number == 0:
#         break
#     dividers(number)
