import unittest
from triangle_func import IncorrSide, get_triangle_type

class TestTriangleFunc(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(get_triangle_type(1, 1, 1), "равносторонний")

    def test_isosceles(self):
        self.assertEqual(get_triangle_type(3, 4, 4), "равнобедренный")

    def test_nonequilateral(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "неравносторонний")

    def test_invalid_sides_1(self):
        with self.assertRaises(IncorrSide):
            get_triangle_type(0, 1, 1)

    def test_invalid_sides_2(self):
        with self.assertRaises(IncorrSide):
            get_triangle_type(3, -4, 5)

    def test_invalid_sides_3(self):
        with self.assertRaises(IncorrSide):
            get_triangle_type(3, 4, 10)


if __name__ == "__main__":
    unittest.main