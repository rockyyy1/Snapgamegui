import random
import copy

class Card:
    def __init__(self, value, suit):
        """
        A class representing a playing card.

        Attributes:
            value (str): The value of the card, such as "A" or "5".
            suit (str): The suit of the card, such as "Hearts" or "Diamonds".

        Methods:
            __repr__(self): Returns a string representation of the card.
        """
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class DeckOfCards:
    def __init__(self):
        """Using the Card class, creates list of 52 cards, 13 (2-A) from each suit (Hearts, Diamonds, Spades, Clubs)
        
        Args:
        None

        Returns:
        cards (list): A list of 52 Card objects.
        """
        valueList = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        suitList = ["Hearts", "Diamonds", "Spades", "Clubs"]    
        self.cards = []
        for suit in suitList:
            for value in valueList:
                card = Card(value, suit)
                self.cards.append(card)

    def display_deck(self):
        """Prints a list of cards
        
        Args: 
        cards (list) - list of cards
        
        Returns:
        None
        """
        for card in self.cards:
            print(card)
        
    def shuffle(self):
        """Shuffles list of cards randomly
        
        Args:
        cards (list) - list of cards to shuffle
        
        Returns:
        None
        """
        random.shuffle(self.cards)

    def deal(self, players):
        """Randomly distrubutes cards equally to given number of players
        
        Args:
        players (int) - the number of players
        
        Returns:
        hands (list) - list of cards given to each player
        """
        #create the number of players' hands
        hands = []
        for i in range(players):
            hands.append([])
            
        #how many cards each player should receive, ignoring the remainder
        cards_per_player = len(self.cards) // players
        
        #distribute equal number of cards to each player
        for player_hand in hands:
            for i in range(cards_per_player):
                random_index = random.randrange(len(self.cards))
                card = self.cards.pop(random_index)
                #card = self.cards.pop(0)
                player_hand.append(card)
                
        player_number = 1
        for player_hand in hands:
            print(f"Player {player_number}:", player_hand)
            player_number += 1
        print()        
        return(hands)

class Player(DeckOfCards):
    """Initializes a Player object.
    
    Methods:
    snap() - plays a game of snap
    """
    def __init__(self):
        DeckOfCards.__init__(self)
        
    def snap(self, number_of_players):
        """
        Plays a game of Snap.

        Args:
            number_of_players (int): The number of players in the game.
        """
        central_pile = []
        play = self.deal(number_of_players)
        cards_list = copy.deepcopy(play)
        
        player = 1
        turn = 1
        all_players_have_cards = True
        
        def add_cards():
            ##if you want a random player to yell snap and get all the cards:
            print(f"PLAYER {random_player+1} YELLS SNAP over the {central_pile[-2]} and collects {len(central_pile)} cards")
            for cards in range(len(central_pile)):
                random_players_cards.append(central_pile.pop(-1))

            #if you want the player who just placed down the card to yell snap and get all the cards:
            #print(f"PLAYER {player} YELLS SNAP over the {central_pile[-2]} and collects {len(central_pile)} cards")
            #for cards in range(len(central_pile)):
            #    i.append(central_pile.pop(-1))

        def check_player_card_count(hand):
            cards_in_hand = len(hand)
            if cards_in_hand == 0:
                return False
            else:
                return True
                
        while all_players_have_cards:
            for i in play:
                random_player = random.randint(1,3)
                random_players_cards = play[random_player]
                #remove from players hand and into central pile
                if len(i) > 0:
                    #print(f"\nTurn #{turn} Player {player} flips over the", i[0])
                    turn += 1
                    central_pile.append(i[0])
                    i.pop(0)
                    all_players_have_cards = check_player_card_count(i)
                    if all_players_have_cards == False:
                        #print(f"Player {player} has run out of cards!")
                        break
                    
                #check to see if the central pile's top two cards are identical
                # if len(central_pile) > 1:
                #     if central_pile[-1].value == central_pile[-2].value:
                #         add_cards()
        
                player += 1
                if player > number_of_players:
                    player = 1
            
                # print("Central pile:", central_pile)
                # print()
                # player_count = 1
                # for i in play:
                #     print(f"Player {player_count}:", i)
                #     player_count += 1
                
        card_counts = []
        for i in play:
            card_counts.append(len(i))
        winner = 0
        most_cards = 0
        for i in range(len(card_counts)):
            if card_counts[i] > most_cards:
                most_cards = card_counts[i]
                winner = i + 1
        #print(f"Player {winner} has won the game with {most_cards} cards!")
        
        return cards_list
    
def main():
    # deck.shuffle()
    # deck.display_deck()
    # deck = DeckOfCards()
    play = Player()
    play.snap(4)

if __name__ == "__main__":
    main()
