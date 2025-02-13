# Simulate following game

# Flip a fair coin 100 times-it gives a sequence of heads (H) and tails (T). For each HH in the sequence of flips, Alice gets a point; for each HT, Bob does, so e.g. for the sequence THHHT Alice gets 2 points and Bob gets 1 point. Who is most likely to win?

import numpy as np
import random


def roll_dice(n):
    '''
    Roll a fair dice n times and return the sequence of the rolls
    Input: n (int) - number of rolls
    Output: rolls (array): sequence of rolls
    '''

    # Create random number generator
    rng = np.random.default_rng()
    # Generate n random integers between 0 and 1 (2 would be exclusive)
    rolls = rng.integers(0, 2, size=n)
    
    return rolls

def count_points(rolls):
    '''
    Count the number of points for Alice and Bob
    Input: rolls (array): sequence of rolls
    Output: alice_points (int): number of points for Alice
            bob_points (int): number of points for Bob
    '''
    alice_points = 0
    bob_points = 0
    for i in range(len(rolls)-1):
        if rolls[i] == 1 and rolls[i+1] == 1:
            alice_points += 1
        elif rolls[i] == 1 and rolls[i+1] == 0:
            bob_points += 1

    return alice_points, bob_points

def simulate_game(n):
    '''
    Simulate the game of flipping a fair coin n times
    Input: n (int) - number of flips
    Output: alice_points (int): number of points for Alice
            bob_points (int): number of points for Bob
    '''
    rolls = roll_dice(n)
    alice_points, bob_points = count_points(rolls)
    return alice_points, bob_points


# Now we simulate the previous game N times and count the number of times Alice (resp Bob) wins
N = 1000000

n = 100

alice_wins = 0
bob_wins = 0
draws = 0
for _ in range(N):
    alice_points, bob_points = simulate_game(n)
    if alice_points > bob_points:
        alice_wins += 1
    elif bob_points > alice_points:
        bob_wins += 1
    else:
        draws += 1

print(f"Alice wins {alice_wins/N*100}% of the time")
print(f"Bob wins {bob_wins/N*100}% of the time")
print(f"There are {draws/N*100}% draws")

