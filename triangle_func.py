from math import sqrt

class IncorrSide(Exception):
    pass

def get_triangle_type(a: float, b: float, c: float) -> str:
    

    if not (a > 0 and b > 0 and c > 0):
        raise IncorrSide("Стороны положительные! должны быть:)")
    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrSide("Стороны треугольника не могут образовывать треугольник")
    
    if a == b == c:
        return "равносторонний"
    elif a == b or b == c or c == a:
        return "равнобедренный"
    else:
        return "неравносторонний"


 

 

 

 

 

 

 

 

 

 

 