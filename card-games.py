class PlayingCard:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        return

    def __repr__(self):
        return "%s" % (self.rank, self.suit)


class DeckOfCards:

    def __init__(self):
        card_suits = ['H','D','C','S']
        card_ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.deck = []
        for suit in card_suits:
            for rank in card_ranks:
                self.deck.append(PlayingCard(suit, rank))
        for colour in ["Red","Black"]:
            self.deck.append(PlayingCard(colour, "Joker"))

    def __repr__(self):
        return "Deck(%s)" % self.deck



deck = DeckOfCards()
print(deck)


# class Bataille:
