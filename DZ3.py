from selectors import SelectSelector

text = input('Введите текст:\n').lower()
word = input('Введите слово из вашего текста:\n').lower()

vowels = 'аяиуэеоиюёы'
consonants = 'йцкнгшщзхфвпрлджчсмтб'

count_vowels = 0
count_consonants = 0

for x in text:
    if x in vowels:
        count_vowels += 1

for y in text:
    if y in consonants:
        count_consonants += 1

print(f'Количество гласных букв в вашей фразе {count_vowels}.')
print(f'Количество согласных букв в вашей фразе {count_consonants}.')

list_word = text.split()
max_word = max(list_word, key=len)

print(f'Самое длинное слово в вашем тексте: {max_word}.')

desired_word = text.count(word)
if desired_word == 2 or desired_word == 3 or desired_word == 4:
    print(f'Слово "{word}" встречается в вашем тексте {desired_word} раза.')
else:
    print(f'Слово "{word}" встречается в вашем тексте {desired_word} раз.')