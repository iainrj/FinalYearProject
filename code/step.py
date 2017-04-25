import support

def stepByStepSolution(score_board, countries, voters, maxScorePerRound):
    for p in range(37): # used for testing all solutions
        entertainmentValue = 0
        performing_countries = countries[:]
        solution = []
        voting_countries = voters[:]
        distances = []
        best = voting_countries[p]
        ignoredIndexes = []
        bestScores = [row[p] for row in score_board]
        solution.append(voting_countries[p])
        ignoredIndexes.append(p)
        distances.append(12)

        for k in range(1, len(voting_countries)): # go through and add to solution
            scores = bestScores[:]
            bestDistance = -1
            
            for j in range(len(voting_countries)): # go through all voters and try their votes as next
                local_scores = scores[:] # get base scores
                current_country = voting_countries[j]
                
                if j in ignoredIndexes: # ignore those youve already tried
                    continue

                for i in range(len(performing_countries)): # add on the votes from this country to all the participants
                    local_scores[i] = score_board[i][j] + local_scores[i]
                minScore = support.refinedMaxMin(local_scores, voting_countries, k, maxScorePerRound) # find the min for that with that voters round
                distance = max(local_scores) - minScore
                
                if distance < bestDistance or bestDistance < 0:
                    bestDistance = distance
                    best = current_country
                    bestScores = local_scores[:]
            ignoredIndexes.append(voting_countries.index(best))
            distances.append(bestDistance)
            solution.append(best)
        
        entertainmentValue = sum(distances)
        # entertainmentValue2, dist2  = support.getEntertainment(solution, countries, score_board, voters, maxScorePerRound)
        
        # print(entertainmentValue, (entertainmentValue == entertainmentValue2), entertainmentValue2)
        # print(distances)
        # print(dist2)
        

        print(solution, entertainmentValue) # used for testing all solutions
        # return (solution, entertainmentValue)
