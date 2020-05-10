'''
1. Дан список чисел. Определите, сколько в нем встречается различных чисел.
    - Примечание. Эту задачу на Питоне можно решить в одну строчку.
'''
from random import randint


print (len(set([randint(100, 200) for _ in range (int(input('Кол-во элементов для множества: ')))])))



'''
2. Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
    - Примечание. Эту задачу на Питоне можно решить в одну строчку.
'''



print(len((set([randint(10, 20) for _ in range (int(input('Максимальное кол-во элементов для множества A: ')))])).union\
    (set([randint(10, 20) for _ in range
    (int(input('Максимальное кол-во элементов для множества B: ')))]))), '- Eсли считать только уникальные элементы')

print('ИЛИ:')

print(len((set([randint(10, 20) for _ in range (int(input('Максимальное кол-во элементов для множества A: ')))])).intersection\
    (set([randint(10, 20) for _ in range
    (int(input('Максимальное кол-во элементов для множества B: ')))]))), '- Если считать только повторяющиеся элементы')

print('Т.к. небыло сказано какие именно числа нужно подсчитать, а мы используем генератор случайных чисел, в котором числа'
      ' могут повторяться. ')
print('З.Ы. Сорри в одну строчку вышло не очень компактно')

'''
1. В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, 
сколько раз оно встречалось в этом тексте.
Задачу необходимо решить с использованием словаря.
'''

d = {}
for i in (input('Введите предложение: ')).split():
    d[i] = d.get(i, 0) + 1
    print (d [i], end = ' | ')
print()

'''
3. Дан текст состоящий из нескольких строк. Выведите слово, которое в этом тексте встречается чаще всего. 
Если таких слов несколько, выведите последнее.
Задачу необходимо решить с использованием словаря.
'''



d = {} #заводим словарь. а не собаку(
txt = input('Enter your best txt ever: ') #ввод текста

for i in txt.split(): # разделение на составляющие в спискеч
    if i not in d:
        d[i] = 1
    else:
        d[i]+=1 #сюда слова
word = max(d.values())
for key in sorted(d.keys()):
    if d[key] == word:
        print(('Magic word is: '),key)
        break

# А можно ведь было это сделать через ф-цию counter?

'''

'''