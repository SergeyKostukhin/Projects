def greet():
    print('Приветствуем Вас в игре крестики-нолики')
    print('выберете координаты хода x и y')

greet()

field = [[" "] * 3 for i in range(3)]
def show():
    print (f" 0 1 2")
    for i in range(3):
        row_info = " ".join(field[i])
        print(f"{i} {row_info}")

def ask():
    while True:
        x, y = map(int, input("Ваш ход:  ").split())
        if 0 <= x <= 2 and 0 <= y <= 2 :
            if field [x][y] == " " :
                return x, y
            else:
                print("Клетка занята")
        else:
            print("Нет такой клетки")

def win_check():

    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))

    for cord in win_cord:

        symbols = []

        for c in cord:
            symbols.append(field[c[0]][c[1]])

        if symbols == ["X", "X", "X"]:
            print("Выиграли крестики")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграли нолики")
            return True

    return False
num = 0
while True:
        num += 1

        show()

        if num % 2 == 1:
            print("Ходит крестик")
        else:
            print("Ходит нолик")

        x, y = ask()

        if num % 2 == 0:
            field[x][y] = "0"
        else:
            field[x][y] = "X"

        if win_check():
            break

        if num == 9:
            print("Ничья")
            break





