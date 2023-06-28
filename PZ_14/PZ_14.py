"""Из исходного текстового файла (ip_address.txt) из раздела «Зарезервированные
адреса» перенести в первый файл строки с ненулевыми первым и вторым октетами,
а во второй – все остальные. Посчитать количество полученных строк в каждом
файле."""
import re

with open('ip_address.txt', 'r', encoding='utf-8') as file:
  data = file.read()[535:]

anyone_address = re.findall("\d+\.\d+\.\d+\.\d+.\d+", data)
adresses_null = [i for i in re.sub("[0-9]+\.[1-9]+\.\d+\.\d+.\d+", '', '\n'.join(anyone_address)).split('\n') if i != '']
adresses_not_null = [i for i in re.findall("[1-9]+\.[1-9]+\.\d+\.\d+.\d+", data) if i != '']

with open('not_null_adresses.txt', 'w', encoding='utf-8') as file:
  file.writelines('\n'.join(adresses_not_null))

with open('null_adresses.txt', 'w', encoding='utf-8') as file:
  file.writelines('\n'.join(adresses_null))

with open('not_null_adresses.txt', 'r', encoding='utf-8') as file:
  string_length_not_null = len(file.readlines())

with open('null_adresses.txt', 'r', encoding='utf-8') as file:
  string_length_null = len(file.readlines())


print(f'{string_length_not_null} - кол-во строк в первом файле \n{string_length_null} - кол-во строк в втором файле')
