import random
import sys

print("Sup boi? Would you like some dice to throw? (yes or no)")
remark = input("> ")
while remark.upper() == "YES":
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print(f'''Yo boi, you've rolled a {die1} and a {die2}
    Dare ye roll once mo'?''')
    remark = input("> ")

if remark.upper() == "NO":
    print("well played, mi dearest boi boi")
else:
    print("HEYO, LEARN HOW TO ANSWER DA QUESTION!")
