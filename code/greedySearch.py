from timeit import default_timer as timer
import support

def greedySearch(score_board, countries, voters):
    max_iterations = 100000
    i = 0
    iters = 0
    xNow = support.getInitialSolution(voters)
    xBest = xNow[:]
    entertainmentXBest, distances = support.getEntertainment(xBest, countries, score_board, voters, 0)
    oldEntertainment = entertainmentXBest
    oldDistances = distances
    
    while i < max_iterations:
        xNow, key1 = support.getAdjacentNeighbour(xNow)
        # entertainmentXNow = getEntertainment(xNow, countries, score_board, voters, key1)
        
        start = timer()
        otherE , otherD = support.getEntertainment(xNow, countries, score_board, voters, key1)
        end = timer()
        print('full: ', end - start)
        
        start = timer()
        entertainmentXNow, distances = support.offsetGetEntertainment(xNow, countries, score_board, voters, key1, oldEntertainment, oldDistances)
        end = timer()
        print('reduced: ', end - start)
        
        if entertainmentXNow < entertainmentXBest:
            print("new solution", entertainmentXNow)
            xBest = xNow[:]
            entertainmentXBest = entertainmentXNow
        i = i+1
    return "xBest:", xBest, entertainmentXBest
