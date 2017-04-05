import support

def stepByStepSolution(score_board, countries, voters, maxScorePerRound):
    entertainmentValue = 0
    performing_countries = countries[:]
    solution = []
    voting_countries = voters[:]
    distances = []
    best = voting_countries[0]
    ignoredIndexes = []
    bestScores = [row[0] for row in score_board]
    solution.append(voting_countries[0])
    distances.append(12)

    for k in range(len(voting_countries) - 1):
        scores = bestScores[:]
        countries_tried = []
        bestDistance = -1
        ignoredIndexes.append(voting_countries.index(best))
        
        for j in range(len(voting_countries)):
            local_scores = scores[:]
            current_country = voting_countries[j]
            if j in ignoredIndexes:
                continue
            for i in range(len(performing_countries)):
                local_scores[i] = score_board[i][j] + local_scores[i]
            otherMin = support.refinedMaxMin(local_scores, voting_countries, k, maxScorePerRound)
            distance = max(local_scores) - otherMin
            
            if distance < bestDistance or bestDistance < 0:
                bestDistance = distance
                best = current_country
                bestScores = local_scores[:]
            countries_tried.append(current_country)
        distances.append(bestDistance)
        solution.append(best)
    entertainmentValue = sum(distances)
 
    return solution, entertainmentValue
