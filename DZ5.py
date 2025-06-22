def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    print(f'{n} число в строке Фибоначчи: {b - a}')

n = int(input('Введите целое не отрицательное число:\n'))
fibonacci(n)

'''
Ответ по первой задаче:
def F(4): результат 7
'''