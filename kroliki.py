# -*- coding: utf-8 -*-

field = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def draw_field(field):
    print("-------------")
    for i in range(3):
        print("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
        print("-------------")

def move_input(player_side):
    move = False
    while not move:
        player_move = input("На клетку с каким номером ставите " + player_side +"?  ")
        try:
            player_move = int(player_move)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_move >= 1 and player_move <= 9:
            if (str(field[player_move-1]) not in "XO"):
                field[player_move-1] = player_side
                move = True
            else:
                print("Поле с этим номером уже занято")
        else:
            print("Введите номер свободного поля чтобы сделать на его месте свой ход.")

def check_win(field):
    win_combinations = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for side in win_combinations:
        if field[side[0]] == field[side[1]] == field[side[2]]:
            return field[side[0]]
    return False

def main(field):
    counter = 0
    finish = False
    while not finish:
        draw_field(field)
        if counter % 2 == 0:
            move_input('X')
        else:
            move_input('O')
        counter += 1
        if counter > 4:
            current_player = check_win(field)
            if current_player:
                print(current_player, 'выиграл!!!')
                finish = True
                break
            if counter == 9:
                print("Ничья, друзья).")
                break
    draw_field(field)

main(field)
