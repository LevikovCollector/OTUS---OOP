import pytest

from figure_objects import Triangle, Rectangle, Circle, SquareFigure


@pytest.fixture
def create_triangle():
    return Triangle('Новый треугольник', 5, 6, 7)

@pytest.fixture
def create_rectangle():
    return Rectangle('Новый прямоугольник', 3, 5)

@pytest.fixture
def create_circle():
    return Circle('Новый круг', 8)

@pytest.fixture
def create_square():
    return SquareFigure('Новый квадрат', 7)


