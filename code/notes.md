# Code notes

## Algorithms
- Greedy search
    - Finds a solution in a reasonable time
    - not convinced that it is the optimal or at least near optimal solution
- Brute force
    - Left to run for ~8 hours and could only find one solution better than the initial solution
    - Searching all solutions (37!) would take about 1.2x10^40 seconds, so is infeasible
- Simulated Annealing
    - Finds a better solution than greedy search, every time
    - Takes longer to run and come up with a solution
    - Solutions range around 2550
- Step by step
    - Same solution returned every time
    - Very fast (< 1 second)
    - Solution has score of 2777
    
## refinedMaxMin
- gives a lower value by virtue of the fact that it only calculates with minimum score that can still win
    - need another way of comparing algorithms?
- chart of difference between just minimum and refinedMin below

![difference](https://raw.githubusercontent.com/iainrj/FinalYearProject/master/code/difference_MinvsRefinedMin.png)

## Full re-calculation vs partial re-calculation
- after finding a neighbour of a given solution, the entertainment value of that solution must be found
- by swapping 2 adjacent countries in the solution a partial re-calculation of the entertainment value can be done using the entertainment value of the previous solution
- a full calculation of the entertainment value in this problem always involves:
    - 37 * 26 = 962 score calculations (37 = number of voters, 26 = number of participants)

- as the previous solution and the new solution only differ by one position it is possible to only partially re-calculate the entertaiment
- entertainment is the sum of the distances between the first place and the last who can still win
- re-calculation involves removing the distances for the two rounds of the swapped countries in the old solution and adding them back in their new positions in the new solution
    - equation for this is:
        - `oldEntertainmentValue - oldDistances + newDistances`
    - the oldEntertainment and oldDistances can be found by keeping them from the old solution and passing them into the entertainment calculation function
    - the newDistances must still be re-calculated however only up to the index of the second country
    - this means that the partial entertainment calculation will involve:
    - Max => 37 * 26 = 962 score calculations (same as full)
    - Min => 2 * 26 = 52 score calculations
    - Average => 18 * 26 = 468 score calculations
    
- chart of average running time of full and partial entertainment calculations below

![reducedvsfulldistancecalc](https://cloud.githubusercontent.com/assets/6751845/24546254/4f969150-1602-11e7-851d-292d1d174a99.png)

    
