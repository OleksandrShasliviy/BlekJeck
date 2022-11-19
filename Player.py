import abc
from Deck import Deck
class AbstratPlayer(abc.ABC):
    def __init__(self, position):
        self.cards = []
        self.position = position
        self.bet = 0




    def ask_card(self, deck):
        card = deck.get_cart()
        self.cards.append(card)
        return True


    @abc.abstractmethod
    def change_bet(self):
        pass


class Player(AbstratPlayer):


    def change_bet(self, max_bet, min_bet):
        while True:
            value = int(input('Make your bet: '))
            if value > max_bet and value < min_bet:
                self.bet = value
                break

class Dealer(AbstratPlayer):
    pass

#class Bot(AbstratPlayer):
 #   def __init__(self):
   #     pass