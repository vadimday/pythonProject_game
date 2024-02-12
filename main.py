def main():
    introduction = intro()
    board = create_grid()
    pretty = printPretty(board)
    symbol_1, symbol_2 = sym()
    full = isFull(board, symbol_1, symbol_2)

def intro():
    print("\n")
    print("\n")
    input("Нажмите enter.")
    print("\n")

def create_grid():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board

def sym():
    symbol_1 = input(" x или 0? ")
    if symbol_1 == "x":
        symbol_2 = "O"
        print("Игрок 2, ты 0. ")
    else:
        symbol_2 = "x"
        print("Игрок 2, ты x. ")
    input("Нажмите enter.")
    print("\n")
    return (symbol_1, symbol_2)

def startGamming(board, symbol_1, symbol_2, count):
    if count % 2 == 0:
        player = symbol_1
    elif count % 2 == 1:
        player = symbol_2
    print("Игрок " + player + ", твоя очередь. ")
    row = int(input("Выберите строку:"
    "[верхняя строка:0, средняя строка:1, нижняя строка:2]"))
    column = int(input
                 ("Выберите столбец:"
                  "[левый столбец:0, средний столбец:1, правый столбец:2]"))
    while (row > 2 or row < 0) or (column > 2 or column < 0):
        outOfBoard(row, column)
        row = int(input("Выберите строку[верхняя строка:"
    "[введите 0, средняя строка: 1, нижняя строка:2]"))
        column = int(input("Выберите столбец:"
    "[левый столбец:0, средний столбец:1, правый столбец:2]"))
    while (board[row][column] == symbol_1) or (board[row][column] == symbol_2):
        filled = illegal(board, symbol_1, symbol_2, row, column)
        row = int(input("Выберите строку[верхняя строка:"
    "[введите 0, средняя строка:1, нижняя строка:2]"))
        column = int(input("Выберите столбец:"
            "[левый столбец: 0, средний столбец:1, правый столбец:2]"))
    if player == symbol_1:
        board[row][column] = symbol_1

    else:
        board[row][column] = symbol_2
    return (board)
def isFull(board, symbol_1, symbol_2):
    count = 1
    winner = True
    while count < 10 and winner == True:
        gaming = startGamming(board, symbol_1, symbol_2, count)
        pretty = printPretty(board)

        if count == 9:
            print("Игра закончена!!")
            if winner == True:
                print("Ничья ")
        winner = isWinner(board, symbol_1, symbol_2, count)
        count += 1
    if winner == False:
        print("Игра закончена!")
    report(count, winner, symbol_1, symbol_2)

def outOfBoard(row, column):
    print("Выберите другой.")
def printPretty(board):
    rows = len(board)
    cols = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board
def isWinner(board, symbol_1, symbol_2, count):
    winner = True
    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
            winner = False
            print("Игрок " + symbol_1 + ", выиграл")

        elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            winner = False
            print("Игрок " + symbol_2 + ", выиграл")
    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
            winner = False
            print("Игрок " + symbol_1 + ", выиграл")
        elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
            winner = False
            print("Игрок " + symbol_2 + ", выиграл")
    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        winner = False
        print("Игрок " + symbol_1 + ", выиграл")

    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        winner = False
        print("Игрок  " + symbol_2 + ", выиграл")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
        winner = False
        print("Игрок " + symbol_1 + ", выиграл")
    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = False
        print("Игрок" + symbol_2 + ", выиграл")
    return winner

def illegal(board, symbol_1, symbol_2, row, column):
    print("Выбранный вами квадрат уже заполнен. Выберите другой.")
def report(count, winner, symbol_1, symbol_2):
    print("\n")
    if (winner == False) and (count % 2 == 1):
        print("Победитель : Игрок " + symbol_1 + ".")
    elif (winner == False) and (count % 2 == 0):
        print("Победитель : Игрок " + symbol_2 + ".")
    else:
        print("Ничья играйте заново! ")

main()
