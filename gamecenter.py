import CardGame_uno
import CardGame_blackjack
import CardGame_war

inp = "0"

while (inp != "4"):
    print("---- Game Center ----")
    inp = input("What game would you like to play?\n(1) Uno\n(2) Blackjack\n(3) War\n(4) Quit\n> ")
    if (inp == "1"):
        CardGame_uno.uno()
    elif (inp == "2"):
        CardGame_blackjack.blackjack()
    elif (inp == "3"):
        CardGame_war.playWar()
    else:
        inp = "4"