name = input('What is your name? \n')
age = input('How old are you? \n')
yesnot = input('You like to programming? Yes or no? \n')

user_info = {
    'What is your name?': name,
    'How old are you?': age,
    'You like to programming?': yesnot
}

print(user_info)

print('Решите выражение: \ny < x - 2')
x = int(
    input('Введите число x: \n')
)
y = int(
    input('Введите число y \n')
)

print('Корректность вычисления:\n')

print(y < x-2)