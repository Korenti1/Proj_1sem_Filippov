from math import pi

_default_radius: int = 5


def circle_perimiter(radius: int = _default_radius) -> float:
    """периметр круга"""
    return 2 * pi * radius


def circle_area(radius: int = _default_radius) -> float:
    """площадь круга"""
    return pi * (radius ** 2)


if __name__ == "__main__":
    circle_perimiter()
    circle_area()
