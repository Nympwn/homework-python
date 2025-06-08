# Task 1

def symbol(num):
    print('–' * num)
    print('–' * num)

n = int(input('Введите число: \n'))

symbol(n)

# Task 2

def rectangle(num):
    print(f'{"–" * num}')
    print(f'|{" " * (num - 2)}|')
    print(f'{"–" * num}')


n = int(input('Введите ширину прямоугольника: \n'))

rectangle(n)

# Task 3

def triangle(n):
    for i in range(1, n+1):
        print('*' * i)

n = int(input('Введите размер стороны треугольника:\n'))
triangle(n)

# Task 4

def arif_mean(a, b, c, d, e):
    print(f'Среднее арифметическое введенных чисел: {(a + b + c + d + e) / 5}')

a = int(input('Введите первое число:\n'))
b = int(input('Введите второе число:\n'))
c = int(input('Введите третье число:\n'))
d = int(input('Введите четвертое число:\n'))
e = int(input('Введите пятое число:\n'))

arif_mean(a, b, c, d, e)

# Task 5

def count_symbol(n):
    print(f'В вашем числе {len(str(n))} символов.')

n = int(input('Введите число:\n'))
count_symbol(n)

# Task 7

def perimeter(a, b, c, d):
    if a > b or c > d:
        print('Нет верных данных. Расчет невозможен.')
    elif a < 0 or b < 0 or c < 0 or d < 0:
        print('Нет верных данных. Расчет невозможен.')
    else:
        print(f'Периметр вашего многоугольника равен {((b - a) + (d - c)) * 2}')

a = int(input('Введите начальную координату ширины вершины прямоугольника:\n'))
b = int(input('Введите конечную координату ширины вершины прямоугольника:\n'))
c = int(input('Введите начальную координату высоты вершины прямоугольника:\n'))
d = int(input('Введите конечную координату высоты вершины прямоугольника:\n'))

perimeter(a, b, c, d)