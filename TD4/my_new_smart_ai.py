"""
Artificial Intelligence to play Hanabi.
"""

import itertools
import random

class AI:
    """
    AI base class: some basic functions, game analysis.
    """
    def __init__(self, game):
        self.game = game

    @property
    def other_hands(self):
        "The list of other players' hands."
        return self.game.hands[1:]

    @property
    def other_players_cards(self):
        "All of other players's cards, concatenated in a single list."
        # return sum([x.cards for x in self.other_hands], [])
        return list(itertools.chain.from_iterable([hand.cards for hand in self.other_hands]))


class Idiot(AI):

    def play(self):
        game = self.game
        if game.blue_coins <= 0:
            n = randint(1,2)
        else:
            n = randint(1,3)

        if n==1:
            i = randint(1,5)
            print('Idiot would discard: card ',i)
            return "d%d"%i

        if n==2:
            i = randint(1,5)
            print('Idiot would play: card ',i)
            return "p%d"%i


        if n==3:
            i = randint(1,2)
            clue = randint(1,5)
            couleur = {1:'R', 2:'G', 3:'B', 4:'W', 5:'Y'}
            if i==1:
                clue = "c%s"%couleur[clue]
            else:
                clue = "c%d"%clue
            print('Idiot would clue: ', clue)
            return clue
