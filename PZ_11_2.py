# Из предложенного текстового файла (text18-23.txt) вывести на экран его содержимое,
#количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
#который поместить текст в стихотворной форме предварительно заменив символы верхнего
#регистра на нижний.

import string

file = open('text18-23.txt', encoding="utf8")

data = file.readlines()
count = 0
for i in ' '.join(data):
   if i in string.punctuation:
     count+=1

file.close()

print(f'Исходное стихотворение: {"".join(data)}')
print(f'Количество знаков препинания: {count}')

file = open('text18-23-final.txt', 'w' ,encoding="utf8")

file.write(''.join(data).lower())

file.close()