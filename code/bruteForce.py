import numpy, itertools
import support

def bruteForce(score_board, countries, voters):
    best = voters[:]
    bestCost = support.getEntertainment(numpy.asarray(voters), countries, score_board, voters)

    for solution in itertools.permutations(voters):
        currentCost, dist = support.getEntertainment(numpy.asarray(solution), countries, score_board, voters)

        if currentCost < bestCost:
            # print('New Solution: ', currentCost)
            best = solution[:]
            bestCost = currentCost

    return best, bestCost
