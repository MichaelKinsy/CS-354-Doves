import CardGame_uno
import CardGame_blackjack

inp = "0"

while (inp != "3"):
    print("---- Game Center ----")
    inp = input("What game would you like to play?\n(1) Uno\n(2) Blackjack\n(3) Quit\n> ")
    if (inp == "1"):
        CardGame_uno.uno()
    if (inp == "2"):
        CardGame_blackjack.blackjack()