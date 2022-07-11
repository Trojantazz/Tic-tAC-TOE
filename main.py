board_list = ["", "", "", "", "", "", "", "", ""]
turn = 1
game_over = False


def check_winner(mark):
    """ Checks board for three connecting marks """
    return ((board_list[0] == mark and board_list[1] == mark and board_list[2] == mark) or  # for row1

            (board_list[3] == mark and board_list[4] == mark and board_list[5] == mark) or  # for row2

            (board_list[6] == mark and board_list[7] == mark and board_list[8] == mark) or  # for row3

            (board_list[0] == mark and board_list[3] == mark and board_list[6] == mark) or  # for Col1

            (board_list[1] == mark and board_list[4] == mark and board_list[7] == mark) or  # for Col2

            (board_list[2] == mark and board_list[5] == mark and board_list[8] == mark) or  # for col3

            (board_list[0] == mark and board_list[4] == mark and board_list[8] == mark) or  # diagonal1

            (board_list[2] == mark and board_list[4] == mark and board_list[6] == mark))     # diagonal2


def next_round():
    """ Game flow control """
    global turn
    global board_list
    allowed_entries = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    square = input("Which square you would like to fill ? User a number from 1 to 9.\n")
    if square == "exit" or square not in allowed_entries:
        exit()
    else:
        square = int(square)
    if turn % 2 == 0:
        marker = "O"
    else:
        marker = "X"
    if board_list[square - 1] == "":
        board_list[square - 1] = marker
        board = f"{board_list[0]}       | {board_list[1]}     | {board_list[2]}\n - - - - - - - - - - -  \n" \
                f"{board_list[3]}       | {board_list[4]}     | {board_list[5]}\n - - - - - - - - - - - \n" \
                f"{board_list[6]}       | {board_list[7]}     | {board_list[8]}"
        print(board)
        turn += 1
    else:
        pass


def is_game_over():
    """ Function to check entries in board """
    global game_over
    mark = "X"
    player1_win = check_winner(mark)
    if player1_win:
        print("Player 1 Wins!")
        exit()
    mark = "O"
    player2_win = check_winner(mark)
    if player2_win:
        print("Player 2 Wins!")
        exit()
    if "" not in board_list:
        print("It's a draw.")
        game_over = True


while not game_over:
    """ While loop to keep game going as long as bool 'game_over'=False """
    next_round()
    is_game_over()
