# Consider a standard 52-card deck shuffled uniformly at random. 
# Divide the deck into 13 piles of four cards each, and label the piles "Ace," "2," "3," ... "Queen," "King." 
# Note that the label of each pile is independent of its contents.

# With this setup, we're ready to play Clock Solitaire. 
# To start, select one of the piles. 
# Pick up the top card and view the card's rank. 
# Discard it to the side, and then draw your next card from the pile according to the rank you just saw. 
# Steps (2) and (3) are repeated until you either get stuck or win. 
# "Getting stuck" means you attempt to draw from a pile that is already empty, breaking the cycle and leaving you in a dead end. 
# "Winning" refers to drawing all 52 cards and never getting stuck.

# What is the probability that you win?

import numpy as np
def play_game():
    deck = list(range(52))
    np.random.shuffle(deck)
    shuffledDeck = deck
    cardsLeft = {i: 4 for i in range(13)}

    currentCard = np.random.randint(low=0, high=13)
    currentCardRank = currentCard
    cardsLeft[currentCardRank] = 3

    for _ in range(51): 
        # Compute next pile       
        newCardRank = shuffledDeck[currentCard] % 13

        # If no cards left in this pile, loss
        if cardsLeft[newCardRank] == 0:
            return 0
        
        # Update current card
        currentCard = (4 - cardsLeft[newCardRank]) * 13 + newCardRank
        # Update number of cards in pile
        cardsLeft[newCardRank] -= 1
        
    return 1

nSimulations = 100000

wins = 0
for _ in range(nSimulations):
    wins += play_game()

pWin = wins / nSimulations 
print(pWin)
    

