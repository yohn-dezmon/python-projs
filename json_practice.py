import json


class Test(object):

    def __init__(self):
        self.high_scores = [3,2,1]
        self.json_list = json.dumps(self.high_scores)
        self.data = []


    def put_in_list(self, New_score):
        self.high_scores.append(New_score)
        self.high_scores.sort()


    def make_json(self):
        self.json_list = json.dumps(self.high_scores)
        

    def write_json(self):
        with open('/Users/HomeFolder/Python1/High_Scores/hs_json.txt', 'w') as outfile:
            for score in self.json_list:
                outfile.write(score)

    def load_json(self):
        with open('/Users/HomeFolder/Python1/High_Scores/hs_json.txt', 'r') as self.json_list:
            self.data = json.load(self.json_list)
            self.data.sort()

    def print_list(self):
        for number in self.data:
            print(number)



hs = Test()
New_score = 4
hs.put_in_list(New_score)
hs.make_json()
hs.write_json()
hs.load_json()
hs.print_list()

# -----------------------
# my_list = [3,2,1]
# json_list = json.dumps(my_list)
#
# # the indent just makes the list easier to read (if you have to read the list)
#
# # with opens the destination file!
# #then the json.dumps writes the data object to the outfile as a string.
# with open('/Users/HomeFolder/Python1/High_Scores/data.txt', 'w') as outfile:
#     for x in json_list:
#         outfile.write(x)
#
#
# with open('/Users/HomeFolder/Python1/High_Scores/data.txt', 'r') as json_list:
#     data = json.load(json_list)
#     data.sort()
#
#
# # for number in data:
# #     print(number)
#




#------------
# sources:
# (1) https://www.youtube.com/watch?v=9N6a-VLBa2I
# (2) https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/

# ok this is coool but how do I open it/write it when I want the file to come from
# a different directory?
# https://stackoverflow.com/questions/21297533/python-open-a-json-file-in-a-different-directory
# I think I need to use open!

# ok now I need to appepnd to the list!

# problem: I can update the attribute list high_scores...
# but when I call high_scores after that OH! it has to do with the instantiation!
