#. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
#последовательности из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Содержимое первого файла:
#Четные элементы:
#Произведение четных элементов:
#Минимальный элемент:
#Содержимое второго файла:
#Нечетные элементы:
#Количество нечетных элементов:
#Сумма нечетных элементов:

import random

file = open('file_one.txt', 'w', encoding='UTF-8')

file.write(' '.join([str(random.randint(-20, 20)) for _ in range(20)]))

file.close()

file = open('file_second.txt', 'w', encoding='UTF-8')

file.write(' '.join([str(random.randint(-20, 20)) for _ in range(20)]))

file.close()

file = open('file_one.txt', 'r', encoding='UTF-8')

raw_data = file.read().split(' ')
data = [int(i) for i in raw_data]
p = 1
for i in list(filter(lambda x: x%2==0, data)):
  p*=i

file.close()

file = open('file_second.txt', 'r', encoding='UTF-8')

sec_raw_data = file.read().split(' ')
sec_data = [int(i) for i in sec_raw_data]

file.close()

file = open('final_file.txt', 'w', encoding='UTF-8')

print(f'Содержимое первого файла: {data}', file=file)
print(f'Четные элементы: {list(filter(lambda x: x%2==0, data))}', file=file)
print(f'Произведение четных элементов: {p}', file=file)
print(f'Минимальный элемент: {min(data)}', file=file)

print(f'Содержимое второго файла: {sec_data}', file=file)
print(f'Нечетные элементы: {list(filter(lambda x: x%2!=0, sec_data))}', file=file)
print(f'Количество нечетных элементов: {len(list(filter(lambda x: x%2!=0, sec_data)))}', file=file)
print(f'Сумма нечетных элементов: {sum(data)}', file=file)

file.close()