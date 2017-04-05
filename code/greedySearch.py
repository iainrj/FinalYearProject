from timeit import default_timer as timer
import support

def greedySearch(score_board, performers, voters, maxScorePerRound):
    max_iterations = 10000
    iters = 0
    xNow = support.getInitialSolution(performers, score_board, voters, maxScorePerRound)
    xBest = xNow[:]
    entertainmentXBest, distances = support.getEntertainment(xNow, performers, score_board, voters, maxScorePerRound)
    oldEntertainment = entertainmentXBest
    oldDistances = distances
    
    for i in range(max_iterations):
        xNow, key1 = support.getAdjacentNeighbour(xNow)
        
        # start = timer()
        # otherE , otherD = support.getEntertainment(xNow, performers, score_board, voters)
        # end = timer()
        # print('full: ', end - start)
        
        # start = timer()
        entertainmentXNow, distancesXNow = support.offsetGetEntertainment(xNow, performers, score_board, voters, key1, oldEntertainment, oldDistances, maxScorePerRound)
        # end = timer()
        # print('reduced: ', end - start)
        
        if entertainmentXNow < entertainmentXBest:
            # print("new solution", entertainmentXNow)
            xBest = xNow[:]
            entertainmentXBest = entertainmentXNow
            i = 0
        
        oldEntertainment = entertainmentXNow
        oldDistances = distancesXNow
        i = i+1
    return xBest, entertainmentXBest
