import random
import time

colors = ['Red', 'Green', 'Blue', 'Yellow']
numbers = [1,2,3,4,5,6,7,8,9,0]

def unoSingle():
    #A basic game of UNO against yourself
    #Single-draw, Player solitaire style, no special rules

    global pHandColor
    global pHandNumber
    pHandColor = []
    pHandNumber = []

    global currentColor
    global currentNumber

    pDeal(8)

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

    print("You win!")
    showCurrent(4)
    time.sleep(5)
        

def pPlay():

    if currentColor not in pHandColor:
        if currentNumber not in pHandNumber:
            print("No valid cards, draw 1")
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

def pDeal(number):

    for n in range(number):

        newColor = random.choice(colors)
        newNumber = random.choice(numbers)
        
        pHandColor.append(newColor)
        pHandNumber.append(newNumber)

        #print("Got a", newColor, newNumber)

        
def showHand():
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

unoSingle()
