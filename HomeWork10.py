
from random import randint

from math import sqrt


'''
1. Дан список случайных целых чисел. Замените все нечетные числа списка нулями. И выведете их количество

'''

lst = [randint(1, 10) for _ in range(10)]
print(lst)
res = []
for idx in lst:
    if idx % 2 != 0:
        res.append(0)
    else:
        res.append(idx)
print(res)

print()

'''
2. Заполните список случайными числами и выполните реверс для части списка между элементами с индексами a и b (включая эти элементы)
'''


lst = [randint(1, 100) for _ in range(10)]
print(lst)
a = lst.index(int(input('Enter 1st digit:  ')))
b = lst.index(int(input('Enter 2nd digit: ')))
print(a, b)
res = lst[:a] + lst[b:a-1:-1] + lst[b+1:]
print(res)




'''
3. Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа): 
периметр квадрата, площадь квадрата и диагональ квадрата.
'''

rows = cols = n = int(input('Enter yo side: '))
def draw_rect(rows, cols):
     for _ in range(rows):
         for _ in range(cols):
             print('\u26bd  ', end='')
         print()
     print()
draw_rect(n,n)


def square(rows):
    return ('Perimetr: ', 4 * rows,
            'Area: ', rows ** 2,
            'Diagonal: ', rows * sqrt(2))


print(square(n))

'''
4. Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.
'''

def is_prime(argument):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n

n = (int(input('digit: ')))
print (is_prime(n))


