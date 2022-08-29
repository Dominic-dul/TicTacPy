import random as ran

def display_board(board):
    for tiles in range(0, len(board)-1, 3):
        print(board[tiles+1:tiles+4])

def player_input():

    global player1
    global player2

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
    board[postion] = marker

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
    choice = ran.randint(1,2)
    if choice == 1:
        return "Player1"
    else:
        return "Player2"

def space_check(board, position):
    if position in range(0,10) and board[position] == ' ':
        return True
    else:
        return False

def player_choice(board):
    choice = 10

    while choice not in range(0,10) or not space_check(board, choice):
        choice = int(input("Enter the position 1-9 you want to place your marker in:"))

        if choice not in range(0,10):
            print("Wrong input! Try again")
        if not space_check(board, choice):
            print("This place is already taken. Try again")

    return choice

def full_board_check(board):
    for position in board:
        if position == ' ':
            return False

    return True

def replay():
    choice = '#'

    while choice not in ['Y', 'N']:
        choice = input("Do you want to replay the game? Type 'Y' if yes and 'N' otherwise")

        if choice not in ['Y', 'N']:
            print("Wrong input! Try again")

    return choice == 'Y'

player1 = '#'
player2 = '#'

print('Welcome to Tic Tac Toe!')

while True:
    game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    game_board_postions = ['$', 1, 2, 3, 4, 5, 6, 7, 8, 9]
    marker1 = '#'
    marker2 = '#'
    choice = None

    print("This is the positions to place in the board:")
    display_board(game_board_postions)

    player_input()

    starting_player = choose_first()
    second_player = None

    if starting_player == 'Player1':
        second_player = "Player2"
        marker1 = player1
        marker2 = player2
    else:
        second_player = "Player1"
        marker1 = player2
        marker2 = player1

    while not full_board_check(game_board):
        print(100*'\n')
        print(f"{starting_player} turn:")
        display_board(game_board)

        choice = player_choice(game_board)
        place_marker(game_board, marker1, choice)

        print(100*'\n')
        display_board(game_board)

        if win_check(game_board, marker1):
            print(f"{starting_player} has won the game!")
            break

        print(100*'\n')
        print(f"{second_player} turn:")
        display_board(game_board)

        choice = player_choice(game_board)
        place_marker(game_board, marker2, choice)

        print(100*'\n')
        display_board(game_board)

        if win_check(game_board, marker2):
            print(f"{second_player} has won the game!")
            break

    if not replay():
        break
    else:
        player1 = '#'
        player2 = '#'