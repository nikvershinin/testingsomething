print("*" * 20, " Крестики-нолики ", "*" * 20)

a = [1,2,3,4,5,6,7,8,9]                                             #список для хранения значений Х или О

def board(a):                                                       #фукция для постройки интерфейса
    for i in range(3):
        print("|", a[0+i*3], "|", a[1+i*3], "|", a[2+i*3], "|")
        print("-" * 13)

c = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]] #условия победы

board(a)
count = 0
while True:
    if count % 2 == 0:
        print ("Ход игрока №1. Кестики")
        b = int(input("В какую цифру поставить? \n"))
        if b >= 1 and b <= 9 and a[b-1] != "X" and a[b-1] != "0":   #проверка ввода
            a[b-1] = "X"
            d = [i for i in range(len(a)) if a[i] == "X"]
            if d in c:
                print("Игрок №1 'Креситики' выйграл")          #проверка победы
                break
            count += 1
            board(a)
        else:
            print("Клетка занята, выберите другую")
            board(a)
    else:
        print("Ход игрока №2. Нолики")
        b = int(input("В какую цифру поставить? \n"))
        if b >= 1 and b <= 9 and a[b - 1] != "0" and a[b-1] != "X": #проверка ввода
            a[b - 1] = "0"
            d = [i for i in range(len(a)) if a[i] == "0"]
            if d in c:
                print("Игрок №2 'Нолики' выйграл")#проверка победы
                break
            count += 1
            board(a)
        else:
            print("Клетка занята, выберите другую")
            board(a)
    if count >= 9:
        break
