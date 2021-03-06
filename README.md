# Final Year Project
## Maximising entertainment value in the vote-reveal problem

In many elections or competitions, a set of voters will rank a set of candidates from best to worst, or will give scores to some of the candidates, with the winner then being the candidate that gets the highest total number of points. When it comes to revealing the result after all votes have been cast, some competitions proceed by having a roll-call of all the voters in which each announces their own scores. This is often done for entertainment purposes such as in the Eurovision Song Contest.

The concept of entertainment, especially with respect to competition, is heavily subjective subject and as such is hard to quantify in simple terms. There are intuitive constituent parts to an entertaining competition (like Eurovision) such as, if the winner is known early or late, and how many teams are in the running to win. A large constituent part of this project will be to convert these intuitive ideas into mathematical values that can then be maximised by some optimisation algorithm. 

The two main questions that this project will aim to answer are:

- How can we define the concept of ''entertainment'' in the context of an optimisation problem, and hence try to maximise it.
- In which order should the votes be revealed in order to maximise that entertainment value?

# Running the code
## Code was run using Python 2.7.10 however should also work with other Python versions
## Will run either Greedy Search, Simulated Annealing, Brute Force or Step-by-step algorithm and return an order of voting and a value for entertainment
``` bash
> cd code
> python order.py <greedy|brute|simAnnealing|step> <number of runs of algorithm>
```

# Running the tests
``` bash
> cd code
> python orderTest.py
```

# Viewing the visualisation locally
### You must have Node (and npm) installed locally
``` bash
> cd visualisation
> npm install
> npm start
* follow the instruction on-screen
```
