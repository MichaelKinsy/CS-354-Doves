import random

print("Roll a set of dice.")
strnumber = input("How many dice? > ")
max = input("How many sides do the dice have? > ")

printout = str(strnumber)+'d'+str(max)
print("rolling",printout)

total = 0
number=int(strnumber)

for x in range(number):
    y = int(random.randint(1,int(max)))
    print(y)
    total = total + y

print("total:", total)
