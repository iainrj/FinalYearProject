import random, csv, numpy, itertools

def voting_order(score_board, countries, voters):
    # select feasible solution and set xnow and xbest to it
    max_iterations = 100
    i = 0
    xNow = getInitialSolution(voters)
    xBest = xNow
    entertainmentXBest = getEntertainment(xBest, countries, score_board, voters)
    
    # while stopping criteria is not met:
    while i < max_iterations:
        # select a neighbour and set xNow to it
        xNow = getNeighbour(xNow)
        # if cost of xnow < cost of best then set xbest to xnow
        entertainmentXNow = getEntertainment(xNow, countries, score_board, voters)
        # print "entertainmentXNow", entertainmentXNow
        if entertainmentXNow < entertainmentXBest:
            print "new solution", entertainmentXNow
            xBest = xNow[:]
            entertainmentXBest = entertainmentXNow
        i = i+1
    return "xBest:", xBest, entertainmentXBest

def getInitialSolution(countries):
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
    
def getEntertainment(solution, countries, score_board, voters):
    entertainmentValue = 0
    performing_countries = countries[:]
    current_solution = solution[:]
    # print 'solution: ', current_solution
    # print 'performers: ', performing_countries
    # print 'voters: ', voters
    distances = [] # keep distances between min and max every round (len = 37)
    # index of country = countries.index(current_solution[i])
    scores = [0] * 26
    for j in range(len(solution)):
        for i in range(len(countries)):
            # print i, j
            # print voters.index(solution[j])
            # print current_solution[j], performing_countries[i], score_board[i][voters.index(solution[j])]
            # print current_solution[i], countries.index(current_solution[i]), score_board[countries.index(current_solution[i])][j]
            # print i, j, scores[i], score_board[countries.index(current_solution[i]) + 1][j]
            scores[i] = score_board[i][voters.index(solution[j])] + scores[i]
        distance = max(scores) - min(scores)
        # print distance
        distances.append(distance)
    # print scores, len(scores)
# remove the first and last distances as they will always be the same (12and 288)??
    
    entertainmentValue = (sum(distances) / len(distances))
 
    return entertainmentValue

def bruteForce(score_board, countries, voters):
    best = voters[:]
    bestCost = getEntertainment(numpy.asarray(voters), countries, score_board, voters)

    for solution in itertools.permutations(voters):
        currentCost = getEntertainment(numpy.asarray(solution), countries, score_board, voters)

        if currentCost < bestCost:
            print 'New Solution: ', currentCost
            best = solution[:]
            bestCost = currentCost

    return best, bestCost


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

    print(bruteForce(SCOREBOARD, PERFORMING_COUNTRIES, VOTING_COUNTRIES))
    # print(voting_order(SCOREBOARD, PERFORMING_COUNTRIES, VOTING_COUNTRIES))
