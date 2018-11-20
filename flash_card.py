#flash_card.py

#model: prompt user for a key and definition (Check)
#set up a way so that they can access both the key > definition (check)
# or def > key (I don't think this is possible!)

#in review, it should display 1 key at a time, wait for the user to type enter
#then it should display the definition. for loop!

#set up shuffle or ordered play back.

#set up a while loop for the input, and end it when they want to.

#questions:
#how do I input things into a dictionary...
#using .append() ?? no!
#use dict.update( {'key' : 'value'})
# how can I export the dictionary of this file to another file... (look back)


#have the dictionary stored in a file for future use! wow this is getting complex...






#q 2: how do I get the user to input things into a dictionry?
from sys import exit
import csv
import pickle
cards = {}
#ok exporting to text is kind of shitty b/c its difficult to import
# ideally I would like to export the dictionary to .py
# from what I'm gathering I think the best method might be to 'pickle' the dictionary...
# pickling is used to store objects! (hopefullly dictionaries!)
# pickle a machine learning classifier.
#
def export():
    print("What would you like your flash card set to be called?")
    set_name = input("> ")
    set_name += ".pickle"
    print(f'Your flashcard set file name is: {set_name}')
    new_pickle = open(set_name, "wb") # do i have to write "dict.pickle" for the first argument?
    pickle.dump(cards, new_pickle)
    new_pickle.close()
    print("Great! Your flashcard set has been pickled!")
    return_to_main()
    #print("Would you like the file saved as a csv or text file?")
    #txt_csv = input("> ")
    #if txt_csv == "csv":
        #set_name += ".csv"
        #w = csv.writer(open(set_name, "w"))
        #for key, val in cards.items():
        #    w.writerow([key, val])
    #elif txt_csv == "text":
        #set_name += ".txt"
        #f = open(set_name, "w")
        #f.write( str(cards))
        #f.close()
    #else:
        #return_to_main() #

def update():
    while True:
        print("Please enter your key, followed by your definition:\n")
        term = input("> ")
        defin = input("> ")
        cards.update( {term:defin} )
        if term or defin == ' ':
            return_to_main()


def importF():
    print("ehyo! what set u gwanna get?")
    setget = input("> ")
    dict_pickle = open(setget,"rb") # read bytes
    global cards
    cards = pickle.load(dict_pickle)
    print("Bayum! Your set is ready to be reviewed!")
    return_to_main()

    #return_to_main()
    #print("Cool! is that a text or csv file?")
    #txtorcsv = input("> ")
    #if txtorcsv == "text":
        #setget += ".txt"

        #print("Cool!")
        #return_to_main()

        #import setget  # this doesn't work... i guess it makes sense since setget is a string
        #and when you do 'import something' the something is just a file.
    #elif txtorrcsv == "csv":
        #csv_file = setget + ".csv"
        #txt_file = csv_file
        #with open(txt_file, "w") as output_file:
            #with open(csv_file, "r") as input_file:
                #[ output_file.write(" ".join(row)+ '\n') for row in csv.reader(input_file)]
            #output_file.close()
            #import txt_file
    #else:
        #quit(0)
# ok right now, after
def return_to_main():
    print('''
    What would you like to do?

    a. Continue adding to my current set of cards
    b. Review my set
    c. Edit my set
    d. Export my flash cards to a file''')
    choice = input("> ")

    if choice.lower() == "a":
        update()
    elif choice.lower() == "b":
        review() #still need to define this.
    elif choice.lower() == "c":
         edit()
    elif choice.lower() == "d":
        export()
    else:
        exit(0)
#not done yet!
def edit():
    global cards
    print("\t\t\t WELCOME TO THE EDITOR")
    print("Here are your terms:")
    print(', '.join(cards))
    print('''Would you like to...
    a. Add to your set
    b. Delete a term/definition pair
    c. Redefine a term
    d. Return to main menu''')
    resp = input("> ")
    if resp.lower() == "a":
        while True:
            print("Please enter your key, followed by your definition:\n")
            term = input("> ")
            defin = input("> ")
            cards.update( {term:defin} )
            if term or defin == ' ':
                return_to_main()
    elif resp.lower() == "b":
        print("Please enter the term you would like to be deleted:\n")
        term = input("> ")
        cards.pop(term)
        edit()
    elif resp.lower() == "c":
        print("Which term would you like to redefine?")
        term = input("> ")
        print("What's its new definition?")
        defn = input("> ")
        cards[term] = defn
        edit()
    else:
        return_to_main()
#not done yet!

def review():
    #print(', '.join(cards)) # this just returns the keys...
    print("Here is a list of your terms:")
    for term in cards:
        print(term)
    while True:
        print("Please tell me the term you'd like to review!")
        trm = input("> ")
        try:
            if cards[trm]:
                print(cards.get(trm, 'ut oh!'))
        except:
            print("Sorry that's not in the list!")
            return_to_main()

# Greeting
def start():
    print('''
    Hello Indexer! Welcome to the lo-fi flash card program!
-If at any time you want to stop creating cards, please enter a blank space-

What would you like to do?
(please select a, b, or c)

a. Create a new set of flash cards
b. Import a previous set''')
    choice = input("> ")

    if choice.lower() == "a":
        update()
    elif choice.lower() == "b":
        importF()
    else:
        exit(0)

start()

#problem! I can import the dictionary, and within the function save it to cards.
#however when I use cards in other functions it is not recognizing the newly saved dictionary.
# temporary solution: make separate set of functions for post import...
# actual solution, you need to make cards GLOBAL!
# Sources:
# (adding .csv to input) https://stackoverflow.com/questions/37715217/python-3-how-do-i-join-input-with-a-string
# (saving a dictionary to a file) https://pythonspot.com/save-a-dictionary-to-a-file/
# (pickling?) https://docs.python.org/3.1/library/pickle.html
# try and except: https://stackoverflow.com/questions/40369827/using-continue-in-a-try-and-except-inside-while-loop
#  checking if a key is in a dict: https://stackoverflow.com/questions/7771318/the-most-pythonic-way-of-checking-if-a-value-in-a-dictionary-is-defined-has-zero
# aha!
