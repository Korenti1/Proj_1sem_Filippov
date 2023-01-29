#В матрице найти максимальный положительный элемент, кратный 4
from random import randint

n = int(input())

matrix = [[randint(-20, 20) for _ in range(n)] for _ in range(n)]

print(matrix)

print(sum(matrix, []))

print(max(list(filter(lambda x: x%4 and x > 0, sum(matrix, [])))))