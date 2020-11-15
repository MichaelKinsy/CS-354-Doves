import random
import math

print("This program will generate starting Dungeons and Dragons character stats using the standard 5th-edition generation method, assigning stat numbers randomly.")
name = input("Give your new character a name: ")

statlist = []
statmodlist = []
statnames = ("Strength","Dexterity","Constitution","Intellegence","Wisdom","Charisma")

for x in range(6):
    rolls = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    rolls.sort(reverse = True)
    print(statnames[x], "=", rolls,", dropping", rolls[3])
    stat = rolls[0] + rolls[1] + rolls[2]
    statlist.append(stat)

print("------------")
printed = name+"'s Stats (and Modifiers):"
print(printed)
for x in range(6):
    mod = math.floor((statlist[x] - 10)/2)

    modstr = str(mod)
    
    if mod > 0:
        modstr = "+" + modstr

    modstr = "("+modstr+")"

    statmodlist.append(modstr)
    
    print("  ",statnames[x], "=", statlist[x], modstr)

print("------------")
printed = name+"'s Ability Scores (without proficiencies):"
print(printed)

print("   Athletics:",statmodlist[0])
print("   Acrobatics, Sleight of Hand, Stealth:", statmodlist[1])
print("   Arcana, History, Investigation, Nature, Religion:", statmodlist[3])
print("   Animal Handling, Insight, Medicine, Perception, Survival:", statmodlist[4])
print("   Deception, Intimidation, Performance, Persuasion:", statmodlist[5])
