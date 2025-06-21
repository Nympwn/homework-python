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
# # Task 11
#
# def exchange(a, b, c, d):
#     a, b = b, a
#     c, d = d, c
#     print(f'Значение a равно {a}.\n'
#           f'Значение b равно {b}.\n'
#           f'Значение c равно {c}.\n'
#           f'Значение d равно {d}.')
#
# a = int(input('Введите значение a:\n'))
# b = int(input('Введите значение b:\n'))
# c = int(input('Введите значение c:\n'))
# d = int(input('Введите значение d:\n'))
#
# exchange(a, b, c, d)
#
# # Task 12
#
# def perimeter_triangle(a, b, c):
#     return a + b + c
#
# def square_triangle(a, b, c):
#     half_p = perimeter_triangle(a, b, c) / 2
#     return (half_p*(half_p - a)*(half_p - b)*(half_p - c)) ** 0.5
#
# a1 = float(input('Введите первую длину стороны первого треугольника:\n'))
# b1 = float(input('Введите вторую длину стороны первого треугольника:\n'))
# c1 = float(input('Введите третью длину стороны первого треугольника:\n'))

# a2 = float(input('Введите первую длину стороны второго треугольника:\n'))
# b2 = float(input('Введите вторую стороны второго треугольника:\n'))
# c2 = float(input('Введите третью длину стороны второго треугольника:\n'))
#
# sum_perimeter = perimeter_triangle(a1, b1, c1) + perimeter_triangle(a2, b2, c2)
# sum_square = round(square_triangle(a1, b1, c1) + square_triangle(a2, b2, c2), 2)
#
# print(f'Сумма периметров двух треугольников равна {sum_perimeter}')
# print(f'Сумма площадей двух треугольников равна {sum_square}')
#
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
#
# # Task 19
#
# def point_in_rect(a, a1, a2, b, b1, b2):
#     return a1 <= a <= a2 and b1 < b < b2
#
# point_up_left1 = int(input('Введите координату высоты верхней левой точки прямоугольника:\n'))
# point_up_left2 = int(input('Введите координату ширины верхней левой точки прямоугольника:\n'))
# point_down_right1 = int(input('Введите координату высоты нижней правой точки прямоугольника:\n'))
# point_down_right2 = int(input('Введите координату ширины нижней правой точки прямоугольника:\n'))
# point1 = int(input('Введите координату высоты точки:\n'))
# point2 = int(input('Введите координату ширины точки:\n'))
#
# print(point_in_rect(point1, point_up_left1, point_down_right1, point2, point_up_left2, point_down_right2))
#
# # Task 20
#
# def side_len(a1, a2, b1, b2):
#     return ((a2 - a1)**2 + (b2 - b1)**2)**0.5
#
# def triangle_square(c, d, e):
#     half_perimeter = (c + d + e) / 2
#     return (half_perimeter * (half_perimeter - c) * (half_perimeter - d) * (half_perimeter * e))**0.5
#
# def point_in_triangle(a, a1, a2, a3, b, b1, b2, b3):
#     c = side_len(a1, a2, b1, b2)
#     d = side_len(a2, a3, b2, b3)
#     e = side_len(a3, a1, b3, b1)
#     square = triangle_square(c, d, e)
#
#     c1 = side_len(a, a1, b, b1)
#     d1 = side_len(a, a2, b, b2)
#     e1 = side_len(a2, a3, b2, b3)
#     square1 = triangle_square(c1, d1, e1)
#
#     c2 = side_len(a, a2, b, b2)
#     d2 = side_len(a, a3, b, b3)
#     e2 = side_len(a2, a3, b2, b3)
#     square2 = triangle_square(c2, d2, e2)
#
#     c3 = side_len(a, a3, b, b3)
#     d3 = side_len(a, a1, b, b1)
#     e3 = side_len(a3, a1, b3, b1)
#     square3 = triangle_square(c3, d3, e3)
#
#     total_square = square1 + square2 + square3
#     return square == total_square
#
# point_triangle_up1 = int(input('Введите координату высоты верхней точки треугольника:\n'))
# point_triangle_up2 = int(input('Введите координату ширины верхней точки треугольника:\n'))
# point_triangle_right1 = int(input('Введите координату высоты правой точки треугольника:\n'))
# point_triangle_right2 = int(input('Введите координату ширины правой точки треугольника:\n'))
# point_triangle_left1 = int(input('Введите координату высоты левой точки треугольника:\n'))
# point_triangle_left2 = int(input('Введите координату ширины левой точки треугольника:\n'))
# point1 = int(input('Введите координату высоты точки:\n'))
# point2 = int(input('Введите координату ширины точки:\n'))
#
# print(point_in_triangle(point1, point_triangle_up1, point_triangle_left1, point_triangle_right1, point2, point_triangle_up2, point_triangle_left2, point_triangle_right2))
#
# # Task 21
#
# def average_result(a, b, c, d, e):
#     result_list = [a, b, c, d, e]
#     result_list = sorted(result_list)
#     return round(sum(result_list[1:4]) / 3, 2)
#
# score1 = int(input('Введите оценку первого эксперта:\n'))
# score2 = int(input('Введите оценку второго эксперта:\n'))
# score3 = int(input('Введите оценку третьего эксперта:\n'))
# score4 = int(input('Введите оценку четвертого эксперта:\n'))
# score5 = int(input('Введите оценку пятого эксперта:\n'))
#
# print(f'Среднее количество баллов у спортсмена составляет {average_result(score1, score2, score3, score4, score5)}.')
