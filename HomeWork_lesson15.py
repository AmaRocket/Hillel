'''
1. Реализовать класс цифрового счетчика.
Обеспечьте возможность установки максимального и минимального значений,
увеличения счетчика на 1, возвращения текущего значения.
'''



class Counter:
    num = 0
    def __init__(self, minimum=0, maximum=0, k=0):
        self.minimum = minimum
        self.maximum = maximum
        self.k = k

    def up(self):
        if self.num < self.maximum:
            self.num += 1
            return self.num
        else:
            return 'Out of circle'


count=Counter(1,4)
print(count.up())
print(count.up())
print(count.up())
print(count.up())

'''
2. Создать класс, описывающий группу студентов - `Group`. 
Данный класс хранит студентов в виде списка объектов `Student` также реализованного в виде соответствующего класса.
В классах реализовать необходимай набор атрибутов 
(Например класс `Student` должен иметь атрибуты `name`, `age`, `grades`), 
а так же необходимый набор методов экземпляра для работы с этими экземплярами.

Наследование здесь не понадобится.

class Group:
    def __init__(self(self, Student)):

    class Student:
        def __init__(self, age, name, grades):

'''