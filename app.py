from random import choice
from sys import exit

game_dict = {'1':'paper', '2':'rock', '3':'scissors'}
valid_input = ['1', '2', '3']
score = {'player':0, 'cpu':0}


def get_player_input():
    player_input = input("Please enter: 1 - for paper; 2 - for rock; 3 - for scissors: Any other character to quit: ")
    if player_input not in valid_input:
        print("Game over!")
        print_the_result()
        exit(0)
    # return None
    else:
        print(f"You have chosen {game_dict[player_input]}")
    return player_input


def get_cpu_input():
    cpuinput = choice(valid_input)
    print(f"The computer have chosen {game_dict[cpuinput]}")
    return cpuinput


def calculate_the_winer(p, c):
# try using simple neural network later on this decision
    if p==c:
        print("Draw!")
        return
    if (p == '1' and c == '2') or (p == '2' and c == '3') or (p == '3' and c == '1'):
        print("Player won!")
        add_point('player')
    else:
        print("CPU won!")
        add_point('cpu')


def print_the_result():
    print(f"The result is Player [{score['player']}] : [{score['cpu']}] CPU")


def add_point(winner):
    current_points = score[winner]
    score[winner] = current_points + 1


while(True):
    print_the_result()
    player_input = get_player_input()
    cpu_input = get_cpu_input()
    calculate_the_winer(player_input, cpu_input)


