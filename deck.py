import random
from random import randrange

# Deck class that holds a collection of cards
class Deck:

    # Hold our collection of cards in a list
    cards = list()

    # Constructor for the deck
    def __init__(self):
        self.numberOfCards = 0  # Instance variable to keep track of how many cards are in the deck
        self.position = 0       # Instance variable to keep track of our position in the deck

    # Return the number of cards currently in the deck
    def displayNumberOfCards(self):
        return "There are " + str(self.numberOfCards) + "cards in the deck."

    # Insert a card into the deck
    def insert(self, card):
        self.cards.append(card) # Append to deck
        self.numberOfCards += 1 # Increment our count

    # Returns the list of all cards currently in the deck
    def displayDeck(self):
        return self.cards

    # Randomizes the order of cards in the deck
    def shuffleDeck(self):
        random.shuffle(self.cards)  # Uses the random module to shuffle the list
        self.position = 0           # Reset our position in the deck when we shuffle

    # Draws a card from the top of the deck
    def drawCard(self):
        retval = self.cards[self.position]
        self.position += 1
        return retval

    # Draws a card from the top of the deck, and then replaces it randomly back into the deck
    def drawAndReplace(self):
        retval = self.cards[self.position]
        self.position += 1
        self.cards.remove(retval)

        # Inserts the card at a random position in the deck
        self.cards.insert(randrange(len(self.cards) + 1), retval)
        return retval

# Card class that holds a card value and suit
class Card:

    # Constructor for a card
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    # "toString()" equivalent
    def __repr__(self):
        return str(self.suit) + " "  + str(self.number)

    # Returns the suit of a card
    def getSuit(self):
        return self.suit

    # Returns the value of a card
    def getNumber(self):
        return self.number

# Utility function to add every combination of cards from two lists into a deck
def insertCardsIntoDeck(suits, numbers, deck):
    for i in suits:
        for j in numbers:
            c = Card(i, j)
            deck.insert(c)


def main():

    # List of suits
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

    # List of numbers
    numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # Create a new deck
    deck1 = Deck()

    # Insert every combination of suits and numbers into the deck
    insertCardsIntoDeck(suits, numbers, deck1)

    # Make sure we have 52
    print(deck1.displayNumberOfCards())

    # Output the ordered deck
    print("Ordered deck:")
    print(deck1.displayDeck())
    print("---------------------------")

    # Shuffle the deck
    deck1.shuffleDeck()

    # Print the shuffled deck
    print("Shuffled deck:")
    print(deck1.displayDeck())
    print("---------------------------")

    # Draw a few cards
    print("Draw 1:", deck1.drawCard())
    print("Draw 2:", deck1.drawCard())
    print("Draw 3:", deck1.drawCard())

# Direct an immidiate call to deck.py to main()
if __name__ == "__main__":
    main()
