# You are given an integer array deck. There is a deck of cards where every card has a unique integer. The integer on the ith card is deck[i].
# You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.
# You will do the following steps repeatedly until all cards are revealed:
# Take the top card of the deck, reveal it, and take it out of the deck.
# If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.
# If there are still unrevealed cards, go back to step 1. Otherwise, stop.
# Return an ordering of the deck that would reveal the cards in increasing order.
# Note that the first entry in the answer is considered to be the top of the deck.
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        if len(deck) == 1:
            return deck
        deck.sort()
        deck_save = deck.copy()
        cards = {}
        take = True
        ind = 0
        while len(deck) > 0:
            if take:
                take = False
                cards[deck[0]] = deck_save[ind]
                ind += 1
                del deck[0]
            else:
                take = True
                elem = deck[0]
                del deck[0]
                deck.append(elem)
        return [cards[card] for card in deck_save]
