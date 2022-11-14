from const import PRINTED, SUITS, RANKS
from itertools import product
from random import shuffle


class Card:
    def __init__(self, suit, rank, picture, points):
        self.suit = suit
        self.rank = rank
        self.picture = picture
        self.points = points
        self.dec = Deck()

    def __str__(self):
        massege = self.picture + '\nPoints:' + str(self.points)
        return massege

class Deck:

    def __init__(self):
        self.cards = self._generate_deck()
        shuffle(self.cards)

    def _generate_deck(self):
        cards = []
        for suit, rank in product(SUITS, RANKS):
            if rank == "ace":
                points = 11
            elif rank.isdigit():
                points = int(rank)
            else:
                points = 10
            picture = PRINTED.get(rank)
            c = Card(suit=suit, rank=rank, points=points, picture=picture)
            cards.append(c)
        return cards

    def get_cart(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)
