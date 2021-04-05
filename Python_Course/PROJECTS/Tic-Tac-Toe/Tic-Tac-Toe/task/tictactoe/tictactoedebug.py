def check_user_input(coordinate):
    for char in coordinate:
        if char in alphabet:
            return True
    return False


def coordinate_to_indices(coordinates):
    row = int(coordinates[0])
    col = int(coordinates[1])
    i = col + 2
    j = row - 1
    index = (j * 3 + i) - 3
    return index


debug = False
game_done = False

game_state = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

while not debug:
    choice = input("""Welcome to the Debug Menu! (Written by Michele Pipicelli)
                      Please input your choice.
                    
                      Menu Options:
                          (E)xit, (G)ame check, (P)rint board """)
    if choice == 'E':
        debug = True
        exit()
    elif debug == 'P':
        print(f'''
        ---------
        | {game_state[0]} {game_state[1]} {game_state[2]} |
        | {game_state[3]} {game_state[4]} {game_state[5]} |
        | {game_state[6]} {game_state[7]} {game_state[8]} |
        ---------''')

print(f'''
---------
| {game_state[0]} {game_state[1]} {game_state[2]} |
| {game_state[3]} {game_state[4]} {game_state[5]} |
| {game_state[6]} {game_state[7]} {game_state[8]} |
---------''')

row_one = [game_state[0], game_state[1], game_state[2]]
row_two = [game_state[3], game_state[4], game_state[5]]
row_three = [game_state[6], game_state[7], game_state[8]]

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

x_count = 0
o_count = 0

coordinates = ''

while not game_done:
    coordinates = input("Enter the coordinates: ")
    if check_user_input(coordinates):
        print('Please input numbers!')
        continue
    else:
        coordinates = coordinates.replace(" ", "")

        index_one = int(coordinates[0])
        index_two = int(coordinates[1])

        if index_one > 3 or index_one < 1 or index_two > 3 or index_two < 1:
            print('Coordinates should be from 1 to 3!')
            continue

        indice = coordinate_to_indices(coordinates)

        if game_state[indice] == " ":
            game_state[indice] = 'X'
        else:
            print('This cell is occupied! Choose another one!')
            continue

print(f'''
---------
| {game_state[0]} {game_state[1]} {game_state[2]} |
| {game_state[3]} {game_state[4]} {game_state[5]} |
| {game_state[6]} {game_state[7]} {game_state[8]} |
---------''')

for x in range(9):
    if game_state[x].upper() == 'X':
        x_count += 1
    elif game_state[x].upper() == 'O':
        o_count += 1

print(f'There are {x_count} X\'s on the board.')
print(f'There are {o_count} O\'s on the board.')
print(x_count - o_count)
print(o_count - x_count)


def check_impossible():
    stopped = False
    if (x_count) - o_count > 1:
        return True
    if (o_count) - x_count > 1:
        return True

    if check_winner('X') and check_winner('O'):
        return True

    return False


def check_winner(char):
    # Check horizontal
    if row_one.count(char) == 3:
        return True
    elif row_two.count(char) == 3:
        return True
    elif row_two.count(char) == 3:
        return True
    else:
        pass

    if row_one[0] == char and row_two[0] == char and row_three[0] == char:
        return True
    elif row_one[1] == char and row_two[1] == char and row_three[1] == char:
        return True
    elif row_one[2] == char and row_two[2] == char and row_three[2] == char:
        return True

    if row_one[0] == char and row_two[1] == char and row_three[2] == char:
        return True
    elif row_three[0] == char and row_two[1] == char and row_one[2] == char:
        return True

    return False


def check_draw():
    if game_state.__contains__('_') == False:
        if check_winner("O") == False and check_winner("X") == False:
            return 'Draw'


def check_not_finished():
    if game_state.__contains__('_'):
        return True
    return False


if check_impossible():
    print('Impossible')
    exit()

if check_winner('O'):
    print('O wins')
    exit()

if check_winner('X'):
    print('X wins')
    exit()

if check_draw():
    print('Draw')
    exit()

if check_not_finished():
    print('Game not finished')
    exit()


def check_winner():
    pass
