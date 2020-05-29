from string import ascii_letters  # letters
from string import digits  # numbers
import itertools  # onelove

from random import randint

alphabet = (ascii_letters + digits)
print(alphabet)

'''
8. Написать функцию `XOR_cipher`, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования, которая
возвращает строку, зашифрованную путем применения операции XOR (битовое исключающее ИЛИ) над символами строки с ключом.
Написать также функцию `XOR_uncipher`, которая по зашифрованной строке и ключу восстанавливает исходную строку.
'''

# ord(chr) -> int
# Возвращает числовое представление для указанного символа.
# ЗЫ ,бикоз хер работает со строками
# chr --   Возвращает cимвол, в виде строки, чья позиция кода для Юникод равна указанному целому i
#  ord -- Возвращает для указанного Юникод-символа целое, представляющее его позицию кода.
#
# abra = 'banana'
# cadabra = (11, 22, 33, 44, 55, 66)
# q = zip(abra, cadabra)
# print(q)


s = (input('Enter string: '))
k = (input('Enter Key (len(key) must be >= string) : '))  # key >= string


def xor_cipher(s, k):  # создаем ф=цию
    return ''.join([chr(ord(x) ^ ord(y)) for (x,y) in zip(s, itertools.cycle(k))]) #взвращаем склеивая строки

encoded = xor_cipher(s, k)
print(encoded)

k = (input('Enter Key: '))
decoded = xor_cipher(encoded, k)
print(decoded)


'''
9. Написать функцию для перевода десятичного числа в другую систему исчисления (2-36).  
Небольшая подсказка. В этой задаче вам понадобится:
    - список
    - метод `revers()` (или срез [::-1], или вместо `revers()` использовать `insert()` тогда не придётся разворачивать 
    список), чтоб развернуть список, метод `join()`
    - строка `ascii_uppercase` из модуля `string` (её можно получить если сделать импорт `from string import 
    ascii_uppercase`), она содержит все буквы латинского алфавита.
'''

n = (int(input('Yo digit: ')))  # Вводим число в десятичной системе
b = (int(input('Yo base (2-36): ')))  # Вводим основание

def calculation(n, b):
    a = (digits + ascii_letters)   # словарь
    res = ''  # Заводим место для хранения
    while n:  # пока н - тру
        n, i = n // b, n % b   # divmod(n, b) можно записать через параметр дивмод  Для целых результат аналогичен (a // b, a % b).
        res = a[i] + res 
    return res


print(calculation(n, b))


'''
10. Написать функцию, циклически сдвигающую целое число на N разрядов вправо или влево, в зависимости от третьего 
параметра функции. Функция должна принимать три параметра: в первом параметре передаётся число для сдвига, второй 
параметр задаёт количество разрядов для сдвига (по умолчанию сдвиг на 1 разряд), 3-й булевский параметр задаёт 
направление сдвига (по умолчанию влево (False)).
'''

a = (int(input("Число для сдвига: ")))
print(a)
b = (int(input("Кол-во разрядов для сдвига : ")))
c = (input('False - Влево, True - Вправо: '))

def shift_left(number, step):
    for _ in range(step):
        tmp = number
        d = 0
        rate = 0
        while tmp > 0:
            d = tmp % 10
            tmp //= 10
            rate += 1

        number = number % (10 ** (rate-1)) * 10 + d
    return number

def shift_right(number, step):
    for _ in range(step):

        tmp = number
        d = tmp % 10
        tmp //= 10
        rate = 1
        while tmp > 0:
            tmp *= 10
            tmp += 1
        number = d * rate + number // 10
    return number

def shift(number, step, side=False):
    if side:
        res = shift_right(number, step)
    else:
        res = shift_left(number, step)
    return res

a = shift(a, b, c)
print(a)
print()
'''
3. Реверс списка
    - Принцип алгоритма заключается в следующем: мы меняем местами 0-ый элемент с последним, 1-ый с предпоследним и д.т.
    - Итого количество таких обменов будет равно половине длины списка. Иначе элементы поменяются местами по-второму кругу
и вернутся в первоначальное положение.
'''
# выдумывал велосипед, а оказалось, все более чем просто

lst = [randint(1, 100) for _ in range(11)]
print(lst)

lst = lst[::-1]
print(lst)

