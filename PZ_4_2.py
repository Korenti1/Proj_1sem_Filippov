# Даны целые положительные числа N и K. Используя только операции сложения и
# вычитания, найти частное от деления нацело N на K, а также остаток от этого деления.
def check() -> int:
    num = input("Введите пожалуйста число: ")
    while type(num) != int:
        try:
            return int(num)
        except ValueError:
            print("Введите число снова!")
        num = input()


n = check()
k = n + 1

while k > 0:
    if k ** 2 > n:
        k -= 1
    else:
        break

print(f"Наибольшее целое число, квадрат которого меньше числа n - {k}")
