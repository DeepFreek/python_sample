from random import choice
class RW():
    def __init__(self,points_number):
        self.points_number=points_number
        self.x_values=[0]
        self.y_values=[0]
    def new_point(self,prev_value):
        direction=choice([-1,1])
        distance=choice([10,20,30,40,50])
        move=direction*distance
        new_value=prev_value+move
        return new_value
    def fill_walk(self):
        while(len(self.x_values)<self.points_number):
            self.x_values.append(self.new_point(self.x_values[-1]))
            self.y_values.append(self.new_point(self.y_values[-1]))

    def ret_val(self):
        print(self.x_values)
        print(self.y_values)



