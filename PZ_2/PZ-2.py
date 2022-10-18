try:
    x = int(input('Введите число'))
    if x < 999:
        print('Введено некорректное число')
    else:
        y = x // 1000
        n = y % 10
        print(n)
except ValueError:
    print('Error')