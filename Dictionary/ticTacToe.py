def printBoard(board):
    print(f"{board['top-L']} | {board['top-M']} | {board['top-R']}")
    print(f"--+---+--")
    print(f"{board['mid-L']} | {board['mid-M']} | {board['mid-R']}")
    print(f"--+---+--")
    print(f"{board['low-L']} | {board['low-M']} | {board['low-R']}")

board = {'top-L': '', 'top-M': '', 'top-R': '', 
        'mid-L': '', 'mid-M': '', 'mid-R': '',
        'low-L': '', 'low-M': '', 'low-R': ''}

turn = 'X'
for _ in range(9):
    printBoard(board)
    print("Enter your move:")
    print(board.keys())
    move = input()
    board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'