#------------------------------------------------
#This program plays a automated game of war between "you"
# and the computer. Once the program begins it will split
# the deck in half and give each half to both players then draw a card off
# the top of each pile. The program then prints off both players cards
# and whoever has a higher number card or wins the war wins.
# The amount of cards the winner has are printed off.
#------------------------------------------------

#------------------------------------------------
#This program plays a automated game of war between "you"
# and the computer. Once the program begins it will split
# the deck in half and give each half to both players then draw a card off
# the top of each pile. The program then prints off both players cards
# and whoever has a higher number card or wins the war wins.
# The amount of cards the winner has are printed off.
#------------------------------------------------

import deck as d
import  random as r


# List of suits
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

# List of numbers
numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]





def deal(deck,players):
    hand = 25
    count = 0
    while count <= hand:
        c = deck.drawCard()
        c2 = deck.drawCard()
        players[0]["Cards"].append(c)
        players[1]["Cards"].append(c2)
        players[0]["Count"] = players[0]["Count"] + 1
        players[1]["Count"] = players[1]["Count"] + 1
        count += 1
    # print(players[0]["Count"])
    # print(players[1]["Count"])    

def compare(card1,card2):
    if(card1.getNumber() == card2.getNumber()):
        return 0
    else:
        count1 = 0
        count2 = 0
        for i in numbers:
            if i == card1.getNumber():
                count1 = numbers.index(i)
            if i == card2.getNumber():
                count2 = numbers.index(i)
        if count1 > count2:
            return 1
        else:
            return 2
def gameOver(players):
    over = False
    if len(players[0]["Cards"]) == 0:
        over = True
        print("You have won!!!")
    elif len(players[1]["Cards"]) == 0:
        over = True
        print("You have lost...")
    return over 

def war(players,cards1,cards2):
    if gameOver(players):
        return
    if(len(players[0]["Cards"]) >= 1):
        cards1.append(players[0]["Cards"].pop(0))
        players[0]["Count"] = players[0]["Count"] - 1  
    if(len(players[0]["Cards"]) >= 1):
        cards1.append(players[0]["Cards"].pop(0))
        players[0]["Count"] = players[0]["Count"] - 1 
    
    if(len(players[1]["Cards"]) >= 1):
        cards2.append(players[1]["Cards"].pop(0))
        players[1]["Count"] = players[1]["Count"] - 1 
    if(len(players[1]["Cards"]) >= 1):
        cards2.append(players[1]["Cards"].pop(0))
        players[1]["Count"] = players[1]["Count"] - 1  

    res = compare(cards1[len(cards1)-1],cards2[len(cards2)-1])

    if res == 0:
        war(players,cards1,cards2)
    elif res == 1:
        for i in cards1:
            players[0]["Cards"].append(i)
            players[0]["Count"] = players[0]["Count"] + 1 
        for i in cards2:
            players[0]["Cards"].append(i)
            players[0]["Count"] = players[0]["Count"] + 1 
    else:
        for i in cards1:
            players[1]["Cards"].append(i)
            players[1]["Count"] = players[1]["Count"] + 1 
        for i in cards2:
            players[1]["Cards"].append(i)
            players[1]["Count"] = players[1]["Count"] + 1      

def play(players):
    while not gameOver(players):
        turn = r.randint(0,1)
        c1 = players[0]["Cards"].pop(0)
        players[0]["Count"] = players[0]["Count"] - 1 
        c2 = players[1]["Cards"].pop(0)
        players[1]["Count"] = players[1]["Count"] - 1 
        res = compare(c1,c2)
        print("Your Card: ",c1," My Card: ",c2)
        if res == 0:
            print("War!")
            cards1 = [c1]
            cards2 = [c2]
            war(players,cards1,cards2)
        elif res == 1:
            if turn == 0:
                players[0]["Cards"].append(c1)
                players[0]["Cards"].append(c2)
            else:
                players[0]["Cards"].append(c2)
                players[0]["Cards"].append(c1)                
            players[0]["Count"] = players[0]["Count"] + 2 
            print("You have ", players[0]["Count"], "Cards")
        else:
            if turn == 0:
                players[1]["Cards"].append(c1)
                players[1]["Cards"].append(c2)
            else:
                players[1]["Cards"].append(c2)
                players[1]["Cards"].append(c1)                
            players[1]["Count"] = players[1]["Count"] + 2 
            print("I  have ", players[1]["Count"], "Cards")

def playWar():
    deck = d.Deck()
    d.insertCardsIntoDeck(suits, numbers, deck)
    # Shuffle the deck
    deck.shuffleDeck()
    player = {"Cards":[],"Count":0}
    computer = {"Cards":[],"Count":0}
    players = [player,computer]
    deal(deck,players)
    play(players)
