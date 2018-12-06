import json


class Test(object):

    def __init__(self):
        self.high_scores = [3,2,1]
        self.json_list = json.dumps(self.high_scores)
  


    def put_in_list(self, New_score):
        self.high_scores.append(New_score)
        self.high_scores.sort()


    def make_json(self):
        self.json_list = json.dumps(self.high_scores)
        

    def write_json(self):
        with open('hs_json.txt', 'w') as outfile:
            for score in self.json_list:
                outfile.write(score)

    def load_json(self):
        with open('hs_json.txt', 'r') as self.json_list:
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

hs = Test()
hs.if_file_exists()
hs.make_json()
hs.write_json()
New_score = 4
hs.put_in_list(New_score)
hs.make_json()
hs.write_json()
hs.load_json()
hs.print_list()
