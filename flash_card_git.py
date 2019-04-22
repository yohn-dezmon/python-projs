#flash_card.py

from sys import exit
import csv
import pickle
# create a dictionary to store the terms and definitions
cards = {}

# export the modified or new Flashcard set to a .pickle file
# exports the pickle file to my example directory, where I have a specific folder for flashcard sets.
def export():
    print("What would you like your flashcard set to be called?")
    set_name = input("> ")
    set_name += ".pickle"
    print(f'Your flashcard set file name is: {set_name}')
    new_pickle = open(f'/Users/HomeFolder/Python1/Flashcardz/{set_name}', "wb") # write the file to bytes
    pickle.dump(cards, new_pickle)
    new_pickle.close()
    print("Great! Your flashcard set has been pickled!")
    return_to_main()
# Allows user to create a new flashcard set from scratch or add to an existing set
def update():
    print("Please enter your key, followed by your definition:\n")
    print(''''After you've finished adding, please enter \'stop\'
    as the term and definition to continue''')
    term = ' ' 
    defin = ' ' 
    while term != 'stop':
        term = input("Term: ")
        defin = input("Def: ")
        cards.update({term:defin})
    del cards['stop']
    return_to_main()
#         term = input("Key: ")
#         defin = input("Def: ")
#         cards.update( {term:defin} )
#         if term or defin == ' ':
#             return_to_main()

# imports the pickle file as a dictionary that is ready to be reviewed and edited
# imports the pickle file from my example directory where I have a specific folder for flashcard sets
# I've included seget += ".pickle" so the user does not need to write .pickle every time they want to retrieve a flashcard set.
def importF():
    print("ehyo! what set u gwanna get? (no file extension)")
    setget = input("> ")
    setget += ".pickle"
    dict_pickle = open(f'/Users/HomeFolder/Python1/Flashcardz/{setget}',"rb") # read bytes
    global cards
    cards = pickle.load(dict_pickle)
    print("Bayum! Your set is ready to be reviewed!")
    return_to_main()

# The main menu of the flashcard program, gives user the option to add to, review, edit, or export their existing flashcard set.
def return_to_main():
    print('''
    What would you like to do?
    a. Continue adding to my current set of cards
    b. Review my set
    c. Edit my set
    d. Export my flashcards to a file
    e. Leave the program''')
    choice = input("> ")

    if choice.lower() == "a":
        update()
    elif choice.lower() == "b":
        review() 
    elif choice.lower() == "c":
         edit()
    elif choice.lower() == "d":
        export()
    else:
        exit(0)
# the editor, displays terms of the flashcard set. Gives user the option to add to, delete, redefine, or return to main menu.
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
        update()
    elif resp.lower() == "b":
        print("Please enter the term you would like to be deleted:\n")
        term = input("> ")
        try:
            if term in cards:
                cards.pop(term)
                edit()
        except:
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
# Review the current flashcard set. It will iterate until the user enters an input that is not a term.
def review():
    #print(', '.join(cards)) # this just returns the keys...
    print("Here is a list of your terms:")
    key_list = list(cards.keys())
    for x in key_list:
        y = key_list.index(x)
        print(f"{y}" + '.' + " " + x)

    while True:
        print("Please tell me the number of the term you'd like to review!")
        try:
            nmb= int(input("> "))
            trm = key_list[nmb]
        except:
            print("that's not a number!")
            return_to_main()
        try:
            if cards[trm]:
                print(cards[trm])
        except:
            print("Sorry that's not in the list!")
            return_to_main()

# Greeting
def start():
    print('''
    Hello Indexer! Welcome to the lo-fi flashcard program!
-If at any time you want to stop creating cards, please enter a blank space-

What would you like to do?
(please select a or b)
a. Create a new set of flashcards
b. Import a previous set''')
    choice = input("> ")

    if choice.lower() == "a":
        update()
    elif choice.lower() == "b":
        importF()
    else:
        exit(0)

start()


# Sources:
# (adding .csv to input) https://stackoverflow.com/questions/37715217/python-3-how-do-i-join-input-with-a-string
# (saving a dictionary to a file) https://pythonspot.com/save-a-dictionary-to-a-file/
# (pickling?) https://docs.python.org/3.1/library/pickle.html
# try and except: https://stackoverflow.com/questions/40369827/using-continue-in-a-try-and-except-inside-while-loop
# checking if a key is in a dict: https://stackoverflow.com/questions/7771318/the-most-pythonic-way-of-checking-if-a-value-in-a-dictionary-is-defined-has-zero
# pickling to a particular directory: https://stackoverflow.com/questions/17750422/how-to-pickle-an-object-to-a-certain-directory
