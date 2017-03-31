import random

# List<String> -> List<String>
def getInitialSolution(countries):
    # order = ['Albania', 'Belarus', 'Poland', 'Russia', 'Armenia', 'Israel', 'Malta', 'FYR Macedonia', 'Denmark', 'Azerbaijan', 'Germany', 'San Marino', 'Moldova', 'Latvia', 'Finland', 'Montenegro', 'Hungary', 'Estonia', 'France', 'Romania', 'Iceland', 'Austria', 'Italy', 'Ukraine', 'Georgia', 'Lithuania', 'Norway', 'Sweden', 'Belgium', 'Greece', 'Ireland', 'Portugal', 'Slovenia', 'Spain', 'Switzerland', 'The Netherlands', 'United Kingdom']
    # return order
    # real_order = ['Azerbaijan','Greece','Poland','Albania','San Marino','Denmark','Montenegro','Romania','Russia','The Netherlands','Malta','France','United Kingdom','Latvia','Armenia','Iceland','FYR Macedonia','Sweden','Belarus','Germany','Israel','Portugal','Norway','Estonia','Hungary','Moldova','Ireland','Finland','Lithuania','Austria','Spain','Belgium','Italy','Ukraine','Switzerland','Georgia','Slovenia']
    # return real_order
    # piecemeal_order = ['Albania', 'Belarus', 'Poland', 'Russia', 'Armenia', 'Israel', 'Malta', 'FYR Macedonia', 'Denmark', 'Azerbaijan', 'Germany', 'San Marino','Moldova','Latvia', 'Finland', 'Montenegro', 'Hungary', 'Estonia', 'France', 'Romania', 'Iceland', 'Austria', 'Italy', 'Ukraine', 'Georgia', 'Ireland','Sweden', 'Lithuania', 'Greece', 'Spain', 'Belgium', 'Portugal', 'The Netherlands', 'United Kingdom', 'Norway', 'Slovenia', 'Switzerland']
    # return piecemeal_order
    performing_countries = countries[:]
    order = []
    while len(performing_countries) > 0:
        nextCountry = performing_countries[0]
        order.insert(0, nextCountry)
        performing_countries.remove(nextCountry)
    return order

# List<String> -> List<String>
def getNeighbour(xNow):
    neighbour = xNow[:]
    key1, key2 = random.sample(list(neighbour), 2)
    index1, index2 = neighbour.index(key1), neighbour.index(key2)
    neighbour[index2], neighbour[index1] = neighbour[index1], neighbour[index2]
    
    return neighbour

# List<String> -> List<String>
def getAdjacentNeighbour(xNow):
    neighbour = xNow[:]
    key1 = random.randint(0, len(neighbour) - 2)
    key2 = key1 + 1
    neighbour[key2], neighbour[key1] = neighbour[key1], neighbour[key2]
    
    return neighbour, key1

# List<Integer> -> List<String> -> Integer -> Integer
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

# List<String> -> List<String> -> Integer -> List<List<Integers>> -> Integer
def calculateDistances(solution, voters, no_performers, score_board):
    distances = []
    num_rows = len(voters)
    num_columns = no_performers
    scores = [0] * num_rows
    
    for j in range(num_rows):
        for i in range(num_columns):
            scores[i] = score_board[i][voters.index(solution[j])] + scores[i]
        minimumScore = refinedMaxMin(scores, solution, j)
        distances.append(max(scores) - minimumScore)
    
    return distances

# List -> List -> List -> List -> Integer -> Integer -> List
def offsetGetEntertainment(solution, countries, score_board, voters, key1, oldEntertainment, oldDistances):
    entertainmentValue = 0
    performing_countries = countries[:]
    current_solution = solution[:]
    distances = oldDistances[:]
    key2 = key1 + 1

    oldDistance1, oldDistance2 = oldDistances[key1], oldDistances[key2]

    l_dist = []
    scores = [0] * 26
    for j in range(key2 + 1):
        for i in range(len(countries)):
            scores[i] = score_board[i][voters.index(solution[j])] + scores[i]
        otherMin = refinedMaxMin(scores, solution, j)
        l_dist.append(max(scores) - otherMin)
    
    newDistance1, newDistance2 = l_dist[-1], l_dist[-2]
    entertainmentValue = oldEntertainment - (oldDistance1 + oldDistance2) + (newDistance1 + newDistance2)
    
    distances[key1] = newDistance1
    distances[key2] = newDistance2
    
    return entertainmentValue, distances

# List<Integer> -> List<String -> Integer -> Integer -> Integer
def iterationsBeforeStop(sorted_scores, solution, j, iters):
    if sorted_scores[-1] - sorted_scores[-2] > 12 * (len(solution) - 1 - j) and j+1 < iters:
        print('Winner cannot be caught after: ', j + 1, 'iterations', sorted_scores[-1], sorted_scores[-2], (12 * (len(solution) - 1 - j)))
        return j+1
    return iters

# List<String> -> List<String> -> List<List<Integer>> -> List<String> -> Integer
def getEntertainment(solution, countries, score_board, voters):
    entertainmentValue = 0
    performing_countries = countries[:]
    current_solution = solution[:]
    
    distances = []
    iters = 37
    scores = [0] * 26
    for j in range(len(solution)):
        for i in range(len(countries)):
            scores[i] = score_board[i][voters.index(solution[j])] + scores[i]
        otherMin = refinedMaxMin(scores, solution, j)
        distance = max(scores) - otherMin
        distances.append(distance)
    entertainmentValue = sum(distances)
    
    return entertainmentValue, distances

# List<List<Integer>> -> List<String> -> List<String> -> null
def printScoreboard(board, voting, performing):
    print(' ', ' '.join(voting))
    for i in range(len(board)):
        print(performing[i])
        for j in range(board[i]):
            if (board[i][j] == 0):
                print('-')
            else:
                print(board[i][j])
                
        print()

# PERFORMING_COUNTRIES_SHORT = ['UA','BY','AZ','IS','NO','RO','ME','PL','GR','AT','DE', 'SE','FR','RU','IT','SI','FI','ES','CH','HU','MT','DK','NL','SM','UK']
# VOTING_COUNTRIES_SHORT = ['AL', 'AM', 'AT', 'AZ', 'BY', 'BE', 'DK', 'EE', 'MK', 'FI', 'FR', 'GE', 'DE', 'GR', 'HU', 'IS', 'IE', 'IL', 'IT', 'LV', 'LT', 'MT', 'MD','ME', 'NO', 'PL', 'PT', 'RO', 'RU', 'SM', 'SI', 'ES', 'SE', 'CH','NL', 'UA', 'UK']

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