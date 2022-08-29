import random

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

#player_input()

def place_marker(board, marker, postion):
    board[-postion] = marker

#place_marker(test_board,'$',8)
#display_board(test_board)

def win_check(board, mark):
    winning_list = list(mark*3)
    if board[1:4] == winning_list:
        return True
    elif board[4:7] == winning_list:
        return True
    elif board[7:10] == winning_list:
        return True
    elif [board[1], board[4], board[7]] == winning_list:
        return True
    elif [board[2], board[5], board[8]] == winning_list:
        return True
    elif [board[3], board[6], board[9]] == winning_list:
        return True
    elif [board[1], board[5], board[9]] == winning_list:
        return True
    elif [board[3], board[5], board[7]] == winning_list:
        return True
    else:
        return False

#print(win_check(test_board, 'O'))

def choose_first():
    choice = random.randInt(1, 2)
    if choice == 1:
        return "Player1"
    else:
        return "Player2"

def space_check(board, position):
    return board[-position] == ' ' or position in range(0,9)

def player_choicer(board):
    choice = 10

    while choice not in range(0,9) and not space_check(board, choice):
        choice = input("Enter the position 1-9 you want to place your marker in:")

        if choice not in range(0,9):
            print("Wrong input! Try again")
        if not space_check(board, choice):
            print("This place is already taken. Try again")