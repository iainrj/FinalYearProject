import random, math
import support

def simulatedAnnealing(score_board, countries, voters):
    num_iterations = 400
    ti = 2000
    tl = 60
    cr_coefficient = 0.8
    
    # num_iterations = 250
    # ti = 2000
    # tl = 60
    # cr_coefficient = 0.85
    
    t = ti
    
    xNow = support.getInitialSolution(voters)
    entertainmentXNow, distxNow = support.getEntertainment(xNow, countries, score_board, voters)
    
    xBest = xNow[:]
    entertainmentXBest = entertainmentXNow

    for i in range(num_iterations):
        for j in range(tl):
            xPrime = support.getNeighbour(xNow)
            entertainmentXPrime, distXPrime = support.getEntertainment(xPrime, countries, score_board, voters)

            deltaC = entertainmentXPrime - entertainmentXNow

            if deltaC <= 0:
                xNow = xPrime[:]
                entertainmentXNow = entertainmentXPrime
            else:
                q = random.randint(0, 1)

                if q < math.exp(-(deltaC)/t):
                    xNow = xPrime[:]
                    entertainmentXNow = entertainmentXPrime

            if entertainmentXNow < entertainmentXBest:
                # print("new solution", entertainmentXNow)
                xBest = xNow[:]
                entertainmentXBest = entertainmentXNow
                i = 0

        t = t * cr_coefficient
    return xBest, entertainmentXBest
