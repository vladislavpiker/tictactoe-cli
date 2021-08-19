import os

print('\nWelcome to Tic-Tac-Toe!')
print('''
 1 | 2 | 3
 —   —   —
 4 | 5 | 6
 —   —   —
 7 | 8 | 9
''')
indexes_of_grid = (2, 6, 10, 26, 30, 34, 50, 54, 58)

def game(p1, p2):
    grid = '\n   |   |   \n———————————\n   |   |   \n———————————\n   |   |   \n'
    winlist = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
    p1_yet_was = []
    p2_yet_was = []
    print(grid)
    for i in range(9):
        if i % 2 == 0:
            print(f'{p1}', end=', ')
            sym = 'X'
            cur_plr = p1
        elif i % 2:
            print(f'{p2}', end=', ')
            sym = 'O'
            cur_plr = p2

        while 1:
            try:
                num_input = int(input('enter number of cell: '))
                assert 0 < num_input < 10
                assert (num_input not in p1_yet_was) and (num_input not in p2_yet_was)
            except (ValueError, AssertionError):
                print('Number is incorrect, try again')
                continue
            rep_ind = indexes_of_grid[num_input - 1]
            grid_list = list(grid)
            grid_list[rep_ind] = sym
            grid = ''.join(grid_list)
            if cur_plr == p1: p1_yet_was.append(num_input)
            elif cur_plr == p2: p2_yet_was.append(num_input)
            break

        if os.name == 'posix': os.system('clear')
        elif os.name == 'nt': os.system('cls')
        print(grid)

        for x in winlist:
            w_p2 = [j in p2_yet_was for j in x]
            w_p1 = [j in p1_yet_was for j in x]
            if all(w_p1):
                print(f'\n{p1} is winner!\n')
                return
            if all(w_p2):
                print(f'\n{p2} is winner!\n')
                return

    print('\nNo winner\n')


def tic_tac_game():
    while 1:
        start = input('Start new game [y/N]? ')
        if start in ('y', 'Y', 'Yes', 'yes'):

            def name_input(plr_num: int):
                while 1:
                    player = input(f'Player{plr_num}, enter your name: ')
                    if len(player) == 0:
                        print('Name length must be greater than zero')
                        continue
                    return player

            player1, player2 = name_input(1), name_input(2)
            game(player1, player2)
        else:
            print('Goodbye!')
            return
tic_tac_game()
