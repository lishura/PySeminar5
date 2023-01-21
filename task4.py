# 4.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from itertools import groupby
from os import path

def rle_contraction(text = 'text_file.txt', code = 'code_file.txt'):
    if path.exists(text):
        with open(text, 'r') as file_1, \
                open(code,'a') as file_2:
            for i in file_1:
                file_2.write(''.join([f'{len(list(v))}{ch}' for ch,v in groupby(i)]))
    else:
        print('Файлы отсутствуют! ')


def rle_restore(file):
    if path.exists(file):
        with open(file, 'r') as f:
            for i in f:
                elements = [''.join(v) for k, v in groupby(i.strip(), key=str.isdigit)]
                print(''.join([f'{int(elements[i])*elements[i+1]}' for i in range(0, len(elements), 2)]))
    else:
        print('Файлы отсутствуют! ')


rle_contraction('text_file.txt', 'code_file.txt')
rle_restore('code_file.txt')
