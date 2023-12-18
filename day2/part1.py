
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

if __name__ == "__main__":
    puzzle_input = get_input()
    print('Part One: ', part_one(puzzle_input))
