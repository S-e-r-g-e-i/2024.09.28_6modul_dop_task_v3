# Дополнительное практическое задание по модулю
import math


class Figure:
    sides_count = 0

    def __init__(self, color: tuple, *args_sides: int):
        self.__color = [*color] if self.__is_valid_color(color) is True else [0, 0, 0]   # список цветов в формате RGB
        self.__sides = [*args_sides] if self.__is_valid_sides(*args_sides) is True else [1] * self.sides_count  # (список сторон (целые числа))
        self.filled = False

    def __is_valid_color(self, new_color: tuple): # проверяет корректность переданных значений перед установкой нового цвета
        flag = 0
        for i in new_color:
            if 255 >= i >= 0 == i % 1 and isinstance(i, int) is True:
                flag += 1
        if flag == 3:
            return True
        else:
            return False

    def set_color(self, *args_new_color: int):           # принимает новый цвет
        # a = args_new_color
        # print(a, type(a))
        self.__color = [*args_new_color] if self.__is_valid_color(args_new_color) is True else self.__color

    def get_color(self):                    # возвращает список RGB цветов
        return self.__color

    def __is_valid_sides(self, *args_sides: int):        # проверка сторон
        flag = 0
        for i in args_sides:
            if i > 0 and i % 1 == 0:
                flag += 1
        if flag == len(args_sides) == self.sides_count:
            return True
        else:
            return False

    def set_sides(self, *new_sides: int):    # принимает новые значения сторон, если их количество не подходит - не меняет
        self.__sides = [*new_sides] if self.__is_valid_sides(*new_sides) is True else self.__sides

    def get_sides(self):                # возвращает список сторон фигуры (длин), не работает в Кубе, тк __sides переопределен
        return self.__sides

    def __len__(self):                  # возвращает периметр фигуры (непонтно зачем __len__ по условию???)
        return sum(self.get_sides())


class Circle(Figure):
    sides_count = 1
    # __radius = Figure.__len__() / (2 * math.pi) #  !? тут не работает код, нужно определять для экземляра, а не класса

    def __init__(self, color: tuple, *args_sides: int):
        super().__init__(color, *args_sides)
        self.__radius = self.__len__() / (2 * math.pi)  # радиус, доп. атрибут экземпляра, !!!НЕ изменяется при изменении стороны(периметра)

    def get_square(self):       # возвращает площадь круга
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        p = sum(self.get_sides()) / 2
        S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return S


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple, sides: int):
        super().__init__(color)
        self.__sides = [sides] * self.sides_count
        # else [args_sides[0]] * 12 if self.sides_count == 12
        # else [args_sides[0]] * 12 if len(args_sides) == 1

    def get_volume(self):
        return self.__sides[0] ** 3


# Проверка
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides()) # !!!????
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


print('\nДополнительные проверки:')
# Проверка площади (круга):
print(circle1.get_square()) # !!!НЕ изменяется при изменении стороны(периметра)

# Проверка треугольника:
trangle1 = Triangle((12, 13, 25), 5, 5, 5)
print(trangle1.get_square())






