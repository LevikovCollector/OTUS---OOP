from math import sqrt, pow


class GeometryFigure():
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    @staticmethod
    def angles():
        pass


    def perimetr(self):
        pass

    def add_square(self, second_figure):
        if isinstance(second_figure, GeometryFigure):
            return self.area + second_figure.area
        else:
            raise AttributeError('Не принадлежит к классу GeometryFigure!')


class Triangle(GeometryFigure):
    calc_perimetr = None
    square = None

    def __init__(self, name, side_a, side_b, side_c):
        super(GeometryFigure).__init__()
        self.name = name
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self):
        half_perimetr = self.perimetr / 2
        self.square = sqrt(half_perimetr * (half_perimetr - self.side_a)
                           * (half_perimetr - self.side_b)
                           * (half_perimetr - self.side_c))
        return  float('{0: .2f}'.format(self.square))

    @property
    def perimetr(self):
        self.calc_perimetr = self.side_a + self.side_b + self.side_c
        return self.calc_perimetr

    def angles():
        return 3


class SquareFigure(GeometryFigure):
    def __init__(self, name, side_a):
        super(GeometryFigure).__init__()
        self.name = name
        self.side_a = side_a

    @property
    def area(self):
        return pow(self.side_a, 2)

    @property
    def perimetr(self):
        return 4 * self.side_a

    def angles():
        return 4


class Rectangle(SquareFigure):
    def __init__(self, name, side_a, side_b):
        super(SquareFigure).__init__()
        self.name = name
        self.side_a = side_a
        self.side_b = side_b

    @property
    def perimetr(self):
        return 2 * (self.side_a + self.side_b)

    @property
    def area(self):
        return self.side_a * self.side_b


class Circle(GeometryFigure):
    pi = 3.14159

    def __init__(self, name, radius):
        super(GeometryFigure).__init__()
        self.name = name
        self.rad = radius


    def angles():
        return 0

    @property
    def perimetr(self):
        return float('{0: .2f}'.format(2 * self.pi * self.rad))

    @property
    def area(self):
        return float('{0: .2f}'.format(self.pi * pow(self.rad, 2)))

if __name__ == '__main__':
    trigl_1 = Triangle('первый треугольник', 4, 5, 6)
    print(trigl_1.area)
    print(trigl_1.perimetr)
    print('----------------------------')
    rec_1 = Rectangle('прямоугольник 1', 4, 3)
    print(rec_1.area)
    print(Rectangle.angles())
    print('----------------------------')
    sq_1 = SquareFigure('квадрат 1', 5)
    print(sq_1.area)
    print(SquareFigure.angles())
    print('----------------------------')
    circl_1 = Circle('первый круг', 5)
    print(circl_1.area)
    print(circl_1.perimetr)
    print(Circle.angles())