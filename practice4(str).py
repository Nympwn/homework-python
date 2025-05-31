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

# Task 6

phrase = input('Введите фразу:\n').replace(' ', '')

print(phrase)

# Task 7

phrase = input('Введите фразу:\n')
phrase.lower()
spisok = phrase.split()

print(max(spisok, key=len))

# Task 8