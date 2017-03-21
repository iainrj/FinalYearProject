import random, csv, numpy, itertools, math

def voting_order(score_board, countries, voters):
    max_iterations = 100000
    i = 0
    iters = 0
    xNow = getInitialSolution(voters)
    xBest = xNow[:]
    entertainmentXBest, iters1 = getEntertainment(xBest, countries, score_board, voters)
    
    # while stopping criteria is not met:
    while i < max_iterations:
        # select a neighbour and set xNow to it
        # xNow = getNeighbour(xNow) # swap two random indexes
        xNow = getAdjacentNeighbour(xNow) # swap two adjacent indexes
        # if cost of xnow < cost of best then set xbest to xnow
        entertainmentXNow, iters2 = getEntertainment(xNow, countries, score_board, voters)
        # print "entertainmentXNow", entertainmentXNow
        if entertainmentXNow < entertainmentXBest:
            print("new solution", entertainmentXNow)
            xBest = xNow[:]
            entertainmentXBest = entertainmentXNow
            iters = iters2
        i = i+1
    return "xBest:", xBest, entertainmentXBest, iters

def getInitialSolution(countries):
    # order = ['Albania', 'Belarus', 'Poland', 'Russia', 'Armenia', 'Israel', 'Malta', 'FYR Macedonia', 'Denmark', 'Azerbaijan', 'Germany', 'San Marino', 'Moldova', 'Latvia', 'Finland', 'Montenegro', 'Hungary', 'Estonia', 'France', 'Romania', 'Iceland', 'Austria', 'Italy', 'Ukraine', 'Georgia', 'Lithuania', 'Norway', 'Sweden', 'Belgium', 'Greece', 'Ireland', 'Portugal', 'Slovenia', 'Spain', 'Switzerland', 'The Netherlands', 'United Kingdom']
    # return order
    # real_order = ['Azerbaijan','Greece','Poland','Albania','San Marino','Denmark','Montenegro','Romania','Russia','The Netherlands','Malta','France','United Kingdom','Latvia','Armenia','Iceland','FYR Macedonia','Sweden','Belarus','Germany','Israel','Portugal','Norway','Estonia','Hungary','Moldova','Ireland','Finland','Lithuania','Austria','Spain','Belgium','Italy','Ukraine','Switzerland','Georgia','Slovenia']
    # return real_order
    performing_countries = countries[:]
    order = []
    while len(performing_countries) > 0:
        nextCountry = performing_countries[0]
        order.insert(0, nextCountry)
        performing_countries.remove(nextCountry)
    return order
    
def getNeighbour(xNow):
    neighbour = xNow[:]
    key1, key2 = random.sample(list(neighbour), 2)
    index1, index2 = neighbour.index(key1), neighbour.index(key2)
    neighbour[index2], neighbour[index1] = neighbour[index1], neighbour[index2]
    
    return neighbour

def getAdjacentNeighbour(xNow):
    neighbour = xNow[:]
    key1 = random.randint(0, len(neighbour) - 2)
    key2 = key1 + 1
    neighbour[key2], neighbour[key1] = neighbour[key1], neighbour[key2]
    
    return neighbour
    
def getEntertainment(solution, countries, score_board, voters):
    entertainmentValue = 0
    performing_countries = countries[:]
    current_solution = solution[:]
    # solution = ['Azerbaijan','Greece','Poland','Albania','San Marino','Denmark','Montenegro','Romania','Russia','The Netherlands','Malta','France','United Kingdom','Latvia','Armenia','Iceland','FYR Macedonia','Sweden','Belarus','Germany','Israel','Portugal','Norway','Estonia','Hungary','Moldova','Ireland','Finland','Lithuania','Austria','Spain','Belgium','Italy','Ukraine','Switzerland','Georgia','Slovenia']
    # solution = ['Belarus', 'Malta', 'Montenegro', 'Norway', 'Albania', 'Azerbaijan', 'Denmark', 'Germany', 'Lithuania', 'Estonia', 'Russia', 'The Netherlands', 'Armenia', 'Poland', 'San Marino', 'Moldova', 'Georgia', 'France', 'Switzerland', 'Austria', 'Greece', 'Latvia', 'Israel', 'Ukraine', 'Sweden', 'FYR Macedonia', 'Slovenia', 'Iceland', 'Spain', 'Romania', 'Ireland', 'Italy', 'United Kingdom', 'Belgium', 'Hungary', 'Finland', 'Portugal']
    
    distances = [] # keep distances between min and max every round (len = 37)
    iters = 37
    scores = [0] * 26
    for j in range(len(solution)):
        for i in range(len(countries)):
            scores[i] = score_board[i][voters.index(solution[j])] + scores[i]
        # sorted_scores = sorted(scores)
        # print(iters)
        # iters = iterationsBeforeStop(sorted_scores, solution, j, iters)
        otherMin = refinedMaxMin(scores, solution, j)
        distance = max(scores) - otherMin
        distances.append(distance)
    # exit()
    entertainmentValue = sum(distances)
 
    return entertainmentValue, iters

def refinedMaxMin(scores, solution, j):
    sorted_scores = sorted(scores[:])
    currentTop = sorted_scores[-1]
    minScore = sorted_scores[0]
    del sorted_scores[-1] # remove highest score
    roundsRemaining = (len(solution) - 1 - j)

    for score in sorted_scores:
        if score + (12 * roundsRemaining) < currentTop:
            minScore = score
    return minScore
    
def iterationsBeforeStop(sorted_scores, solution, j, iters):
    # print(sorted_scores[-1] - sorted_scores[-2] > 12 * (len(solution) - 1 - j), j+1 < iters)
    if sorted_scores[-1] - sorted_scores[-2] > 12 * (len(solution) - 1 - j) and j+1 < iters:
        print('Winner cannot be caught after: ', j + 1, 'iterations', sorted_scores[-1], sorted_scores[-2], (12 * (len(solution) - 1 - j)))
        return j+1
    return iters

def bruteForce(score_board, countries, voters):
    best = voters[:]
    bestCost = getEntertainment(numpy.asarray(voters), countries, score_board, voters)

    for solution in itertools.permutations(voters):
        currentCost = getEntertainment(numpy.asarray(solution), countries, score_board, voters)

        if currentCost < bestCost:
            print('New Solution: ', currentCost)
            best = solution[:]
            bestCost = currentCost

    return best, bestCost
    
def simulated_annealing(score_board, countries, voters):
    num_iterations = 10000
    ti = 5000
    tl = 50
    cr_coefficient = 0.8
    
    t = ti
    
    xNow = getInitialSolution(voters)
    entertainmentXNow = getEntertainment(xNow, countries, score_board, voters)
    
    xBest = xNow[:]
    entertainmentXBest = entertainmentXNow

    for i in range(num_iterations):
        for j in range(tl):
            xPrime = getNeighbour(xNow)
            entertainmentXPrime = getEntertainment(xPrime, countries, score_board, voters)

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
                xBest = xNow[:]
                entertainmentXBest = entertainmentXNow

        t = t * cr_coefficient
    return "xBest:", xBest, entertainmentXBest

# def printScoreboard(board, voting, performing):
#     print ' ', ' '.join(voting)
#     for i in range(len(board)):
#         print performing[i]
#         for j in range(board[i]):
#             if (board[i][j] == 0):
#                 print '-'
#             else:
#                 print board[i][j]
                
#         print

if __name__ == '__main__':
    # PERFORMING_COUNTRIES = ['Ukraine','Belarus','Azerbaijan','Iceland','Norway','Romania','Montenegro','Poland','Greece','Austria','Germany',
    #                     'Sweden','France','Russia','Italy','Slovenia','Finland','Spain','Switzerland','Hungary','Malta','Denmark',
    #                     'The Netherlands','San Marino','United Kingdom']
    # PERFORMING_COUNTRIES_SHORT = ['UA','BY','AZ','IS','NO','RO','ME','PL','GR','AT','DE',
    #                     'SE','FR','RU','IT','SI','FI','ES','CH','HU','MT','DK',
    #                     'NL','SM','UK']
    # # Eurovision 2014 scoreboard. 1st column is Albania's vote, 2nd column is Armenia's vote, etc.
    # VOTING_COUNTRIES = ['Albania', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Denmark', 'Estonia', 'FYR Macedonia', 'Finland', 'France',
    #                      'Georgia', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Israel', 'Italy', 'Latvia', 'Lithuania', 'Malta', 'Moldova',
    #                      'Montenegro', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Slovenia', 'Spain', 'Sweden', 'Switzerland',
    #                      'Netherlands', 'Ukraine', 'United Kingdom']
    # VOTING_COUNTRIES_SHORT = ['AL', 'AM', 'AT', 'AZ', 'BY', 'BE', 'DK', 'EE', 'MK', 'FI', 'FR',
    #                      'GE', 'DE', 'GR', 'HU', 'IS', 'IE', 'IL', 'IT', 'LV', 'LT', 'MT', 'MD',
    #                      'ME', 'NO', 'PL', 'PT', 'RO', 'RU', 'SM', 'SI', 'ES', 'SE', 'CH',
    #                      'NL', 'UA', 'UK']
    
    # scoreboard = numpy.zeros((26, 37), dtype=numpy.int)
    # with open('ESC-2014-grand_final-full_results.csv', 'rbU') as csvfile:
    #     results = csv.reader(csvfile)
    #     results.next() # skip the first two lines
    #     results.next()
    #     j = 0
    #     currentRow = []
    #     emptyScoreboard = []
        
    #     for i, row in enumerate(results):
    #         points = 0
    #         if row[-1] != '\n':
    #             points = row[-1]
    #         # print row[0], row[1], points, i
    #         currentRow.append(int(points))
    #         # print 'cr', row[0], row[1], points, currentRow
    #         # if i % 26 == 0:
    #         #     print i
    #         #     print len(currentRow)
    #         #     print currentRow
    #         #     emptyScoreboard.append(currentRow)
    #         #     j = j + 1
    #         #     currentRow = []
    # printScoreboard(currentRow, VOTING_COUNTRIES_SHORT, PERFORMING_COUNTRIES_SHORT)
    # # final = [currentRow[i:i + 26] for i in xrange(0, len(currentRow), 26)]

    # # print 'scoreboard', final
    # exit()
            
    PERFORMING_COUNTRIES = ['Ukraine','Belarus','Azerbaijan','Iceland','Norway','Romania','Armenia','Montenegro','Poland','Greece','Austria',
    'Germany','Sweden','France','Russia','Italy','Slovenia','Finland','Spain','Switzerland','Hungary','Malta','Denmark','The Netherlands',
    'San Marino','United Kingdom']
    # Eurovision 2014 scoreboard. 1st column is Albania's vote, 2nd column is Armenia's vote, etc.
    VOTING_COUNTRIES = ['Albania', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Denmark', 'Estonia', 'FYR Macedonia', 'Finland', 'France',
                        'Georgia', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Israel', 'Italy', 'Latvia', 'Lithuania', 'Malta', 'Moldova',
                        'Montenegro', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Slovenia', 'Spain', 'Sweden', 'Switzerland',
                        'The Netherlands', 'Ukraine', 'United Kingdom']
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

    # print(bruteForce(SCOREBOARD, PERFORMING_COUNTRIES, VOTING_COUNTRIES))
    print(voting_order(SCOREBOARD, PERFORMING_COUNTRIES, VOTING_COUNTRIES))
    # print(simulated_annealing(SCOREBOARD, PERFORMING_COUNTRIES, VOTING_COUNTRIES))
