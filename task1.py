# 1.	Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

from random import sample


def words_list(count:int, model:str = 'абв'):
    my_list = []
    for i in range(count):
        word = sample(model,3)
        my_list.append("".join(word))
    return ' '.join(my_list)


def cut_list(words_list:str):
    return ' '.join(i for i in words_list.split() if i != 'абв')

num = int(input('Введите количество слов '))
elements = words_list(num)
print(elements)
print(cut_list(elements))