import random
class KUB():
    def __init__(self,max):
        self.num=0
        self.max=max
    def roll(self):
        self.num=random.randint(1,self.max)

