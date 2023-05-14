_a: int = 15


def square_perimiter(a: int = _a) -> float:
    """периметр квадрата"""
    return a * 4


def square_area(a: int = _a) -> float:
    """площадь квадрата"""
    return a ** 2


if __name__ == "__main__":
    square_perimiter()
    square_area()
