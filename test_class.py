import pytest
from triangle_class import Triangle, IncorrSide

def test_triangle_creation_positive():
    triangle = Triangle(3, 4, 5)
    assert triangle.a == 3
    assert triangle.b == 4
    assert triangle.c == 5

def test_triangle_creation_negative():
    with pytest.raises(IncorrSide):
        Triangle(1, 2, 3)
    with pytest.raises(IncorrSide):
        Triangle(0, 1, 2)
    with pytest.raises(IncorrSide):
        Triangle(1, 2, 5)

def test_triangle_type():
    triangle1 = Triangle(2, 4, 3)
    assert triangle1.triangle_type() == "неравносторонний"
    triangle2 = Triangle(5, 5, 5)
    assert triangle2.triangle_type() == "равносторонний"
    triangle3 = Triangle(7, 7, 10)
    assert triangle3.triangle_type() == "равнобедренный"

def test_perimeter():
    triangle = Triangle(3, 4, 5)
    assert triangle.per() == 12
