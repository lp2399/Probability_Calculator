import random
import copy
from collections import Counter
class Hat: 
    def __init__(self,**kwargs): # from dict to a list of key*val times. if we pass Hat(blue=3,red=2) we get a list [blue,blue,blue,red,red]
        contents = []
        for i,j in kwargs.items():
            for x in range(j):
                contents += i.split()
        self.contents = contents

    def draw(self,quantity):
        drawn_list = []
        if(quantity>len(self.contents)): # if the len is greater than the len(contents) we just return the list
            return self.contents
        for i in range(quantity): # we do this for the amount needed
            drawn_list.append(self.contents.pop(self.contents.index(random.choice(self.contents)))) 
        return drawn_list
def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    drawn_list = []
    M =0 # helps us keep track of the times expected_balls appaears in drawn list
    for i in range(num_experiments):
        hat_obj = copy.deepcopy(hat) # had to look this up since hat_obj = hat wasnt working had me confused
        drawn = hat_obj.draw(num_balls_drawn)# drawing the balls using draw method num_ball_time
        drawn_list.append(drawn) #append what is returned from draw
    for sub in drawn_list:
        if(len( Counter(expected_balls)-Counter(i for i in sub))==0): 
            M+=1           
    return M/num_experiments # finally we return our prob
hat = Hat(black=6, red=4, green=3)      
probability = experiment(hat, {"red":2,"green":1},5,2000)
print(probability)
