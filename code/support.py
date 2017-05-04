import random, numpy

# List<String> -> List<String>
def getInitialSolution(performers, score_board, voters, maxScorePerRound):
    # order that this method returns normally = 3824
    # order = ['Albania', 'Belarus', 'Poland', 'Russia', 'Armenia', 'Israel', 'Malta', 'FYR Macedonia', 'Denmark', 'Azerbaijan', 'Germany', 'San Marino', 'Moldova', 'Latvia', 'Finland', 'Montenegro', 'Hungary', 'Estonia', 'France', 'Romania', 'Iceland', 'Austria', 'Italy', 'Ukraine', 'Georgia', 'Lithuania', 'Norway', 'Sweden', 'Belgium', 'Greece', 'Ireland', 'Portugal', 'Slovenia', 'Spain', 'Switzerland', 'The Netherlands', 'United Kingdom']
    # return order
    # 2014 order = 3104
    # real_order = ['Azerbaijan','Greece','Poland','Albania','San Marino','Denmark','Montenegro','Romania','Russia','The Netherlands','Malta','France','United Kingdom','Latvia','Armenia','Iceland','FYR Macedonia','Sweden','Belarus','Germany','Israel','Portugal','Norway','Estonia','Hungary','Moldova','Ireland','Finland','Lithuania','Austria','Spain','Belgium','Italy','Ukraine','Switzerland','Georgia','Slovenia']
    # return real_order
    # solution piecemeal returns = 2571
    # piece = ['Austria', 'Armenia', 'Albania', 'Italy', 'Russia', 'San Marino', 'Malta', 'Azerbaijan', 'Poland', 'Belarus', 'United Kingdom', 'FYR Macedonia', 'Moldova', 'Denmark', 'Montenegro', 'Germany', 'Romania', 'Estonia', 'Finland', 'France', 'Ukraine', 'Latvia', 'Hungary', 'Georgia', 'Iceland', 'Belgium', 'Lithuania', 'Norway', 'Ireland', 'Israel', 'Sweden', 'Greece', 'Spain', 'Portugal', 'Slovenia', 'Switzerland', 'The Netherlands']
    # return piece
    # best = ['Belarus', 'Albania', 'Poland', 'United Kingdom', 'Montenegro', 'Armenia', 'Malta', 'Russia', 'Azerbaijan', 'Germany', 'San Marino', 'Italy', 'FYR Macedonia', 'Moldova', 'Estonia', 'Austria', 'Romania', 'Switzerland', 'Ukraine', 'Latvia', 'Denmark', 'Georgia', 'Hungary', 'Finland', 'Ireland', 'Norway', 'Greece', 'Spain', 'Israel', 'Portugal', 'Lithuania', 'France', 'Belgium', 'Iceland', 'Sweden', 'Slovenia', 'The Netherlands']
    # return best
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
    del sorted_scores[-1] # remove highest score
    roundsRemaining = (len(solution) - 1 - j)

    for score in sorted_scores:
        if score + (maxScorePerRound * roundsRemaining) <= currentTop:
            minScore = score
    return minScore

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
