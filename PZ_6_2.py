# Дан список A размера N. Сформировать новый список B того же размера, элементы
# которого определяются следующим образом:
# BK = 2*AK, если AK < 5,
# AK/2 в противном случае.
import random

a = list()
b = list()
for i in range(random.randint(1, 20)):
    a.append(random.randint(1, 100))

try:
    for i in a:
        if i < 5:
            b.append(2 * i)
        else:
            b.append(i / 2)

    print(b)
except Exception as e:
    print("Возникла ошибка! Перезапустите программу")
