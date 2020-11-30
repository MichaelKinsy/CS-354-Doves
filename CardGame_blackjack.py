import random
from random import randrange


class Deck:

    cards = list()

    def __init__(self):
        self.numberOfCards = 0
        self.position = 0

    def displayNumberOfCards(self):
        return "There are " + str(self.numberOfCards) + " cards in the deck."

    def insert(self, card):
        self.cards.append(card)
        self.numberOfCards += 1

    def displayDeck(self):
        return self.cards

    def shuffleDeck(self):
        random.shuffle(self.cards)
        self.position = 0

    def drawCard(self):
        retval = self.cards[self.position]
        self.position += 1
        return retval

    def getPos(self):
        return self.position

    def drawAndReplace(self):
        retval = self.cards[self.position]
        self.position += 1
        self.cards.remove(retval)

        self.cards.insert(randrange(len(self.cards) + 1), retval)
        return retval


class Card:

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __repr__(self):
        return str(self.suit) + " "  + str(self.number)

    def getSuit(self):
        return self.suit

    def getNumber(self):
        return self.number

    def getValue(self):
        retVal = list()
        try:
            retVal.append(int(self.number))
        except ValueError:
            if (self.number == "A"):
                retVal.append(1)
                retVal.append(11)
            else:
                retVal.append(10)
        return retVal


def insertCardsIntoDeck(suits, numbers, deck):
    for i in suits:
        for j in numbers:
            c = Card(i, j)
            deck.insert(c)


class Hand:

    def __init__(self, deck):
        self.cards = list()
        self.deck = deck

    def getCards(self):
        return self.cards

    def getCardsConceal(self):
        return self.cards[1]

    def totalValue(self):
        retVal = list()
        for x in self.cards:
            if(len(x.getValue()) == 2):
                if(len(retVal) == 0):
                    retVal.append(x.getValue()[0])
                    retVal.append(x.getValue()[1])
                elif(len(retVal) == 1):
                    retVal.append(x.getValue()[1] + retVal[0])
                    retVal[0] = x.getValue()[0] + retVal[0]
                else:
                    retVal[0] = retVal[0] + 1
                    retVal[1] = retVal[1] + 1
            else:
                if (len(retVal) == 1):
                    retVal[0] = retVal[0] + x.getValue()[0]
                elif (len(retVal) == 0):
                    retVal.append(x.getValue()[0])
                else:
                    retVal[0] = retVal[0] + x.getValue()[0]
                    retVal[1] = retVal[1] + x.getValue()[0]

        return retVal

    def hit(self):
        self.cards.append(self.deck.drawCard())
        return self.cards


class Game:
    def __init__(self, deck):
        self.deck = deck
        self.player = Hand(self.deck)
        self.dealer = Hand(self.deck)
        self.mode = "player"

    def displayHands(self):

        # print("------------------------------------")
        clear = "\n" * 100
        print(clear)

        if (self.mode == "player"):
            print("Dealer shows:")
            print(self.dealer.getCardsConceal())
        else:
            print("Dealer shows " + str(self.dValue) + ":")
            print(self.dealer.getCards())

        print("\nYour hand " + str(self.pValue) + ":")
        print(self.player.getCards())

    def playPlayer(self, option):

        # initial deal
        if (option == "0"):

            # shuffle deck if we're running out of cards
            # 18 is the max number of cards that could be used in a one deck game
            if (self.deck.getPos() >= 34):
                self.deck.shuffleDeck()
                print("\nShuffling deck...\n")

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
        if (option == "1"):
            self.player.hit()

            self.pValue = self.player.totalValue()
            if (len(self.pValue) == 2 and self.pValue[1] > 21):
                self.pValue.pop(1)

            self.displayHands()
            if (self.pValue[0] > 21):
                print("\nYou lose!")
                return 2

            return 0

        # player stay
        if (option == "2"):
            self.mode = "dealer"
            if (len(self.pValue) == 2):
                self.pValue.remove(self.pValue[0])
            return self.playDealer()

        # player quit
        if (option == "3"):
            return 4

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

    # Load cards
    insertCardsIntoDeck(suits, numbers, deckOfCards)

    # Shuffle them
    deckOfCards.shuffleDeck()

    choice = "1"

    wins = 0
    losses = 0
    ties = 0

    # repeat?
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

        if (inp == 1):
            wins += 1

        if (inp == 2):
            losses += 1

        if (inp == 3):
            ties += 1

        print("\nWins: " + str(wins) + " Losses: " +
              str(losses) + " Ties: " + str(ties))

        choice = input("\nPlay again?\n(1) Yes\n(2) No\n> ")
