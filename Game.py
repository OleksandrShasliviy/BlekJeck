import Player
from const import MESSAGES
from Deck import Deck
import random

class Game:

    def __init__(self):
        self.players = []
        self.player = None
        self.dealer = None
        self.all_players_count = 1
        self.deck = Deck()
        self.max_bet, self.min_bet = 20, 0

    @staticmethod
    def ask_starting(message):
        while True:
            choice = input(message)
            if choice == 'n':
                return False
            elif choice == 'y':
                return True


    def _launching (self):
        bot_counts = int(input('Hello, write bot count '))
        self.all_players_count = bot_counts + 1

        for i in range(bot_counts):
            # todoo pomenat
            b = Player.Bot(position=i)
            self.players.append(b)

            print(b, ' is created ')

            # todoo pomenat
        self.player = Player.Player(position=bot_counts + 1)


    def ask_bet(self):

    def start_game(self):
        message = MESSAGES.get("ask_start")
        if not self.ask_starting(message=message):
            exit(1)

        bot_counts = int(input('Hello, write bot count '))
        self.all_players_count = bot_counts + 1


        self._launching()

        self.ask_bet()



