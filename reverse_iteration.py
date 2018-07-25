_SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
_RANKS = tuple(range(2, 11)) + tuple('JQKA')

from collections import namedtuple

Card = namedtuple('Card', 'rank, suit')

class CardDeck:

    def __init__(self):
        self.length = len(_RANKS) * len(_SUITS)
    
    def __len__(self):
        return self.length
    
    def __iter__(self):
        return self.CardDeckIter(self.length)
    
    def __reversed__(self):
        return self.CardDeckIter(self.length, reverse=True)

    
    class CardDeckIter:

        def __init__(self, length, reverse=False):
            self.length = length
            self.i = 0
            self.reverse = reverse
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.i >= self.length:
                raise StopIteration
            else:
                if self.reverse:
                    index = self.length - 1 - self.i
                else:
                    index = self.i
                suit = _SUITS[index // len(_RANKS)]
                rank = _RANKS[index % len(_RANKS)]
                self.i += 1
                return Card(rank, suit)

deck  = reversed(CardDeck())
for card in deck:
    print(card)