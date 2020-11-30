import time
from deck import Deck
from deck import Card
from deck import insertCardsIntoDeck


class Hand:

    # class variable for values of cards
    dict = {
        "A": [1, 11],
        "2": [2],
        "3": [3],
        "4": [4],
        "5": [5],
        "6": [6],
        "7": [7],
        "8": [8],
        "9": [9],
        "10": [10],
        "J": [10],
        "Q": [10],
        "K": [10]
    }

    # constructor
    def __init__(self, deck):
        self.cards = list()
        self.deck = deck

    # returns the list of cards in a hand
    def getCards(self):
        return self.cards

    # returns only the second card in a hand (used for the dealer's cards)
    def getCardsConceal(self):
        return self.cards[1]

    # calculate the value of the hand
    # this is a list of length one or two since aces have two values
    def totalValue(self):
        retVal = list()
        for x in self.cards:
            if(len(self.getValue(x)) == 2):
                if(len(retVal) == 0):
                    retVal.append(self.getValue(x)[0])
                    retVal.append(self.getValue(x)[1])
                elif(len(retVal) == 1):
                    retVal.append(self.getValue(x)[1] + retVal[0])
                    retVal[0] = self.getValue(x)[0] + retVal[0]
                else:
                    retVal[0] = retVal[0] + 1
                    retVal[1] = retVal[1] + 1
            else:
                if (len(retVal) == 1):
                    retVal[0] = retVal[0] + self.getValue(x)[0]
                elif (len(retVal) == 0):
                    retVal.append(self.getValue(x)[0])
                else:
                    retVal[0] = retVal[0] + self.getValue(x)[0]
                    retVal[1] = retVal[1] + self.getValue(x)[0]

        return retVal

    # calculates the value of a single card
    # returns a list of length one or two
    def getValue(self, card):
        return self.dict[card.number]

    # invoke a hit (draw a card and add it to the hand)
    def hit(self):
        self.cards.append(self.deck.drawCard())
        return self.cards


class Game:

    # constructor
    def __init__(self, deck):
        self.deck = deck
        self.player = Hand(self.deck)
        self.dealer = Hand(self.deck)
        self.mode = "player"
        self.shuffle = False

    # prints the status of the game
    def displayHands(self):

        clear = "\n" * 100
        print(clear)

        if(self.shuffle == True):
            print("Shuffling deck...\n")
            self.shuffle = False

        if (self.mode == "player"):
            print("Dealer shows:")
            print(self.dealer.getCardsConceal())
        else:
            print("Dealer shows " + str(self.dValue) + ":")
            print(self.dealer.getCards())

        print("\nYour hand " + str(self.pValue) + ":")
        print(self.player.getCards())

    # part of the game that the user interacts with
    # returns...
    # 0 if the game should continue
    # 1 if the player has won
    # 2 if the player has lost
    # 3 if the game is tied
    # 4 if there is a quit condition
    def playPlayer(self, option):

        # initial deal
        if (option == "0"):

            # shuffle deck if we're running out of cards
            # 18 is the max number of cards that could be used in a one deck game
            if (self.deck.position >= self.deck.numberOfCards - 18):
                self.deck.shuffleDeck()
                self.shuffle = True

            # alternate giving cards to player and dealer
            self.player.hit()
            self.dealer.hit()
            self.player.hit()
            self.dealer.hit()

            # calculate hand values
            self.pValue = self.player.totalValue()
            self.dValue = self.dealer.totalValue()

            # determine if there's an instant win condition
            if (len(self.dValue) == 2 and self.dValue[1] == 21):
                if (len(self.pValue) == 2 and self.pValue[1] == 21):
                    self.dValue.pop(0)
                    self.pValue.pop(0)
                    self.mode = "dealer"
                    self.displayHands()
                    print("It's a tie!")
                    return 3
                else:
                    self.dValue.pop(0)
                    self.mode = "dealer"
                    self.displayHands()
                    print("You lose!")
                    return 2
            if (len(self.pValue) == 2 and self.pValue[1] == 21):
                self.pValue.pop(0)
                self.mode = "dealer"
                self.displayHands()
                print("Blackjack! You win!")
                return 1

            self.displayHands()
            return 0

        # player hit
        elif (option == "1"):
            self.player.hit()

            self.pValue = self.player.totalValue()
            if (len(self.pValue) == 2 and self.pValue[1] > 21):
                self.pValue.pop(1)

            # if the player has a 21, skip turn and advance game
            for x in self.pValue:
                if (x == 21):
                    self.mode = "dealer"
                    if (len(self.pValue) == 2):
                        self.pValue.remove(self.pValue[0])
                    return self.playDealer()

            self.displayHands()
            if (self.pValue[0] > 21):
                self.mode = "dealer"
                self.displayHands()
                print("\nYou lose!")
                return 2

            return 0

        # player stay
        elif (option == "2"):
            self.mode = "dealer"
            if (len(self.pValue) == 2):
                self.pValue.remove(self.pValue[0])
            return self.playDealer()

        # player quit
        elif (option == "3"):
            return 4

        # unrecognized input
        else:
            return 4

    # the dealer's part of the game, invoked automatically from playPlayer
    # dealer stays on any 17 (including soft) and hits any lower number
    # win condition is returned to playPlayer and returned to the calling function
    def playDealer(self):

        self.dValue = self.dealer.totalValue()
        if (len(self.dValue) == 2 and self.dValue[1] > 21):
            self.dValue.remove(self.dValue[1])
        self.displayHands()

        for x in self.dValue:
            if (x >= 17 and x <= 21):
                if (self.pValue[0] > x):
                    print("\nYou win!")
                    return 1
                elif (self.pValue[0] < x):
                    print("\nYou lose!")
                    return 2
                else:
                    print("\nIt's a tie!")
                    return 3

        if (self.dValue[0] > 21):
            print("\nYou win!")
            return 1

        q = input("Press enter to continue...\n")
        self.dealer.hit()
        return self.playDealer()


def blackjack():
    # List of suits
    suits = ["♠", "♣", "♥", "♦"]

    # List of numbers
    numbers = ["A", "2", "3", "4", "5", "6",
               "7", "8", "9", "10", "J", "Q", "K"]

    # Create a deck
    deckOfCards = Deck()

    # Let user select the number of decks
    deckNum = input("\nHow many decks should we play with?\n> ")
    try:
        deckNumInt = int(deckNum)
        print("Playing with " + deckNum + " decks.")
    except ValueError:
        deckNumInt = 3
        print("\nInvalid number. Let's use 3.")

    time.sleep(3)

    # Load cards into the deck
    for x in range(1, deckNumInt + 1):
        insertCardsIntoDeck(suits, numbers, deckOfCards)

    # Shuffle them
    deckOfCards.shuffleDeck()

    # Set up variables for game statistics
    choice = "1"
    wins = 0
    losses = 0
    ties = 0

    # Let player start a new game repeatedly
    while (choice == "1"):
        game = Game(deckOfCards)
        inp = game.playPlayer("0")

        # inital deal, skip game loop if instant win
        if (inp == 0):

            # game loop
            while (inp == 0):
                q = input("\nWill you...\n(1) Hit\n(2) Stay\n(3) Quit\n> ")
                if (q != "1" and q != "2" and q != "3"):
                    q = "3"
                inp = game.playPlayer(q)

        # Update statistics
        if (inp == 1):
            wins += 1
        if (inp == 2):
            losses += 1
        if (inp == 3):
            ties += 1

        # Print statistics
        print("\nWins: " + str(wins) + " Losses: " +
              str(losses) + " Ties: " + str(ties))

        # Ask user if they will play again
        choice = input("\nPlay again?\n(1) Yes\n(2) No\n> ")

# Direct an immidiate call to deck.py to main()
if __name__ == "__main__":
    blackjack()
