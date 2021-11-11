# print ("*" * 20, "Игра морской бой", "*" * 20)
#
#
#
#
class Dot:        # класс точки с координатами, х и у.
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other and self.y == other


    def __repr__(self):
        return f"({self.x}, {self.y})"

class Ship:   #описание класса корабля
    def __init__(self, fst_dot, length, hor): #характеристики корабля (первая точка, длина, положение(1 - гориз, 0 - верт)
        self.fst_dot = fst_dot
        self.length = length
        self.hor = hor

    @property
    def ship_dots(self):    # список точек корабля
        ship_list = []  #создаем общий список точек для каждого корабля
        for i in range(self.length):
            cur_x = self.fst_dot.x
            cur_y = self.fst_dot.y

            if self.hor == 1:
                cur_x += i

            else:
                cur_y += i
            ship_list.append(Dot(cur_x, cur_y))
        return ship_list

    def shoot(self, shot):      #
        return shot in self.ship_dots

class GamingBoard:
    def __init__(self, hid=False, size=6):
        self.hid = hid
        self.size = size

        self.count = 0
        self.board = [[" "] * size for i in range(size)]  # хранение входных данных

        self.busy = []      # для хранения информации о занятых точках в результате выстрела, повторного выстрела
        self.ships = []     # для хранения информации о кораблях

    def add_ship(self, ship):
        for d in ship.ship_dots:
            self.board[d.x][d.y] = "■"
            self.busy.append(d)
        self.ships.append(ship)
        self.contur(ship)


    def contur(self, ship):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1),
        ]
        near1 = []
        for d in ship.ship_dots:
            print(d)
            for dx, dy in near:
                print(dx, dy)
                cur = Dot(d.x + dx, d.y + dy)
                print(cur)
                if cur not in near1:
                    print(True)
                    if cur not in ship.ship_dots:
                        near1.append(cur)
                    print(near1)
                else:
                    print(False)
        # self.busy.append([_ for _ in self.near1 if _ not in ship.ship_dots])
        # print(self.busy)
        # print(self.near1)

                # if (0 <= cur.x < self.size) and (0 <= cur.y < self.size) and cur not in self.busy:
                #
                #
                #
                #     self.board[cur.x][cur.y] = "."
                #     self.busy.append(cur)

    def show_board(self):   #отображение игрового поля
        print(f"   1   2   3   4   5   6  ")
        print("-" * 26)
        for i in range(self.size):
            row = " | ".join(self.board[i])
            if self.hid:    #условие для отображения пустого поля
                row = row.replace("■", " ")
            print(f"{i+1}| {row} |")
        print("-" * 26)





    # def ask_shoot():    #Запрос точки с координатами выстрела
    #     while True:
    #         try:
    #             x, y = map(int,input("Выберите кооордикаты выстрела через пробел(x y)").split())
    #             x -= 1
    #             y -= 1
    #         except ValueError:
    #             print("Вы ввели некорректные значения поля.\nПопробуйте еще раз")
    #         else:
    #             return x , y





#
# d = Dot(1,1)
# print(d)

# s = Ship(Dot(1,1), 3, 1)
b = GamingBoard(0)
s = Ship(Dot(1,1), 3, 0)
b.add_ship(s)
print(b.show_board())
print(s.ship_dots)
print()
