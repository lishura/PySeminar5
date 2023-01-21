# 2.	Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


from random import randint, shuffle

candies = 121
candies_lim = 28


def bot_run(candies: int):
    if candies > 28:
        result = candies % candies_lim + 1
    else:
        result = candies
    return result


def motion(active_player):
    first, second = players
    return second if active_player == first else first


players = ['person', 'bot' if int(
    input('Будете играть с ботом: 1 - да, 0 - нет ')) else 'person2']
shuffle(players)

active_player = players[0]
print(f'Первый игрок - {players[0]}, второй игрок - {players[1]}')

while candies > 0:
    print(
        f'\nНа столе {candies} конфет, Вы можете взять от 1 до {candies_lim} конфет ')
    print(f'Ход игрока {active_player} ')

    if active_player == 'bot':
        get_candies = bot_run(candies)
        print(f'Бот взял {get_candies}')
    else:
        get_candies = int(input(f'Сколько конфет возьмет {active_player}? '))

    if get_candies not in range(1, candies_lim+1):
        print('Неверный ход! ')
    else:
        candies -= get_candies
        if candies > 0:
            active_player = motion(active_player)
        else:
            print(f'Игрок {active_player} выйграл!!!')
