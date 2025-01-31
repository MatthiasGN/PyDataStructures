import random

# Practice as a Python refresher for classes.

class PlayingCard:

    card_ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A','Joker']
    card_suits = ['H','D','C','S']
    joker_colours = ['R','B']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        return

    def __repr__(self):
        return f"{self.rank}{self.suit}"
    
    def __gt__(self, card2):
        return self.card_ranks.index(self.rank) > self.card_ranks.index(card2.rank)
    
    def __lt__(self, card2):
        return self.card_ranks.index(self.rank) < self.card_ranks.index(card2.rank)
    
    def __eq__(self, card2):
        return self.card_ranks.index(self.rank) == self.card_ranks.index(card2.rank)
    

class DeckOfCards:

    def __init__(self):
        self.deck = []
        for rank in PlayingCard.card_ranks:
            if rank == "Joker":
                for colour in PlayingCard.joker_colours:
                    self.deck.append(PlayingCard(rank, colour))
            else:
                for suit in PlayingCard.card_suits:
                    self.deck.append(PlayingCard(rank, suit))

    def __repr__(self):
        return f"Deck{self.deck}"
    
    def shuffle(self):
        random.shuffle(self.deck)

    def draw_card(self) -> PlayingCard:
        return self.deck.pop()
    
    def __len__(self):
        return len(self.deck)


class HandOfCards:

    def __init__(self, hand=None):
        if hand == None:
            self.hand = []
        else:
            self.hand = hand

    def __repr__(self):
        return f"{self.hand}"

    def __len__(self):
        return len(self.hand)
    
    def add_card(self, card: PlayingCard):
        self.hand.append(card)

    def random_card(self) -> PlayingCard:
        return random.choice(self.hand)

    def play_card(self, card: PlayingCard):
        return self.hand.remove(card)


class CardGame:

    def __init__(self, num_players=2):
        self.deck = DeckOfCards()
        self.hands = []
        for i in range(num_players):
            self.hands.append(HandOfCards())

    def __repr__(self):
        return f"{self.deck}\n{self.hands}"


class Bataille(CardGame):

    def __init__(self):
        super().__init__(2)
        self.deck.shuffle()

        hand_ctr = 0
        while len(self.deck) > 0:
            self.hands[hand_ctr].add_card(self.deck.draw_card())
            hand_ctr += 1
            if hand_ctr == 2:
                hand_ctr = 0

    def __repr__(self):
        repr = f"{self.deck}"
        for i, hand in enumerate(self.hands):
            repr += f"\n Player{i+1}{hand}"
        return repr
    
    def play_round(self):
        play = []
        round_winner = -1

        for player in self.hands:
            card = player.random_card()
            player.play_card(card)
            play.append(card)

        print(f"Player 1: {play[0]}, Player 2: {play[1]}.")

        # If player 1's card is stronger than player 2's, player 1 wins
        if play[0] > play[1]:
            round_winner = 0

        # If player 1's card is weaker than player 2's, player 2 wins
        elif play[0] < play[1]:
            round_winner = 1
        
        # If player 1's card is equal to player 2's, BATAILLE!
        while play[-2] == play[-1]:
            if len(play) > 6:
                print(f"~~~~~~~~~~~~~~Bataille d'Attrition!~~~~~~~~~~~~~~~~")

            print(f"Bataille!")
            for i in range(2):
                if len(self.hands[i]) < 2:
                    print(f"Player {i} ran out of cards!")
                    round_winner = i-1
                    break

            for i in range(2):
                for player in self.hands:
                    card = player.random_card()
                    player.play_card(card)
                    play.append(card)

            print(f"Player 1: ", end="")
            for card in play[:-3:4]:
                print(f"{card} | ? | ", end="")
            print(f"{play[-2]}")
            
            print(f"Player 2: ", end="")
            for card in play[1:-3:4]:
                print(f"{card} | ? | ", end="")
            print(f"{play[-1]}")
            

            if play[-2] > play[-1]:
                round_winner = 0

            elif play[-2] < play[-1]:
                round_winner = 1

        # The winning player takes the cards.
        while len(play) > 0:
            self.hands[round_winner].add_card(play.pop())

        print(f"Player {round_winner+1} collects the cards.\n")

    def play_interactive(self):
        while input("Press Enter to play the next round.") == "":
            if len(self.hands[0]) == 0:
                print("Player 2 wins!")
                print(bataille)
                break
            elif len(self.hands[1]) == 0:
                print("Player 1 wins!")
                print(bataille)
                break
            self.play_round()
                

        
        
         
bataille = Bataille()
print(bataille)
print()

bataille.play_interactive()



# deck = DeckOfCards()
# print(deck)
# deck.shuffle()
# print(deck)
