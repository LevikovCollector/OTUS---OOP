from figure_objects import Triangle
import pytest

class TestTriangle():
    def test_istance(self, create_triangle):
        '''Проверяем принадлежность к классу'''
        assert isinstance(create_triangle, Triangle)

    def test_area(self, create_triangle):
        '''Проверяем функцию для расчета площади'''
        assert create_triangle.area == 14.7

    def test_perimetr(self, create_triangle):
        '''Проверяем функцию для расчета периметра'''
        assert create_triangle.perimetr == 18

    def test_count_angles(self):
        '''Проверяем количество вершин'''
        assert Triangle.angles() == 3

    def test_sum_area(self, create_triangle, create_rectangle):
        '''Проверяем функцию для расчета суммы площадей'''
        assert create_triangle.add_square(create_rectangle) == 29.7

    def test_error_add_square(self, create_triangle):
        with pytest.raises(AttributeError):
            create_triangle.add_square(int)