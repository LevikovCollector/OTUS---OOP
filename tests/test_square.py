import pytest

from figure_objects import SquareFigure


class TestSquare():
    def test_istance(self, create_square):
        '''Проверяем принадлежность к классу'''
        assert isinstance(create_square, SquareFigure)

    def test_area(self, create_square):
        '''Проверяем функцию для расчета площади'''
        assert create_square.area == 49.0

    def test_perimetr(self, create_square):
        '''Проверяем функцию для расчета периметра'''
        assert create_square.perimetr == 28

    def test_count_angles(self):
        '''Проверяем количество вершин'''
        assert SquareFigure.angles() == 4

    def test_sum_area(self, create_square, create_triangle):
        '''Проверяем функцию для расчета суммы площадей'''
        assert create_square.add_square(create_triangle) == 63.7

    def test_error_add_square(self, create_square):
        with pytest.raises(AttributeError):
            create_square.add_square(int)