import order

def stepByStepSolution(countries, score_board, voters):
    entertainmentValue = 0
    performing_countries = countries[:]
    solution = []
    voting_countries = voters[:]
    distances = [] # keep distances between min and max every round (len = 37)
    best = voting_countries[0]
    ignoredIndexes = []
    # scores[i] = score_board[i][voters.index(solution[j])] + scores[i]
    bestScores = [row[0] for row in score_board]
    solution.append(voting_countries[0])
    distances.append(12)

    for k in range(len(voting_countries) - 1):
        scores = bestScores[:]
        # if k == 3:
        #     print('scores', scores)
        #     exit()
        countries_tried = []
        bestDistance = -1
        ignoredIndexes.append(voting_countries.index(best))
        
        for j in range(len(voting_countries)):
            local_scores = scores[:]
            current_country = voting_countries[j]
            # print('ii', ignoredIndexes)
            # print('curr', current_country)
            if j in ignoredIndexes:
                # print('ignore me', j)
                continue
            for i in range(len(performing_countries)):
                local_scores[i] = score_board[i][j] + local_scores[i]
            otherMin = order.refinedMaxMin(local_scores, voting_countries, j)
            distance = max(local_scores) - otherMin
            
            if distance < bestDistance or bestDistance < 0:
                bestDistance = distance
                best = current_country
                bestScores = local_scores[:]
            countries_tried.append(current_country)
        distances.append(bestDistance)
        solution.append(best)
    # print(solution, distances)
    entertainmentValue = sum(distances)
 
    return solution, entertainmentValue
    
if __name__ == '__main__':
    
    PERFORMING_COUNTRIES = ['Ukraine','Belarus','Azerbaijan','Iceland','Norway','Romania','Armenia','Montenegro','Poland','Greece','Austria', 'Germany','Sweden','France','Russia','Italy','Slovenia','Finland','Spain','Switzerland','Hungary','Malta','Denmark','The Netherlands', 'San Marino','United Kingdom']
    # Eurovision 2014 scoreboard. 1st column is Albania's vote, 2nd column is Armenia's vote, etc.
    VOTING_COUNTRIES = ['Albania', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Denmark', 'Estonia', 'FYR Macedonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Israel', 'Italy', 'Latvia', 'Lithuania', 'Malta', 'Moldova', 'Montenegro', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'The Netherlands', 'Ukraine', 'United Kingdom']
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

    print(stepByStepSolution(PERFORMING_COUNTRIES, SCOREBOARD, VOTING_COUNTRIES))
