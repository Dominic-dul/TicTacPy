from dis import dis


print("Hello")

def display_board(board):
    for tiles in range(0, len(board)-1, 3):
        print(board[tiles+1:tiles+4])

test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
#display_board(test_board)

def player_input():
    player1 = '#'
    player2 = None

    while player1 not in ['O', 'X']:
        player1 = input("Player1, please select which one are you, 'X' or 'O':")

        if player1 not in ['O', 'X']:
            print("Incorrect input! Please try again")

    if player1 == 'O':
        player2 = 'X'
    else:
        player2 = 'O'

    print(f"Player1 is {player1}, Player2 ir {player2}")

player_input()