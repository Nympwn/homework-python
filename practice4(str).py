from itertools import permutations

# Task 1

word = input('Введите фразу:\n')
print(word[::-1])

# Task 2

word1 = input('Введите первое слово:\n').lower()
word2 = input('Введите второе слово:\n').lower()

if sorted(word1) == sorted(word2):
    print('Ваши слова – анаграмма.')
    print(word1, '–', word2)
else:
    print('Слова не являются анаграммой.')

# Task 3

phrase = input('Введите фразу:\n')
phrase = phrase.lower()
count_vowels = 0
count_consonants = 0

vowels = 'аяиуэеоиюёыeuoia'
consonants = 'йцкнгшщзхфвпрлджчсмтбqwrtypsdfghjklzxcvbnm'

for letter in phrase:
    if letter in vowels:
        count_vowels += 1
print(f'Количество гласных в вашем слове: {count_vowels}.')

for letters in phrase:
    if letters in consonants:
        count_consonants += 1
print(f'Количество согласных в вашем слове: {count_consonants}.')

# Task 4

word = input('Введите фразу:\n')
phrase = word.lower()
phrase = phrase.replace(' ', '')

if phrase == phrase[::-1]:
    print(f'Фраза "{word}" является палиндромом.')
else:
    print(f'Фраза "{word}" не является палиндромом.')

# Task 5

word = input('Введите слово:\n').lower()
my_list = list(word)
n = len(my_list)
index = 0
stack = [(my_list, 0)]

while index < len(stack):
    current, l = stack[index]
    index += 1

    if l == n - 1:
        print(''.join(current))
    else:
        i = n - 1
        while i >= l:
            temp = current[:]
            temp[l], temp[i] = temp[i], temp[l]
            stack.append((temp, l + 1))
            i -= 1

# Решение через import permutations

s = input('Введите слово:\n').lower()
perm = permutations(s)

for p in perm:
    print(''.join(p))

# Task 6

phrase = input('Введите фразу:\n').replace(' ', '')

print(phrase)

# Task 7

phrase = input('Введите фразу:\n')
phrase.lower()
spisok = phrase.split()

print(max(spisok, key=len))

# Task 8

phrase = input('Введите фразу: \n').lower()
replaceable = input('Введите заменяемое слово: \n').lower()
replacement = input('Введите слово, на которое нужно заменить предыдущее: \n').lower()

new_phrase = phrase.replace(replaceable, replacement)
print(new_phrase.capitalize())

# Task 9

phrase = input('Введите фразу:\n').lower()
alphabet = set('абвгдеёжзийклмниопрстуфхцчшщъыъэуя')
result = 1

for x in alphabet:
    if x not in phrase:
        result = 0
        break

if result == 1:
    print('Ваша фраза является панграммой.')
else:
    print('Ваша фраза не является панграммой.')

# Task 10

phrase = input('Введите фразу:\n')

print(phrase.title())