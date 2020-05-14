s = int (input('Введите высоту фигуры : '))
cols = rows = s * 2 - 1

# i == rows - 1  = i == cols-1  нижняя строка
# i == rows // 2  =  i==rows-i -1 центральная строка
# j == rows - 1    центральный столбец \\  rows <= j + 1
# i == cols - j -1  левая пустая диагональ \\ если >= закрасит и сделает треугольник \\если <= закрасит все снаружи
# j == rows - i -1 тоже самое левая грань треугольника
# (j == cols // 2 and i > cols // 2)  -  столбец посредине до половины высоты
# i == 0 - верхняя грань
# i == j - диагональ сверху справа, вниз на лево
# cols // 2 == j and i == cols // 2  центральная точка
#
#Все Это Весело, А Теперь, Что Пригодилось
#
#   j == cols // 2 - i  -половинная диагональ 1й четверти
#   j == cols // 2 + i  -половинная диагональ 2й четверти
#   i == cols // 2 + j  -половинная диагональ 3й четверти
#   j == cols // 2 - j + rows - 1  -половинная диагональ 4й четверти ( какого, ХYZ, она так работает? )
#   j == cols // 2  -вертикальная ось
#   i == cols // 2  -горизонтальная ось
#
#
#
#
print("Figure A")
for i in range(rows):

    for j in range(cols):
        if i == cols // 2  or j == cols//2 + i  or j == cols//2 - i:
            print('#', end=' ')
        else:
            print(' ', end=' ')
    print()



print()


print("Figure B")
for i in range(rows):

    for j in range(cols):
        if i == cols // 2 or j == cols // 2 + i or j == cols // 2 - i \
               or j > cols// 2 - i and j < cols // 2 + i and i < cols//2 :
            print('$', end=' ')
        else:
            print(' ', end=' ')
    print()



print()

print("Figure C")
for i in range(rows):

    for j in range(cols):
        if i == cols // 2 or j == cols // 2 + i or j == cols // 2 - i\
        or j > cols// 2 - i and j < cols // 2 + i and i < cols//2 \
                or i == cols // 2 + j or   i == cols // 2 - j + rows - 1:  #WTF!??? почему нижняя правая диагональ именно так работает?
            print('&', end=' ')
        else:
            print(' ', end=' ')
    print()



print()

print()


print("Figure D")
for i in range(rows):

    for j in range(cols):
        if i == cols // 2  or j == cols//2 or j == cols // 2 - i or j == cols // 2 + i\
                or j > cols// 2 - i and j < cols // 2 + i and i < cols//2 \
                or i == cols // 2 + j or   i == cols // 2 - j + rows - 1 :  #WTF!??? почему нижняя правая диагональ именно так работает?
            print('#', end=' ')
        else:
            print(' ', end=' ')
    print()



print()
