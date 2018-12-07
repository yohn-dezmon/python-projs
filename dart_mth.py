import sys
import random
import time
import json
import os

t0 = time.time()

def instructions():
    print('''
    Welcome to Dart Math!
This program is designed to let you practice your mental
addition/subtraction so you don't make a fool
out of yourself come game time!

Here are the accepted commands from the main prompt:

help - provides instructions for the game.

start - initiates the game play.

high score - allows you to view your previously acheived high scores. Scores are
how long it took you to complete the program (i.e. get your score to 0).

clear - allows you to clear the high score list.

quit - allows you to quit the program without altering the high score list.


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

class High_score(object):

    def __init__(self):
        self.high_scores = []
        self.json_list = json.dumps(self.high_scores)
        self.blank_list = []

    def put_in_list(self, New_score):
        self.high_scores.append(New_score)
        self.high_scores.sort()

    def make_json(self):
        self.json_list = json.dumps(self.high_scores)

    def write_json(self):
        with open('/Users/HomeFolder/Python1/High_Scores/hs1_json.txt', 'w') as outfile:
            for score in self.json_list:
                outfile.write(score)

    def load_json(self):
        with open('/Users/HomeFolder/Python1/High_Scores/hs1_json.txt', 'r') as self.json_list:
            self.high_scores = json.load(self.json_list)
            self.high_scores.sort()

    def print_list(self):
        for number in self.high_scores:
            print(number)

    def if_file_exists(self):
        try:
            self.load_json()
        except:
            self.write_json()

    def reset_hs(self):
        with open('/Users/HomeFolder/Python1/High_Scores/hs1_json.txt', 'w') as outfile:
            json.dump(self.blank_list, outfile)
        start()


    def print_hs(self):
        print("These are the TOP 10 high scores!")
        # this saves the top 10 high scores into a list 
        top_10 = self.high_scores[:10]
       # this prints only the top 10 high scores
        for x in range(len(top_10)):
           print(x+1,top_10[x])
        start()


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
        while True:
            try:
                guess_sum = int(input("What is the sum of these three integers? "))
                break
            except:
                print("that's not a number, mi friend!")

        while guess_sum != round_score:
            print("Please try again!")
            guess_sum = int(input("> "))
        if guess_sum == round_score:
            print("Correct!")
            player1.sub_from_total(round_score)


def start():
    strt_input =  input("Welcome to Dart Math! What would you like to do? \n(if you're unsure, please type 'help'!)\n ")
    # if you want to use the skip option, please enter 'skip' into the acceptable_act list! 
    acceptable_act = ['help','clear','clear high score','start','quit','play','high score','high-score','high scores','high-scores']
    while strt_input not in acceptable_act:
        print('slow down partner! we need a valid response to continue! if ye need help, plz type help')
        strt_input = input("> ")
    if strt_input == 'help':
        instructions()
    elif strt_input in ['start','play']:
        p1.throw_dart()
    elif strt_input in ['high score','high scores','high-score','high-scores']:
        hs.if_file_exists()
        hs.make_json()
        # this does need to be here, the if file exists just makes sure that the file is loaded before
        # a brand new file is written!
        hs.write_json()
        hs.print_hs()
    #elif strt_input == 'skip':
        #end()
    elif strt_input in ['clear','clear high score']:
        hs.reset_hs()
    elif strt_input == 'quit':
        print("BYE BYE!")
        quit(0)

def end():
    print('''


    You've gotten to 0! ... or a bit past that, but that's ok this isn't
    real darts anyways!


    ''')
    hs.if_file_exists()
    hs.make_json()
    hs.write_json()
    t1 = time.time()
    total_time = t1-t0
    hs.put_in_list(total_time)
    # hmm i might need to end the game differently if I want it to close properly?//
    hs.make_json()
    hs.write_json()
    hs.load_json()

    # hs.print_list()
    quit(0)


player1 = Score()
p1 = Play()
hs = High_score()
start()

# --------------------
# notes to developers:
# skip - allows you to go to the end of the game. Used to test high score class.

