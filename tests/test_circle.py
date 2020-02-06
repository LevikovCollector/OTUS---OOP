import pytest

from figure_objects import Circle


class TestCircle():
    def test_istance(self, create_circle):
        '''Проверяем принадлежность к классу'''
        assert isinstance(create_circle, Circle)

    def test_area(self, create_circle):
        '''Проверяем функцию для расчета площади'''
        assert create_circle.area == 201.06

    def test_perimetr(self, create_circle):
        '''Проверяем функцию для расчета периметра'''
        assert create_circle.perimetr == 50.27

    def test_count_angles(self):
        '''Проверяем количество вершин'''
        assert Circle.angles() == 0

    def test_sum_area(self, create_circle, create_square):
        '''Проверяем функцию для расчета суммы площадей'''
        assert create_circle.add_square(create_circle) == 402.12

    def test_error_add_square(self, create_circle):
        with pytest.raises(AttributeError):
            create_circle.add_square(int)
