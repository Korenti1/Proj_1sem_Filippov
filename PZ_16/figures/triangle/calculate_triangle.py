from math import sqrt

_a, _b, _c = 7, 2, 8


def triangle_perimiter(a: int = _a, b: int = _b, c: int = _c) -> float:
    """периметр треугольника"""
    return a + b + c


def triangle_area(a: int = _a, b: int = _b, c: int = _c) -> float:
    """площадь треугольника"""
    p = triangle_perimiter(a, b, c)
    return sqrt(p * (p-a) * (p-b) * (p-c))


if __name__ == "__main__":
    triangle_perimiter()
    triangle_area()
