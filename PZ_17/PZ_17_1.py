"""Создайте класс "Животное" с атрибутами "имя" и "вид". Напишите метод, который
выводит информацию о животном в формате "Имя: имя, Вид: вид"."""


class Animal:
  def __init__(self, name, kind):
    self.name = name
    self.kind = kind

  def info(self):
    print(f"Имя: {self.name}, Вид: {self.kind}")

lion = Animal('Лев', "Кошачьи")
lion.info()