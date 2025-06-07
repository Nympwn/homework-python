from selectors import SelectSelector

text = input('Введите текст:\n').lower()
word2 = input('Введите слово из вашего текста:\n').lower()

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
max_word = ''
for word in list_word:
    clean_word = ''
    for char in word:
        if char.isalpha():
            clean_word += char
    clean_word = ''.join([c for c in word if c.isalpha()])

max_word = max(list_word, key=len)

print(f'Самое длинное слово в вашем тексте: {max_word}.')


normalized_words = []
for word in list_word:
    clean = ''.join([c for c in word if c.isalpha()])
    normalized_words.append(clean)

desired_word = normalized_words.count(word2)
if desired_word == 2 or desired_word == 3 or desired_word == 4:
    print(f'Слово "{word2}" встречается в вашем тексте {desired_word} раза.')
else:
    print(f'Слово "{word2}" встречается в вашем тексте {desired_word} раз.')