# Даны целые положительные числа N и K. Найти сумму 1K + 2К + ... + NK
def check() -> int:
    num = input("Введите число: ")
    while type(num) != int:
        try:
            return int(num)
        except ValueError:
            print("Введи число снова!")
        num = input()


n = check()
k = check()
i = 1
sum = 0
while i <= n:
    print(f" i в степени k = {i ** k}")
    sum = sum + i ** k
    i += 1
print(f"Сумма ряда равна {sum}")
