import pytest

from figure_objects import Rectangle


class TestRectangle():
    def test_istance(self, create_rectangle):
        '''Проверяем принадлежность к классу'''
        assert isinstance(create_rectangle, Rectangle)

    def test_area(self, create_rectangle):
        '''Проверяем функцию для расчета площади'''
        assert create_rectangle.area == 15

    def test_perimetr(self, create_rectangle):
        '''Проверяем функцию для расчета периметра'''
        assert create_rectangle.perimetr == 16

    def test_count_angles(self):
        '''Проверяем количество вершин'''
        assert Rectangle.angles() == 4

    def test_sum_area(self, create_rectangle, create_circle):
        '''Проверяем функцию для расчета суммы площадей'''
        assert create_rectangle.add_square(create_circle) == 216.06

    def test_error_add_square(self, create_rectangle):
        with pytest.raises(AttributeError):
            create_rectangle.add_square(int)
