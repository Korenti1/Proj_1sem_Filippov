""". Создайте класс "Фигура", который содержит метод расчета площади фигуры.
Создайте классы "Квадрат" и "Прямоугольник", которые наследуются от класса
"Фигура". Каждый класс должен иметь метод расчета площади собственной фигуры."""

from abc import abstractmethod


class Figure:
  def __init__(self, height, width):
    self.height = height
    self.width = width

  @abstractmethod
  def get_square(self):
    raise NotImplementedError
  
class Square(Figure):
  def __init__(self, height, width=None):
    super(Square, self).__init__(height, width=None)

  def get_square(self):
    return self.height ** 2

class Rectangle(Figure):
  def __init__(self, height, width):
    super(Rectangle, self).__init__(height, width)

  def get_square(self):
    return self.height * self.width
  
r = Rectangle(7,8)
r.get_square()

s = Square(1488)
s.get_square()