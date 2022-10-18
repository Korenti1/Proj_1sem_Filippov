try:
    x = int(input("Введите число: "))
    if x > 100000000000000000000000000:
        print('Слишком большое значение')
    else:
        if x > 0: print(x + 1)
        if x < 0: print(x - 2)
        if x == 0: print("Число 0")
except ValueError:
    print('Error')
