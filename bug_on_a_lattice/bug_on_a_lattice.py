'''
A problem from the BRILLIANT applied probability course.
A bug starts at a random point of the lattice.
Each point is equally likely to be the starting point.
Every minute the bug selects an adjacent point at random and moves to it.
Each adjacent point is equally likely to be chosen.
What is the probability that the bug gets to point A in 2 moves or less.

Date: 6/30/2020
'''

import random

def main():
    # create the lattice object
    lattice = {'B': ['A', 'G', 'C'], 'C': ['B', 'G', 'D'], 'D': ['C', 'G', 'E'],
            'E': ['D', 'G', 'F'], 'F': ['E', 'G', 'A'], 'G': ['A', 'B', 'C', 'D', 'E', 'F'], 'A' : []}

    wins = 0
    n_sims = 300000 # number of simulations

    # run the simulation
    for i in range(n_sims):
        start_point = random.choice(lattice.keys()) # the bug's starting point
        if start_point == 'A':
            wins += 1
            continue
        # bug's position after the first move
        first_point = random.choice(lattice.get(start_point))
        if first_point == 'A':
            wins += 1
            continue
        # bug's position after the second move
        second_point = random.choice(lattice.get(first_point)) # bug's position after second move
        if second_point == 'A':
            wins += 1


        #print lattice.get(start_point)
        #print first_point
        #print lattice.get(first_point)
        #print second_point

    print 'The probability of the bug getting to point A in less than 2 moves or less is {}'.format(round(float(wins)/n_sims, 4))

if __name__ == '__main__':
    main()
