import random

status = {'unknown dot': u"\u25a2", 'in ship dot': u'\u25A0', 'desired dot': u'\u2612', 'contour dot': u'\u25A3'}

board_size = 6
fleet = [2, 1]
activ_ships = []
used_dots = []
hid = False
move = True

class BoardOutException(Exception):
    pass
class BoardPlacementxception(Exception):
    pass

class Board:                            #класс Board — игровая доска. Доска описывается параметрами:
    def __init__(self, board=[]):
        self.hid = hid                  #Параметр hid типа bool — информация о том, нужно ли скрывать корабли на доске
        self.board = board              #Двумерный список, в котором хранятся состояния каждой из клеток.
        self.activ_ships = activ_ships  #Список кораблей доски. #Количество живых кораблей на доске.

    def add_ship(self, ship):   #Метод add_ship, который ставит корабль на доску (если ставить не получается, выбрасываем исключения).
        ship.dots()
        for _ in range(ship.l):
            if not ship.ship_dots[_].out():
                BoardOutException
                print('Клетки ворабля не должны выходить за пределы доски.')
                break
        for _ in range(ship.l):
            if self.board[ship.ship_dots[_].x-1][ship.ship_dots[_].y-1]==status.get('contour dot'):
                BoardPlacementxception
                print('Кораблям нельзя соприкасаться ни бортами, ни углами')
                break
        else:
            self.board[ship.n.x - 1][ship.n.y - 1] = status.get('in ship dot')
            for _ in range(ship.l):
                if ship.v:
                    self.board[ship.n.x - 1 + _][ship.n.y - 1] = self.board[ship.n.x - 1][ship.n.y - 1]
                else:
                    self.board[ship.n.x - 1][ship.n.y - 1 + _] = self.board[ship.n.x - 1][ship.n.y - 1]
            self.activ_ships.append(Ship(Dot(ship.n.x, ship.n.y), ship.l, ship.v))


    def contour(self):  #Метод contour, который обводит корабль по контуру.
        u = Ship
        contour_dots =[]
        for u in self.activ_ships:
            for _ in u.dots():
                contour_dots.append(Dot(_.x, _.y-1)) #лево
                contour_dots.append(Dot(_.x-1, _.y-1)) #верхо-лево
                contour_dots.append(Dot(_.x-1, _.y)) #верх
                contour_dots.append(Dot(_.x-1, _.y+1))  # верх-право
                contour_dots.append(Dot(_.x, _.y+1))  # право
                contour_dots.append(Dot(_.x+1, _.y+1)) #низ-право
                contour_dots.append(Dot(_.x+1, _.y))  # низ
                contour_dots.append(Dot(_.x+1, _.y-1))  # низ-лево
        unique_contour_dots=[]
        for _ in range(len(contour_dots)):
            if contour_dots[_] not in unique_contour_dots:
                unique_contour_dots.append(contour_dots[_])
        for _ in range(len(unique_contour_dots)):
            if unique_contour_dots[_].out():
                if self.board[unique_contour_dots[_].x-1][unique_contour_dots[_].y-1] == status.get('in ship dot'):
                    continue
                else:
                    self.board[unique_contour_dots[_].x-1][unique_contour_dots[_].y-1]=status.get('contour dot')

    def print(self):
        screen_board = self.board
        t = ['  ']
        for x in range(board_size):
            t.append(str(x+1))
        print('   карта ')
        print('|'.join(t))
        for y in range(board_size):
            print(y+1, '|'.join(screen_board[y]))

class Dot:                          # класс Dot — класс точек на поле. Каждая точка описывается параметрами:
    def __init__(self, x=0, y=0):
        self.x = x                  #Координата по оси x
        self.y = y                  #Координата по оси y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'Dot: {self.x,self.y}'

    def out(self):  #Метод out, который для точки возвращает True, если точка выходит за пределы поля, и False, если не выходит.
        if 1 <= self.x <= board_size and 1 <= self.y <= board_size:
            return True
        else:
            return False

class Ship:
    def __init__(self, n, l, v):
        self.n = Dot(n.x, n.y)          #Точка, где размещён нос корабля
        self.l = l                      #Длина.
        self.v = v                      #Направление корабля (вертикальное/горизонтальное).
        self.ship_dots=[]               #Метод dots, который возвращает список всех точек корабля
        self.life = int                 #сколько точек ещё не подбито

    def __str__(self):
        return str(self.n.x)+' '+str(self.n.y)+' '+str(self.l)+' '+str(self.v)

    def dots(self):                     #Метод dots, который возвращает список всех точек корабля
        self.ship_dots=[self.n]
        for _ in range(self.l-1):
            if self.v:
                self.ship_dots.append(Dot(self.n.x+1+_, self.n.y))
            else:
                self.ship_dots.append(Dot(self.n.x, self.n.y+1+_))
        return self.ship_dots

class Player:   #Класс Player — класс игрока в игру (и AI, и пользователь),Игрок описывается параметрами:
    def __init__(self, own_board, enemy_board):
        self.own_board = own_board          #Собственная доска (объект класса Board)
        self.enemy_board = enemy_board      #Доска врага.

    def ask(self):  #ask — метод, который «спрашивает» игрока, в какую клетку он делает выстрел.
        pass

    def move(self):
        pass

class AI(Player):
    def ask(self):
        pass
    pass

class User(Player):

    def ask(self):
        x = int(input('Введите координату по вертикали (номер строчки, считая сверху вниз) и нажмите Enter: '))
        y = int(input('Введите координату по горизонтали (номер столбика, считая слева направо) и нажмите Enter: '))
        return Dot(x, y)

class Game:
    pass
#Игра:

#While Game:

    b_pl = Board()
    b_pl.board = [[status.get('unknown dot') for y in range(board_size)] for x in range(board_size)]

    b_ai = Board()
    b_ai.board = [[status.get('unknown dot') for y in range(board_size)] for x in range(board_size)]

    player = User(b_pl, b_ai)
    ai = AI(b_ai, b_pl)

# Расстановка кораблей:
    for _ in fleet:
        print('Установка', _, '-палубника. Задайте верхнюю левую точку.')
        n = player.ask()
        v = int(input('Ваш корабль должен расположиться вертикально? (1 = да, 0 = нет. Для однопалубника: введите 0 или 1 без разницы.):'))
        s = Ship(n, _, v)
        try:
            player.own_board.add_ship(s)
        except:
            BoardOutException
            print('Клетки kорабля не должны выходить за пределы доски.')
        player.own_board.contour()
        player.own_board.print()






print(status)
