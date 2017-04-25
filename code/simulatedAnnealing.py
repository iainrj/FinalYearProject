import random, math
import support

def simulatedAnnealing(score_board, performers, voters, maxScorePerRound):
    num_iterations = 500
    ti = 4000
    tl = 40
    cr_coefficient = 0.92
    i = 0
    
    t = ti
    
    xNow = support.getInitialSolution(performers, score_board, voters, maxScorePerRound)
    entertainmentXNow, distxNow = support.getEntertainment(xNow, performers, score_board, voters, maxScorePerRound)
    
    xBest = xNow[:]
    entertainmentXBest = entertainmentXNow
    oldEntertainment = entertainmentXNow
    oldDistances = distxNow

    while i < num_iterations:
        for j in range(tl):
            xPrime, key1 = support.getAdjacentNeighbour(xNow)
            
            # otherE, otherD = support.getEntertainment(xPrime, performers, score_board, voters, maxScorePerRound)
            entertainmentXPrime, distXPrime = support.offsetGetEntertainment(xPrime, performers, score_board, voters, key1, oldEntertainment, oldDistances, maxScorePerRound)
            
            
            deltaC = entertainmentXPrime - entertainmentXNow

            if deltaC <= 0:
                xNow = xPrime[:]
                entertainmentXNow = entertainmentXPrime
                oldEntertainment = entertainmentXPrime
                oldDistances = distXPrime
            else:
                q = random.randint(0, 1)

                if q < math.exp(-(deltaC)/t):
                    xNow = xPrime[:]
                    entertainmentXNow = entertainmentXPrime
                    oldEntertainment = entertainmentXPrime
                    oldDistances = distXPrime

            if entertainmentXNow < entertainmentXBest:
                # print("new solution", entertainmentXNow)
                xBest = xNow[:]
                entertainmentXBest = entertainmentXNow
                i = 0
        
        t = t * cr_coefficient
        i = i + 1
    return xBest, entertainmentXBest
