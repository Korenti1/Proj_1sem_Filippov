# С помощью функций получить вертикальную и горизонтальную линии. Линия
# проводится многократной печатью символа. Заключить слово в рамку из
# полученных линий.
def get_horizontal_line():
    line = input("Введите символы, из которого будет состоять горизонтальная линия: ")
    return line


def get_vertical_line():
    line = ""
    for i in range(1):
        line = line + input("Введите 1 символ, из которого будет состоять вертикальная линия: ")
    return line


def main():
    word = input("Введите слово, которое надо поместить в рамку: ")
    horizontal = get_horizontal_line()
    vertical = get_vertical_line()
    print(horizontal)
    print(f"{vertical}" + f"{word}" + f"{vertical}")
    print(horizontal)


if __name__ == "__main__":
    main()
