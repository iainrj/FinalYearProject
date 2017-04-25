import random, numpy

# List<String> -> List<String>
def getInitialSolution(performers, score_board, voters, maxScorePerRound):
    # order that this method returns normally
    # order = ['Albania', 'Belarus', 'Poland', 'Russia', 'Armenia', 'Israel', 'Malta', 'FYR Macedonia', 'Denmark', 'Azerbaijan', 'Germany', 'San Marino', 'Moldova', 'Latvia', 'Finland', 'Montenegro', 'Hungary', 'Estonia', 'France', 'Romania', 'Iceland', 'Austria', 'Italy', 'Ukraine', 'Georgia', 'Lithuania', 'Norway', 'Sweden', 'Belgium', 'Greece', 'Ireland', 'Portugal', 'Slovenia', 'Spain', 'Switzerland', 'The Netherlands', 'United Kingdom']
    # return order
    # 2014 order
    # real_order = ['Azerbaijan','Greece','Poland','Albania','San Marino','Denmark','Montenegro','Romania','Russia','The Netherlands','Malta','France','United Kingdom','Latvia','Armenia','Iceland','FYR Macedonia','Sweden','Belarus','Germany','Israel','Portugal','Norway','Estonia','Hungary','Moldova','Ireland','Finland','Lithuania','Austria','Spain','Belgium','Italy','Ukraine','Switzerland','Georgia','Slovenia']
    # return real_order
    # solution piecemeal returns = 2724
    # piece = ['Albania', 'Belarus', 'Poland', 'Russia', 'Armenia', 'Israel', 'Malta', 'FYR Macedonia', 'Denmark', 'Azerbaijan', 'Germany', 'San Marino', 'Moldova', 'Latvia', 'Finland', 'Montenegro', 'Hungary', 'Estonia', 'France', 'Romania', 'Iceland', 'Austria', 'Italy', 'Ukraine', 'Georgia', 'Belgium', 'Lithuania', 'Spain', 'Greece', 'Slovenia', 'Sweden', 'The Netherlands', 'United Kingdom', 'Norway', 'Ireland', 'Portugal', 'Switzerland']
    # return piece
    v_countries = voters[:]
    order = []
    while len(v_countries) > 0:
        nextCountry = v_countries[0]
        order.insert(0, nextCountry)
        v_countries.remove(nextCountry)
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
def refinedMaxMin(scores, solution, j, maxScorePerRound):
    sorted_scores = sorted(scores[:])
    currentTop = sorted_scores[-1]
    minScore = sorted_scores[0]
    # del sorted_scores[-1] # remove highest score
    roundsRemaining = (len(solution) - 1 - j)

    for score in sorted_scores:
        if score + (maxScorePerRound * roundsRemaining) <= currentTop:
            minScore = score
    return minScore

# List<String> -> List<String> -> Integer -> List<List<Integers>> -> Integer
# UNUSED
# def calculateDistances(solution, voters, no_performers, score_board, maxScorePerRound):
#     distances = []
#     num_rows = len(voters)
#     num_columns = no_performers
#     scores = [0] * num_rows
    
#     for j in range(num_rows):
#         for i in range(num_columns):
#             scores[i] = score_board[i][voters.index(solution[j])] + scores[i]
#         minimumScore = refinedMaxMin(scores, solution, j, maxScorePerRound)
#         distances.append(max(scores) - minimumScore)
    
#     return distances

# List -> List -> List -> List -> Integer -> Integer -> List
def offsetGetEntertainment(solution, countries, score_board, voters, key1, oldEntertainment, oldDistances, maxScorePerRound):
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
            v = voters.index(solution[j])
            scores[i] = scores[i] + score_board[i][v]
        otherMin = refinedMaxMin(scores, solution, j, maxScorePerRound)
        l_dist.append(max(scores) - otherMin)
    
    newDistance1, newDistance2 = l_dist[key2], l_dist[key1]
    entertainmentValue = oldEntertainment - (oldDistance1 + oldDistance2) + (newDistance1 + newDistance2)
    
    distances[key1] = newDistance2
    distances[key2] = newDistance1
    
    return entertainmentValue, distances

# List<Integer> -> List<String -> Integer -> Integer -> Integer
def iterationsBeforeStop(sorted_scores, solution, j, iters, maxScorePerRound):
    if sorted_scores[-1] - sorted_scores[-2] > maxScorePerRound * (len(solution) - 1 - j) and j+1 < iters:
        print('Winner cannot be caught after: ', j + 1, 'iterations', sorted_scores[-1], sorted_scores[-2], (maxScorePerRound * (len(solution) - 1 - j)))
        return j+1
    return iters

# List<String> -> List<String> -> List<List<Integer>> -> List<String> -> Integer
def getEntertainment(solution, countries, score_board, voters, maxScorePerRound):
    entertainmentValue = 0
    performing_countries = countries[:]
    current_solution = solution[:]
    
    distances = []
    iters = 37
    scores = [0] * 26
    for j in range(len(solution)):
        for i in range(len(countries)):
            v = voters.index(solution[j])
            scores[i] = scores[i] + score_board[i][v]
        otherMin = refinedMaxMin(scores, solution, j, maxScorePerRound)
        distance = max(scores) - otherMin
        # distance = max(scores) - min(scores)
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
