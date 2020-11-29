import random
import time

colors = ['Red', 'Green', 'Blue', 'Yellow']
numbers = [1,2,3,4,5,6,7,8,9,0]

def uno():
    #A basic game of UNO against a computer opponent.
    #Not gonna bother giving the opponent a functional hand.
    #Single-draw, Player v Computer, 1v1, no special rules

    global pHandColor
    global pHandNumber
    pHandColor = [] #Your cards in terms of color
    pHandNumber = [] #Your cards in terms of numbers

    global oHandColor
    global oHandNumber
    oHandColor = [] #opponents cards in terms of color
    oHandNumber = [] #opponents cards in terms of numbers

    global currentColor
    global currentNumber

    pDeal(8)
    oDeal(8)

    #print(pHandColor)
    #print(pHandNumber)

    #showHand()

    currentColor = random.choice(colors)
    currentNumber = random.choice(numbers)

    #print("Current card:", currentColor, currentNumber)

    showCurrent(1)

    while len(pHandColor) >= 1:
        showHand()
        
        pPlay()

        showCurrent(3)

        time.sleep(0.5)

        if len(pHandColor) <= 0:
            print("You win!")
            showCurrent(4)
            time.sleep(2)
            break

        #x=0
        #for c in oHandColor:
        
        #    print(x, ":", c, oHandNumber[x])
        #    x=x+1

        oPlay()

        time.sleep(0.5)

        if len(oHandColor) <= 0:
            print("You lose!")
            showCurrent(5)
            time.sleep(2)
            break

        showCurrent(2)

    print("Good game!")
    time.sleep(2)
        
        
def oPlay():
    if currentColor not in oHandColor:
        if currentNumber not in oHandNumber:
            print("Opponent draws 1")
            oDeal(1)
            return


    x=0
    for color in oHandColor:
        
        if color == currentColor:
            oPlace(x)
            return
        else:
            #print("color mismatch:",oHandColor[x], currentColor)
            x=x+1

    x=0
    for number in oHandNumber:
        if number == currentNumber:
            oPlace(x)
            return
        else:
            #print("number mismatch:",oHandNumber[x], currentNumber)
            x=x+1

    print("ILLEGAL CARDS!")
    return

def pPlay():

    if currentColor not in pHandColor:
        if currentNumber not in pHandNumber:
            print("You have no valid cards to play, draw 1")
            pDeal(1)
            return
            

    cardNumber = int(input("Which of your cards do you play? > "))

    if cardNumber >= len(pHandColor):
        print("That is not a valid card")
        return pPlay()

    if currentColor == pHandColor[cardNumber]:
        print("That is a valid color")
        pPlace(cardNumber)
        return

    if currentNumber == pHandNumber[cardNumber]:
        print("That is a valid number")
        pPlace(cardNumber)
        return

    print("That is not a valid card")
    return pPlay()
    

def pPlace(number):
    global currentColor
    global currentNumber
    
    currentColor = pHandColor[number]
    currentNumber = pHandNumber[number]
    
    del pHandColor[number]
    del pHandNumber[number]

def oPlace(number):
    global currentColor
    global currentNumber
    
    currentColor = oHandColor[number]
    currentNumber = oHandNumber[number]
    
    del oHandColor[number]
    del oHandNumber[number]

def oDeal(number):

    for n in range(number):

        newColor = random.choice(colors)
        newNumber = random.choice(numbers)
        
        oHandColor.append(newColor)
        oHandNumber.append(newNumber)

        #print("Got a", newColor, newNumber)

def pDeal(number):

    for n in range(number):

        newColor = random.choice(colors)
        newNumber = random.choice(numbers)
        
        pHandColor.append(newColor)
        pHandNumber.append(newNumber)

        #print("Got a", newColor, newNumber)

        
def showHand():
    print("Opponent has", len(oHandColor),"cards")
    print("You have    ", len(pHandColor),"cards")
    print("Your hand:")
    x = 0
    for c in pHandColor:
        
        print(x, ":", c, pHandNumber[x])
        x=x+1

def showCurrent(state):
    switcher = {
        1: "Starting card: ",
        2: "Opponent played: ",
        3: "You played: ",
        4: "Winning play: ",
        5: "Losing play: ",
    }
    printed = (switcher.get(state, "Current card: "))
    print (printed, currentColor, currentNumber)

uno()
