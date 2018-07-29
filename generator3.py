from collections import namedtuple

Card = namedtuple('Card', 'rank suit')
SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
RANKS = tuple(range(2, 11)) + tuple('JQKA')

"""
suit_index = card_index // len(RANKS)
rank_index = card_index % len(RANKS)
"""
def card_gen():
    for i in range(len(RANKS) * len(SUITS)):
        suit = SUITS[i // len(RANKS)]
        rank = RANKS[i % len(RANKS)]
        card = Card(rank, suit)
        yield card

for card in card_gen():
    print(card)

def card_gen1():
    for suit in SUITS:
        for rank in RANKS:
            yield Card(rank, suit)

for card in card_gen1():
    print(card)

#implementing as an iterable

from collections import namedtuple

class CardDeck:

    Card = namedtuple('Card', 'rank suit')
    SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
    RANKS = tuple(range(2, 11)) + tuple('JQKA')

    def __iter__(self):
        return CardDeck.card_gen()
    
    def __reversed__(self):
        return CardDeck.reverse_card_gen()
    
    @staticmethod
    def card_gen():
        for suit in CardDeck.SUITS:
            for rank in CardDeck.RANKS:
                yield CardDeck.Card(rank, suit)
    
    @staticmethod
    def reverse_card_gen():
        for suit in reversed(SUITS):
            for rank in reversed(RANKS):
                yield CardDeck.Card(rank, suit)

deck = CardDeck()
print(list(deck))

deck = CardDeck()
print(list(reversed(deck)))