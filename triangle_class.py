
from triangle_func import IncorrSide

class Triangle:
    def __init__(self, a: float, b: float, c: float):

        if not (a > 0 and b > 0 and c > 0):
            raise IncorrSide("Стороны треугольника должны быть положительными")
        if a + b <= c or a + c <= b or b + c <= a:
            raise IncorrSide("Стороны треугольника не могут образовывать треугольник")
        
        self.a = a
        self.b = b
        self.c = c

    def triangle_type(self) -> str:

        if self.a == self.b == self.c:
            return "равносторонний"
        elif self.a == self.b or self.b == self.c or self.c == self.a:
            return "равнобедренный"
        else:
            return "неравносторонний"

    def per(self) -> float:
        return self.a + self.b + self.c

