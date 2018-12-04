import sys
import random

def instructions():
    print('''Welcome to Dart Math!
This program is designed to let you practice your mental
addition/subtraction so you don't make a fool
out of yourself come game time!

Here are the accepted commands from the main prompt:

help - provides instructions for the game.
start - initiates the game play.
high score - allows you to view your previously held high scores. Scores are
based upon how many of the questions you got right and how long it took you to
calculate the correct response.
------------------------------

''')
    start()
def continu():
    cont = input('''

    Would you like to continue?\n>''')
    if cont.lower() in ['yes','y','yeah','mhm','yez']:
        p1.throw_dart()
    else:
        print("BYE BYE!")
        quit(0)

class Score(object):

    def __init__(self):
        self.total = [300.0]
       

    def total_score(self):
        return self.total[0]

    def cur_score(self):
        return self.total[-1]

    def sub_from_total(self, round_score):
        self.total.append(self.total_score() - round_score)
        print("Now what is your new total?")
        new_total = int(input("> "))
        while new_total != self.cur_score():
            print("Try again!")
            new_total = int(input("> "))
        if new_total == self.cur_score():
            print("Correct! Your new total is: ")
            print(self.cur_score())
            self.total[0] = self.cur_score()
            if self.total[0] < 0:
                end()
            else:
                print(f'''
                When asked for your total at the end of the next round,
                subtract from {self.total[0]}!

                ''')
                continu()




    #def high_score(self):

class Play(object):

    def __init__(self):
        self.score = Score()

    def throw_dart(self):
        print("You throw three darts!")
        #I still neeed to figure out how to make the random ints only multiples of five.
        # use randrange not randint!
        #for randrange, the last number is not included so do 1 more.

        dart1 = random.randrange(1,61,1)
        print(dart1)

        dart2 = random.randrange(1,61,1)
        print(dart2)

        dart3 = random.randrange(1,61,1)
        print(dart3)

        round_score = dart1 + dart2 + dart3
        guess_sum = int(input("What is the sum of these three integers? "))


        while guess_sum != round_score:
            print("Please try again!")
            guess_sum = int(input("> "))
        if guess_sum == round_score:
            print("Correct!")
            player1.sub_from_total(round_score)





def start():
    strt_input =  input("Welcome to dart math! What would you like to do? \n ")
    acceptable_act = ['help','start','quit','play','high score','high-score','high scores','high-scores']
    while strt_input not in acceptable_act:
        print('slow down partner! we need a valid response to continue! if ye need help, plz type help')
        strt_input = input("> ")
    if strt_input == 'help':
        instructions()
    elif strt_input in ['start','play']:
        p1.throw_dart()
    elif strt_input in ['high score','high scores','high-score','high-scores']:
        print("didnt define yet")
    elif strt_input == 'quit':
        print("BYE BYE!")
        quit(0)
def end():
    print('''


    You've gotten to 0! ... or a bit past that, but that's ok this isn't
    real darts anyways!


    ''')
    quit(0)
player1 = Score()
p1 = Play()
start()


