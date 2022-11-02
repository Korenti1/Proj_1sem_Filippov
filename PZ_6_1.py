# Дан целочисленный список размера N, не содержащий одинаковых чисел.
# Проверить, образуют ли его элементы арифметическую прогрессию. Если образуют,
# то вывести разность прогрессии, если нет — вывести 0.
import random

n = list()
for i in range(random.randint(6, 20)):
    n.append(random.randint(1, 10))

tek_list = list(set(n))
try:
    diff = tek_list[2] - tek_list[1]
    i = 2
    while i < len(tek_list):
        if (tek_list[i] - tek_list[i - 1] > diff) or (tek_list[i] - tek_list[i - 1] < diff):
            diff = 0
        i += 1

    print(f"Разница арифмитической прогрессии равна {diff}")
except Exception as e:
    print("Возникла ошибка при генерации списка. Перезапустите программу!")
