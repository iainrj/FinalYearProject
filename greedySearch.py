import random

def voting_order(score_board, countries):
    # select feasible solution and set xnow and xbest to it
    max_iterations = 100
    i = 0
    xNow = getInitialSolution(countries)
    xBest = xNow
    entertainmentXBest = getEntertainment(xBest)
    
    # while stopping criteria is not met:
    while i < max_iterations:
        # select a neighbour and set xNow to it
        xNow = getNeighbour(xNow)
        # if cost of xnow < cost of best then set xbest to xnow
        entertainmentXNow = getCost(xNow)
        if entertainmentXNow > entertainmentXBest:
            xBest = xNow
            entertainmentXBest = entertainmentXNow
        i = i+1
    return xBest

def getInitialSolution(countries):
    order = []
    while len(countries) > 0:
        nextCountry = countries[0]
        order.insert(0, nextCountry)
        countries.remove(nextCountry)
    return order
    
def getNeighbour(xNow):
    neighbour = xNow[:]
    key1, key2 = random.sample(list(neighbour), 2)
    index1, index2 = neighbour.index(key1), neighbour.index(key2)
    neighbour[index2], neighbour[index1] = neighbour[index1], neighbour[index2]
    
    return neighbour
    
def getEntertainment(solution):
    # entertainment value
    # distance between first and last country (who can still win)
    
    # keep list of teams that can still win (initially all countries)
    # reveal the countries votes according to given order (one iteration through that countries column)
    # after each voting round remove teams that can't win
    # ?? no. rounds remaining * 12 < first place score = team can't win 
    # find distance between first and last team's scores (now only teams that can win)
    # sum distances (minimise) / keep average distance over all rounds (minimise)
    
    return entertainment

if __name__ == '__main__':
    #Eurovision 2014 scoreboard. 1st column is Albania's vote, 2nd column is Armenia's vote, etc.
    VOTING_COUNTRIES = ['Albania', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Denmark', 'Estonia', 'FYR Macedonia', 'Finland', 'France',
                        'Georgia', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Israel', 'Italy', 'Latvia', 'Lithuania', 'Malta', 'Moldova',
                        'Montenegro', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Slovenia', 'Spain', 'Sweden', 'Switzerland',
                        'Netherlands', 'Ukraine', 'United Kingdom']
    SCOREBOARD = [
        [ 0,  0,  5, 10,  8,  4,  1,  8,  0,  2,  0,  6,  0,  5,  2,  0,  0,  5, 10,  7,  5,  0, 10,  7,  0,  5,  0,  0,  7,  0,  0,  6,  0,  0,  0,  0,  0],
        [ 0,  8,  0,  7,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  3,  0,  5,  1,  0,  0,  0,  0, 12,  0,  0,  0,  0,  0,  0,  6,  0],
        [ 0,  0,  0,  0,  3,  0,  0,  0,  0,  0,  0,  7,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10, 12,  0,  0,  0,  0,  0,  1,  0],
        [ 0,  0,  2,  0,  0,  0,  5,  0,  0,  0,  7,  0,  2,  0,  5,  0,  0,  0,  7,  0,  0,  0,  0,  0,  6,  0,  0,  0,  1,  8,  0,  1,  4,  0,  6,  0,  4],
        [ 0,  0,  1,  0,  4,  0,  6,  3,  0,  7,  2,  0,  5,  3,  0,  1,  7,  0,  0,  5,  8,  2,  0,  0,  0,  7,  3,  1,  0,  0,  5,  0,  3,  5, 10,  0,  0],
        [ 0,  0,  8,  6,  1,  5,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  2,  8,  5,  0,  0,  8, 12,  0,  4,  0,  1,  0,  0,  0,  0,  8,  0,  0,  0,  0,  0],
        [ 0,  0, 12,  0, 10,  0,  2,  5,  8,  4, 12, 12,  6,  7,  7,  2,  0,  6,  0, 10,  0,  6,  3, 10,  0,  1,  4,  7,  8,  6,  0,  4,  5,  0,  7, 10,  0],
        [ 6, 12,  0,  0,  0,  0,  0,  0, 12,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  7,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  2,  7,  0,  0,  0,  5,  0,  5,  0, 10,  1,  3,  3,  0,  0,  8,  0,  0,  0,  2,  4,  2,  0,  0,  0,  0,  0,  1,  0,  2,  0,  0,  7,  0],
        [ 2,  7,  0,  4,  6,  0,  0,  0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  2,  3,  0,  0,  1,  0,  0,  0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  2],
        [ 5,  0,  0,  1,  0, 12,  8,  4,  3, 12, 10, 10,  7, 12, 10, 10, 12, 12, 12,  6, 10, 10,  7,  2, 10,  0, 12,  8,  5,  0, 12, 12, 12, 12, 12,  8, 12],
        [ 4,  6,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  8,  0,  2,  0,  0,  2,  0,  0,  7,  0,  5,  0],
        [ 7,  0,  6,  0,  0, 10, 12, 10,  0, 10,  4,  2,  0,  2,  8,  7,  4, 10,  0,  8,  7,  7,  6,  3,  8,  4,  8, 12,  2, 10,  8, 10,  0,  6,  8, 12,  7],
        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0],
        [ 0, 10,  0, 12, 12,  0,  0,  1,  6,  0,  0,  8,  0, 10,  0,  0,  0,  3,  0,  2,  6,  5,  8,  0,  0,  0,  2,  0,  0,  0,  0,  0,  0,  0,  0,  4,  0],
        [10,  0,  0,  0,  0,  0,  0,  0,  2,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 12,  0,  6,  0,  0,  0,  0,  0,  0,  0,  0,  0,  2,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  8,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  4,  0,  0,  3,  4,  6,  0,  0,  0,  0,  4,  0,  6,  5,  0,  0,  6,  3,  0,  0,  0,  0,  7,  3,  0,  0,  0,  3,  0,  0,  6,  4,  2,  0,  6],
        [12,  2,  0,  0,  0,  2,  0,  2,  0,  0,  6,  0,  1,  0,  0,  0,  6,  4,  0,  4,  4,  0,  0,  0,  5,  2,  0,  5,  0,  0,  4,  0,  0,  8,  0,  2,  5],
        [ 0,  5,  3,  0,  0,  0,  0,  0,  0,  0,  0,  1,  3,  4,  1,  0,  5,  0,  2,  0,  2,  3,  0,  5,  0, 10,  7,  6,  0,  0,  3,  0,  0,  0,  3,  0,  1],
        [ 8,  0,  7,  8,  5,  7,  3,  7, 10,  5,  0,  0,  0,  6,  0,  6,  1,  7,  0,  1,  0,  0,  4, 12,  0,  0,  6, 10,  6,  7,  0,  2,  7,  1,  4,  3,  0],
        [ 1,  0,  0,  5,  0,  0,  0,  0,  0,  3,  0,  0,  0,  0,  0,  0,  3,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4,  0,  0,  0,  0,  5,  0, 10],
        [ 0,  1,  0,  0,  0,  6,  0,  0,  0,  6,  3,  0,  8,  0,  0,  8,  0,  0,  0,  0,  1,  0,  0,  0,  1,  6,  5,  4,  0,  1,  6,  3,  8,  3,  1,  0,  3],
        [ 0,  4, 10,  0,  2,  8, 10, 12,  7,  8,  8,  0, 12,  8, 12, 12, 10,  0,  4, 12, 12,  0,  0,  0, 12, 12, 10,  3,  3,  2, 10,  7, 10, 10,  0,  0,  8],
        [ 3,  3,  0,  3,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  1,  7,  0,  0,  0,  0,  3,  0,  0,  0,  4,  8,  0,  0,  0,  0,  4,  0,  0,  3,  0,  0,  0,  0,  5,  0,  5,  0,  0,  0,  0,  0]
    ]

    print(voting_order(SCOREBOARD, VOTING_COUNTRIES))
