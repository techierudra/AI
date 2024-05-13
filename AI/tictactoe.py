def tic_tac_toe():
    board = [' '] * 9
    player = 'X'
    while True:
        print(' '.join(board[0:3]))
        print(' '.join(board[3:6]))
        print(' '.join(board[6:9]))
        print(f"Player {player}, enter your move (1-9):")
        move = int(input()) - 1
        if board[move] != ' ':
            print("Invalid move, try again.")
            continue
        board[move] = player
        if (board[0] == board[1] == board[2] != ' ' or
            board[3] == board[4] == board[5] != ' ' or
            board[6] == board[7] == board[8] != ' ' or
            board[0] == board[3] == board[6] != ' ' or
            board[1] == board[4] == board[7] != ' ' or
            board[2] == board[5] == board[8] != ' ' or
            board[0] == board[4] == board[8] != ' ' or
            board[2] == board[4] == board[6] != ' '):
            print(f"Player {player} wins!")
            break
        player = 'O' if player == 'X' else 'X'
        if ' ' not in board:
            print("It's a draw.")
            break

tic_tac_toe()
