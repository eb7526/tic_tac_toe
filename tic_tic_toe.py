"""Simple game of noughts and crosses for 2 players"""
from IPython.display import clear_output
from random import randint

# set game variables
already_used = []
sample = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
reference_position = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
game_state = True


def display_input_positions():
    # Shows player at start of game the reference positions on the game board.
    display_board(reference_position)
    print('\n-------------------')
    print('Input positions')
    print('-------------------\n')
    print('\n')


def display_board(game_list):
    # Displays the current game board to the user.
    print('\n' * 100)
    print(f'\n  {game_list[0]}  |', f'{game_list[1]} |', f' {game_list[2]} ')
    print(f'---------------')
    print(f'  {game_list[3]}  |', f'{game_list[4]} |', f' {game_list[5]} ')
    print(f'---------------')
    print(f'  {game_list[6]}  |', f'{game_list[7]} |', f' {game_list[8]} \n')


def intro():
    # Ask for player names and assign each on to either o or x.
    player_1 = ''
    allowed_symbols = ['x', 'o']
    print("Welcome to Ed's Noughts and Crosses!")
    player_1_name = input('Player 1: What is your name? ')
    player_2_name = input('Player 2: What is your name? ')
    while player_1 not in allowed_symbols:
        player_1 = input(f'{player_1_name}: Do you want to play as x or o? ')
        if player_1 == 'x':
            player_2 = 'o'
        else:
            player_2 = 'x'
    display_input_positions()
    return player_1_name, player_1, player_2_name, player_2


def game_winner():
    # Logic to detemine when the game has been won.
    win_1 = sample[0] == sample[1] == sample[2] != ' '
    win_2 = sample[3] == sample[4] == sample[5] != ' '
    win_3 = sample[6] == sample[7] == sample[8] != ' '
    win_4 = sample[0] == sample[3] == sample[6] != ' '
    win_5 = sample[1] == sample[4] == sample[7] != ' '
    win_6 = sample[2] == sample[5] == sample[8] != ' '
    win_7 = sample[0] == sample[4] == sample[8] != ' '
    win_8 = sample[2] == sample[4] == sample[6] != ' '
    if win_1 or win_2 or win_3 or win_4 or win_5 or win_6 or win_7 or win_8:
        return True


def play_again():
    # Offers the players an option to play again or not.
    global game_state
    another_game = input("Would you like to play again? (y/n) ")
    if another_game == 'y':
        reset_game_data()
        display_board(sample)
        run_game()
    elif another_game == 'n':
        print('Thanks for playing')
        game_state = False
    else:
        print('Incorrect input. Input y/n.')
        play_again()


def reset_game_data():
    # Resets game data at end of game.
    global sample, already_used
    sample = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    already_used = []
    return sample, already_used


def run_game():
    turn = randint(0, 1)
    if turn:
        print(player_1_name + ' will go first')
    else:
        print(player_2_name + ' will go first')
    global game_state
    while game_state:
        try:
            if turn:
                position = int(
                    input(f'{player_1_name} select next position (1-9). Type any letter to quit: '))
            else:
                position = int(
                    input(f'{player_2_name} select next position (1-9). Type any letter to quit: '))
        except ValueError:
            game_state = False
            print('Thanks for playing!!')
            break
        if position in range(1, 10):
            if position in already_used:
                print('Please select an empty sqaure.')
                continue
            else:
                already_used.append(position)
                if turn:
                    sample[position - 1] = player_1
                else:
                    sample[position - 1] = player_2
            display_board(sample)
            if game_winner() or len(already_used) == 9:
                if len(already_used) == 9:
                    print(f'Tied game!')
                elif turn:
                    print(f'Well done, {player_1_name} wins!')
                else:
                    print(f'Well done, {player_2_name} wins!')
                play_again()
            else:
                pass
            turn = not turn
        else:
            print('Number must be between 1-9!')
            continue


player_1_name, player_1, player_2_name, player_2 = intro()
run_game()
