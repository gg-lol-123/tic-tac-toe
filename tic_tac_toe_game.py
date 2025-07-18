#tic tac toe

import random

test_board = ['','','','','','','','','','']

def display_board(board):
    print('\n' * 10)
    print(board[7] + '  |   ' + board[8] + '    |   ' + board[9])
    print()
    print(board[4] + '  |   ' + board[5] + '    |   ' + board[6])
    print()
    print(board[1] + '  |   ' + board[2] + '    |   ' + board[3])

display_board(test_board)

def player_input():
    print('Player 1\'s choice: ')
    correct_list = ['X','O']
    choice = "Wrong"
    while choice not in correct_list:
        choice = input("Pick capital 'X' or 'O': ")

    if choice == 'X':
        player1 = 'X'
        player2 = 'O'
    elif choice == 'O':
        player1 = 'O'
        player2 = 'X'
    print((player1,player2))
    return(player1,player2)

player1,player2 = player_input()

def place_marker(test_board, marker, position): #marker = 'X' or 'O'
    test_board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

print(win_check(test_board,'X'))

def choose_first():
    result = random.randint(0,1)
    if result == 0:
        return player2
    else:
        return player1

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i) == True:
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Enter position: "))
    return position

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn," will go first.")
    play_game = input('Are you ready to play? Enter Yes or No.')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
