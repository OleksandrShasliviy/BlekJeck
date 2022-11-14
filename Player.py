import abc
from Deck import Deck
class AbstratPlayer(abc.ABC):
    def __init__(self, position):
        self.cards = []
        self.position = position




    def ask_card(self, deck):
        card = deck.get_cart()
        self.cards.append(card)
        return True

class Player(AbstratPlayer):
    pass

class Dealer(AbstratPlayer):
    pass

#class Bot(AbstratPlayer):
 #   def __init__(self):
   #     pass