# *_*coding:utf-8 *_*
"""一摞python风格的纸牌"""
import collections
from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()
    suit_values = dict(spades=3, diamonds=2, clubs=1, hearts=0)

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def spades_high(self, card):
        rank_value = self.ranks.index(card.rank)
        return rank_value * len(self.suit_values) + self.suit_values[card.suit]


if __name__ == '__main__':
    beer_card = Card("7", "diamonds")
    print(beer_card)
    deck = FrenchDeck()
    print(len(deck))
    print(deck[0])
    print(deck[-1])

    print(choice(deck))
    print(deck[:3])
    print(deck[12:13])
    print(deck[12::13])

    for card in deck:
        print(card)
    for card in reversed(deck):
        print(card)
    print(Card("Q", "hearts") in deck)

    for card in sorted(deck, key=deck.spades_high):
        print(card)
