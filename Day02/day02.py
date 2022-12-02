# A = Rock, B = Paper, C = Scissors
# X = Rock, Y = Paper, Z = Scissors

# The first top-secret strategy guide
def part1(elves_data):
    total = 0
    elfGame = 0
    pointVals = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}
    losses = {'X': 'B', 'Y': 'C', 'Z': 'A'}
    for game in elves_data:
        elfGame += pointVals[game[2]]
        if pointVals[game[0]] == pointVals[game[2]]:
            elfGame += 3
            total += elfGame
        else:
            if game[0] == losses[game[2]]:
                total += elfGame
            else:
                elfGame += 6
                total += elfGame
        elfGame = 0
    return total

# The second top-secret strategy guide
def part2(elves_data):
    total = 0
    elfGame = 0
    pointVals = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}
    # Maps Opponent Choice to What I Should Play to Beat Them
    losses = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    # Maps Opponent Choice to What I Should Play to Lose to Them
    wins = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    for game in elves_data:
        # Draw
        if game[2] == 'Y':
            elfGame += 3
            elfGame += pointVals[game[0]]
        # Win
        elif game[2] == 'Z':
            elfGame += 6
            elfGame += pointVals[losses[game[0]]]
        # Lose
        else:
            elfGame += pointVals[wins[game[0]]]
        total += elfGame
        elfGame = 0
    return total



# Display results
gameInput = open('puzzle-input-02', 'r')
allGames = gameInput.readlines()
print("Total score from first game:", part1(allGames))
print("Total score from second game", part2(allGames))