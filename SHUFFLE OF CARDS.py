#Program to shuffle a deck of cards.

import itertools, random
#Form a deck of cards.
deck=list(itertools.product(range(1,14),['Spade', 'Heart', 'Diamond', 'Club']))

#Shuffle the cards.
random.shuffle(deck)

#Draw five cards.
print("Your combination of cards is:")
for i in range(5):
    print(deck[i],[0], "of", deck[i][1])
