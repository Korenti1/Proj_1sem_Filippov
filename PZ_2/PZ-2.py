#Дано целое число, большее 999. Используя одну операцию деления нацело и одну операцию взятия остатка от деления, найти цифру, соответствующую разряду тысяч в записи этого числа.

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