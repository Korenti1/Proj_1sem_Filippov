# Дано множество A из N точек (точки заданы своими координатами x, у). Среди всех
# точек этого множества, лежащих в первой или третьей четверти, найти точку,
# наиболее близкую к началу координат. Если таких точек нет, то вывести точку с
# нулевыми координатами.
# Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
# R = √(x2 – x1)2 + (у2 – y1)2
# .
# Для хранения данных о каждом наборе точек следует использовать по два списка: первый
# список для хранения абсцисс, второй — для хранения ординат.
import random
import math

x = list()
y = list()
dots_and_r = list()
for i in range(11):
    x.append(random.randint(-10, 10))
    y.append(random.randint(-10, 10))
try:
    for i in range(len(x)):
        if (x[i] > 0 and y[i] > 0) or (x[i] < 0 and y[i] < 0):
            R = math.sqrt(math.pow((0 + x[i]), 2) + math.pow((0 + y[i]), 2))
            dots_and_r.append((x[i], y[i], R))
    if dots_and_r is not None:
        r_list = list()
        for i in dots_and_r:
            r_list.append(i[2])
        min_r = min(r_list)
        for i in dots_and_r:
            if i[2] == min_r:
                print(f"Точка с координатами x={i[0]}, y={i[1]} является ближайшей к нулю")
    else:
        print(0, 0)
except Exception as e:
    print("Возникла ошибка на этапе генерации списка, перезапустите программу")
