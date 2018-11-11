# Prompt user for their name
name = input("What is your name? ")

# Greeting with users name
print(f'''Hey {name}! Welcome to Mad Libs the program!

Please provide us with...''')

# Prompt user for a noun, adjective, and verb(ING)
noun = input("A noun: ")
adj = input("An adjective: ")
verb = input("A verb ending in ing: ")

# Print space between the prompts and the story
print('''

''')
# Print the story using the inputs from the user. The title is in capitals and is cenetered.
print(f'''Voila! Here is your story:
\t\tTHE LOST BURRITO
One day a burrito lost its {noun}. The burrito was so sad!
He looked everywhere for this very {adj} {noun}.
It was so dear to him, that he lost himself {verb} for the {noun}!
Poor burrito!''')
