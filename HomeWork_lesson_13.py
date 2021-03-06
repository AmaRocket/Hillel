from random import randint
'''
Написать функцию сортировки двухмерного списка МхМ (матрицы) Значение М - задаётся пользователем, с клавиатуры.
Может быть любым целым, положительным числом, больше 5. 
Функция должна: 
1. найти сумму элементов столбцов и отсортировать столбцы по возрастанию этих сумм 
2. отсортировать каждый нечётный столбец по возрастанию значений снизу вверх, а каждый чётный столбец по возрастанию значений сверху вниз. 
Так же, ваша программа должна иметь функцию вывода данного списка на экран. 
При выводе, внизу каждого столбца должна выводиться сумма элементов этого столбца.
Что можно использовать: 
1. для создания списка использовать ТОЛЬКО 'list comprehension' и генератор случайных чисел. 
Диапазон случайных чисел для заполнения списка от 1 до 50. Список должен создаваться однострочным выражением. 
2. Можно использовать ТОЛЬКО ДВА списка. 
Первый это двухмерный список размером МхМ, второй, вспомогательный, одномерный список размером М. 
Использование других списков (или коллекций) НЕДОПУСТИМО. 
3. Можно использовать ТОЛЬКО ОДНУ переменную М для хранения размера списка, плюс переменные циклов for. 
4. Для сортировки можно использовать алгоритм пузырьковой сортировки. 
Использование встроенных функций сортировки - НЕДОПУСТИМО (да и не получится их использовать)! 
5. Решение должно включать ТОЛЬКО ДВЕ функции: функцию сортировки (по правилам описанным выше) и функцию вывода на экран.  
Задача считается решённой верно при условии соблюдения всех требований. Аккуратный вывод на экран - приветствуется. 

'''

m = (int(input('Enter size of MTRX : ')))  # size of matrix
matrix = [[randint(1, 50) for i in range(m)] for j in range(m)]  # generate matrix


def show(lst):
    tmp = [0] * len(lst)  # пустой список для сумм в размер матрицы. ЗЫ: еси список пустой - вылетает за границы
    for i in range(len(lst)):  # для каждой строки в списке
        for j in range(len(lst[i])):  # для каждого значения в строке списка
            print('{:>4}'.format(lst[i][j]), end='')  # сама матрица
            tmp[j] = tmp[j] + lst[i][j]  # список сумм
        print()  # шоб красиво було

    print()
    for i in range(len(tmp)):  # для списка сумм
        print('{:>4}'.format(tmp[i]), end='')  # марафет

    print('\n')  # отступ


def sort_matrix(lst):
    temp_list = [0] * len(lst)  # временный список, если пустой - вылетает за границы
    for i in range(len(lst)):  # для каждой строки в списке
        for j in range(len(lst)):  # для каждого значения в строке списка
            temp_list[j] = temp_list[j] + matrix[i][j]  # в каждое значение списка, добавляем значение из матрицы

    for _ in range(len(lst)):  # бабл сорт
        for j in range(len(lst) - 1):
            if temp_list[j] > temp_list[j + 1]:
                temp_list[j], temp_list[j + 1] = temp_list[j + 1], temp_list[j]
                for i in range(len(lst)):
                    lst[i][j], lst[i][j + 1] = matrix[i][j + 1], lst[i][j]

    for column in range(len(lst)):  # ротация столбцов
        for _ in range(len(lst)):
            for i in range(len(lst) - 1):
                if lst[i][column] > lst[i + 1][column] if column % 2 == 0 else lst[i][column] < lst[i + 1][column]:
                    lst[i][column], lst[i + 1][column] = lst[i + 1][column], lst[i][column]


# последние 2 строки сортировка по четным\нечетным значениям столбца

sort_matrix(matrix)
show(matrix)
