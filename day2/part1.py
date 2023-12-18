
def get_input():
    with open('input', 'r') as file: 
        return file.read()

def part_one(puzzle_input):
    poss = {'red': 12, 'green': 13, 'blue': 14}
    poss_games = 0
    for id, game in enumerate(puzzle_input.split('\n'), start=1):
        if game != '':
            game = game.split(': ')[1]
        else:
            break
        for hand in game.split('; '):
            imposs = False
            for subset in hand.split(', '):
                n, color = subset.split()
                if int(n) > poss[color]:
                    imposs = True
                    break
            if imposs:
                break
        else:
            poss_games += id
    return poss_games

def part_two(puzzle_input):
    power = 0
    for id, game in enumerate(puzzle_input.split('\n'), start=1):
        max_num = {'red': 0, 'blue': 0, 'green': 0}
        if game != '':
            game = game.split(': ')[1]
        else:
            break
        for hand in game.split('; '):
            for subset in hand.split(', '):
                n, color = subset.split()
                max_num[color] = max(int(n), max_num[color])
        power = power + (max_num['red'] * max_num['blue'] * max_num['green'])
    return power

if __name__ == "__main__":
    print('Part One: ', part_one(get_input()))
    print('Part Two: ', part_two(get_input()))
