import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = list(color)
        self.filled = False

        if not self.__is_valid_sides(*sides):
            self.__sides = self.sides_count * [1]
        else:
            self.__sides = list(sides)

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
            if self.__is_valid_color(r, g, b):
                self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return (len(new_sides) == self.sides_count and
                all(isinstance(side, int) and
                side > 0 for side in new_sides))

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(color)

        if not isinstance(circumference, (int, float)) or circumference <= 0:
            print("Длина окружности введена неверно")

        self.__radius = circumference / (2 * math.pi)
        self.set_sides(circumference)

    def get_square(self):
        return math.pi * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, a, b, c):
        super().__init__(color, a, b, c)

    def get_square(self):
        a, b, c = self.sides_count

        if not all(isinstance(side, (int, float)) and side > 0 for side in (a, b, c)):
            print("Стороны должны являться положительным значением")

        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, edge_length):
        super().__init__(color)

        if not isinstance(edge_length, (int, float)) or edge_length <= 0:
            print("Длина ребра введена неверно")

        self.set_sides(*[edge_length] * self.sides_count)

    def get_volume(self):
        edge_length = self.get_sides()[0]
        return edge_length ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())