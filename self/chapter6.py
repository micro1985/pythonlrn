X = "X"
O = "O"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9


def display_instruct():
    """Выводит на экран инструкцию для игрока."""
    print(
        """
        Добро пожаловать на ринг грандиознейших интеллектуальных состязаний всех времен.
        Твой мозг и мой процессор сойдутся в схватке за доской игры "Крестики-нолики".
        Чтобы сделать ход. введи число от О до 8. Числа однозначно соответствуют полям
        доски - так. как показано ниже:
        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8
        Приготовься к бою. жалкий белковый человечишка. Вот-вот начнется решающее сражение.
        \n
        ----------------------------------------------------------------------------------
        \n"""
        )


def ask_yes_no(question):
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Просит ввести число"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """Определяет чей первый ход"""
    go_first = ask_yes_no("Человек, ты будешь первым ходить? (y/n): ")
    if go_first == "y":
        print("\nЧеловек играет крестиками.")
        human = X
        computer = O
    else:
        print("\nЧеловек играет ноликами.")
        human = O
        computer = X
    return computer, human


def new_board():
    """Создаёт новую доску"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Отображает доску на экране"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8])
    print("\t", "---------")


def legal_moves(board):
    """Создаёт список доступных ходов"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Определяет победителя"""
    WAYS_TO_WIN = ((0,1,2),
                   (3,4,5),
                   (6,7,8),
                   (1,4,7),
                   (2,5,8),
                   (0,3,6),
                   (0,4,8),
                   (2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row]0]
            return winner
        if EMPTY not in board:
            return TIE
    return None


def human_move(board, human):
    """Получает ход человека"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. выбери одно из полей (0-8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nСмешной человек. Поле уже занято. выбери другое.\n")
    print("Ладно...")
    return move




display_instruct()
display_board(new_board())

print("Надеюсь, теперь смысл игры ясен.")
input("\n\nНажмите Enter дял выхода")
