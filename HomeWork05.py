# Урок 5. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension

# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.

# 120 21 ---> 99 бот 4 -> 95 .... бот --->29 --> 27 >> 2конф

# a) Добавьте игру против бота

# # Доп b) Подумайте как наделить бота ""интеллектом"" (Теория игр)

# from random import randint

# count = 120
# max_taken = 28
# winner_human = False

# while count != 0:
#     win_step = count % (max_taken + 1)
#     human = int(input('Ваш ход: '))

#     if human <= 0 or human > 28:
#         print('Неверный ход, введите другое число', '\n')
#         continue
#     elif human == win_step:
#         count -= human
#         print('Осталось: ', count, '\n')
#         if count == 0:
#             winner_human = True
#             break
#         bot = randint(1, 28)
#     else:
#         count -= human
#         print('Осталось: ', count, '\n')
#         win_step = count % (max_taken + 1)
#         bot = win_step

#     print('Ход бота: ', bot)
#     count -= bot
#     print('Осталось: ', count, '\n')

# print('Вы выиграли!' if winner_human else 'Выиграл бот :(', '\n')

#############################################################################
# 2) Создайте программу для игры в ""Крестики-нолики"" человек vs человек.
# 1 | 2 | X
# 4 | X | O
# X | 8 | O

# board = list(range(1,10)) # игровое поле
# def print_board(board):
#     print ("-" * 13)  
#     for i in range(3):
#         print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#         print ("-" * 13)

# print_board(board)

# # Индексы клеток
# win_combo = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

# def getWinner(state, combo):
#     for(x,y,z) in combo:
#         if state[x] == state[y] and state[y] == state[z] and (state[x] == 'X' or state[x] == 'O'):
#             return state[x]
#     return ''

# def game(board):
#     current_step = 'X'
#     while (getWinner(board, win_combo) == ''):
#         index = int(input(f'Введите номер клетки {current_step}?'))
#         board[index-1] = current_step

#         print_board(board)

#         winner = getWinner(board, win_combo)
#         if winner != '':
#             print(f'Вы победили, {winner}!')
#         current_step ='X' if current_step == 'O' else 'O'

# game(board)

#############################################################################
# 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные данные хранятся в отдельных текстовых файлах.

# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"
# Вывод: stroka = "aaabbbbccbbb"

def coder(line: str) -> str:
    encoding_line = ''
    count = 1
    temp = line[0]
    for i in range(1, len(line)):
        if line[i] == temp:
            count += 1
        else:
            encoding_line += str(count) + temp
            temp = line[i]
            count = 1
        # кодировка последнего элемента
        if i == (len(line) - 1):
            encoding_line += str(count) + temp
    return encoding_line


def decoder(line: str) -> str:
    decoder_line = ''
    for i in range(0, len(line), 2):
        decoder_line += line[i + 1] * int(line[i])
    return (decoder_line)

line = 'FFFGGGOOOTFFLLE'

print("Исходная строка: ", line)
code_line = coder(line)
print("Закодированная строка: ", code_line)
print("Декодированная строка: ", decoder(code_line))