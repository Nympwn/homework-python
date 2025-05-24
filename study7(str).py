'''
Строка – неизменяемый тип данных
Может быть только перезаписана
'''

my_num = 123
my_str = str(my_num)
print(my_str)

'''
Операции над строками
Общие: 
x in s 
s[i]
s[i, j] – вывод диапазона символов i <= k < j
min(s)
s.count(x) – найти количество символов в строке x
s + t – "склеивание" символов
s * n – повторение несколько раз (n)
len(s) – длина последовательности (списка)
s.index(x) – возвращает индекс подстроки (какое место занимает в списке от 0)

Дополнительные:
s.capitalize – переводит первую букву в заглавную
s.title – первые буквы становятся заглавными в каждом слове
s.upper – все буквы становятся заглавными
s.lower – все буквы становятся строчными
s.swapcase – замена регистра (меняются зеркально)
s.isupper – true, если все буквы во фразе заглавные, false в других случаях
s.islower – true, если все буквы во фразе строчные, false в других случаях
s.istitle – true, если каждое слово начинается с заглавной буквы, false в других случаях
s.find
s.islower
s.replaсe
s.split
s.startswith
'''

a = [1, 2, 3, 5, 7, -7, 3]
print(a.index(7))
print(a.count(3))

string = 'Hello world'
print(string.count('o'))

string = 'hello World, How are You?'
print(string.capitalize())
print(string.title())
print(string.upper())
print(string.lower())
print(string.swapcase())
print(string.islower())
print(string.isupper())