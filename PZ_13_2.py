#В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в
#2 раза.
from random import randint

n = int(input())

matrix = [[randint(-20, 20) for _ in range(n)] for _ in range(n)]

for i in matrix:
  print(*i, sep='\t')

new_m = []
for i, v in enumerate(matrix):
  new_r = [2*x if i_x != i else x for i_x, x in enumerate(v)]
  new_m.append(new_r)

print()
for i in new_m:
  print(*i, sep='\t')