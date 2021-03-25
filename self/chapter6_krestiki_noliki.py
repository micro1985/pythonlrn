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
            winner = board[row[0]]
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


def computer_move(board, computer, human):
    """Компьютер делает ход"""
    # Создаём рабочую копию доски, т.к. функция будет менять некоторые значения в списке
    board = board[:]
    # Поля от лучшего к худшему
    BEST_MOVES = (4,0,2,6,8,1,3,5,7)
    print("Я выберу поле номер", end=" ")

    for move in legal_moves(board):
        board[move] = computer
    # Если следующим ходом подеждает комп - выбираем этот ход
        if winner(board) == computer:
            print(move)
            return move
    # выполнив проверку отменим внесенные изменения
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human
    # Если следующим ходом побеждает человек - блокируем
        if winner(board) == human:
            print(move)
            return move
    # выполнив проверку отменим внесенные изменения
        board[move] = EMPTY
            
    # Т.к. дошли до сюда - то выбираем лучший ход для компа
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """Осуществляет переход хода"""
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    """Поздравляет победителя"""
    if the_winner != TIE:
        print("Три", the_winner, "в ряд!\n")
    else:
        print("Ничья!\n")

    if the_winner == computer:
        print("Kaк я и предсказывал. победа в очередной раз осталась за м~ой. \n" \
        "Вот еще один довод в пользу того. что компьютеры превосходят людей решительно во всем")
    elif the_winner == human:
        print("O нет. этого не может быть! Неужели ты как-то сумел перехитрить меня. белковый? \n" \
        "Клянусь: я. компьютер. не допущу этого больше никогда!")
    elif the_winner == TIE:
        print("Teбe несказанно повезло. дружок: ты сумел свести игру вничью")


def main():
    display_instruct()
    computer, human = pieces()
    turn =X
    board = new_board()
    display_board(new_board())
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


main()
input("\n\nНажмите Enter дял выхода")
