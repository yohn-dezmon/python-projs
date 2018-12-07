import sys
import random
import time
import json
import os

t0 = time.time()

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
        # uhh I hope this doesn't reset the score...

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
            json.dump(self.high_scores, outfile)
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
        try:
            guess_sum = int(input("What is the sum of these three integers? "))

        except:
            print("that's not a number, mi friend!")
            quit(0)

        while guess_sum != round_score:
            print("Please try again!")
            guess_sum = int(input("> "))
        if guess_sum == round_score:
            print("Correct!")
            player1.sub_from_total(round_score)





def start():
    strt_input =  input("Welcome to dart math! What would you like to do? \n ")
    acceptable_act = ['help','clear','clear high score','skip','start','quit','play','high score','high-score','high scores','high-scores']
    while strt_input not in acceptable_act:
        print('slow down partner! we need a valid response to continue! if ye need help, plz type help')
        strt_input = input("> ")
    if strt_input == 'help':
        instructions()
    elif strt_input in ['start','play']:
        # player1 = Score()
        # player1.initial_score()
        p1.throw_dart()
    elif strt_input in ['high score','high scores','high-score','high-scores']:
        hs.if_file_exists()
        hs.make_json()
        # this does need to be here, the if file exists just makes sure that the file is loaded before
        # a brand new file is written!
        hs.write_json()
        hs.print_hs()
    elif strt_input == 'skip':
        skip_to_end()
    elif strt_input in ['clear','clear high score']:
        hs.reset_hs()
    elif strt_input == 'quit':
        print("BYE BYE!")
        quit(0)
def skip_to_end():
    end()

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
# player1 = Score()
# player1.initial_score()



# notes:

# yay https://stackabuse.com/reading-and-writing-lists-to-a-file-in-python/


# How to interpret inputs as numbers?
# x = int(input("Enter a number: "))
# source: https://stackoverflow.com/questions/20449427/how-can-i-read-inputs-as-numbers

#How do I instantiate one class within another class (without inheritance)?
# https://stackoverflow.com/questions/12008991/python-create-instance-of-class-in-another-class-with-generic-example
# OMG! Yay! you have to instantitae the class within the constructor of the class you what-is-the-formal-difference-between-print-and-return
# example def __init__(self): self.score = Score()
# Wow I might be able to complete the game now...

# OK since I'm having this conflict of saving a value in a class, and also being able to get out of that class
# I'm thinking a possible solution would be to have the score in a global list...
# then I could call the global list within the necessary classes...
# this would change up the structure of the code a lot though.


# functionality I want to add:
# 1. Timer for the entire game
# 2. High score which incorporates the timer... the high scores should probably be
# stored in a separate file?  maybe? in a dictionary?

# Timer: one way... (if I can figure out exactly where my code starts and stops)
# is to do import time
# t0 = time.time()
# ...
# t1 = time.time()
# total = t1-t0
#
# High score: Can you store previous high scores in the script?
# I don't think so, I was already thinking that I should probably just pickle
# the high scores (like I did with my flash cards)
# and when I googled it I found a response saying you should save the scores in a
# text file using shelve
# If I want to save in in an ordered list... how to do that?
# Can I somehow order the list before exporting it?

# shelve module: https://stackoverflow.com/questions/16726354/saving-the-highscore-for-a-python-game
# https://docs.python.org/2/library/shelve.html

# question: Do the ends of my functions always have to lead back into other functions?
# by not having them go into a particular function, does it then end the program?

# Question: Why does my dump (import) keep overwriting my file pickle file/list?
# answer: https://stackoverflow.com/questions/20624682/pickle-dump-replaces-current-file-data

# the answer ^ above says that a better way to store dictionaries (and probably lists?)
# is using the shelve module rather than the pickle thing...
# apparently using pickle will make the program slower :(

# question: How do I make a function that only runs the first time the program opens?
# answer: since your function creates a file, check for the existence of the file before doing anything.
# https://stackoverflow.com/questions/20745546/python-need-a-function-that-runs-only-at-first-time-startup

# back to https://stackoverflow.com/questions/20624682/pickle-dump-replaces-current-file-data
# pickle doesn't support APPENDING. This guy suggests using JSON module.

# ok I think the way I have it set up now, it won't add to the list unless I do high score first
# what am I doing by saying high score that I'm not other wise that is essential to it adding to the
# list?
# also yeah I just confirmed this, by doing skip directly, I overwrite the file! so I'm not checking!
