import itertools
import support

def bruteForce(score_board, countries, voters, maxScorePerRound):
    best = voters[:]
    bestCost = support.getEntertainment(voters, countries, score_board, voters, maxScorePerRound)

    for solution in itertools.permutations(voters):
        currentCost, dist = support.getEntertainment(solution, countries, score_board, voters, maxScorePerRound)

        if currentCost < bestCost:
            # print('New Solution: ', currentCost)
            best = solution[:]
            bestCost = currentCost

    return best, bestCost
