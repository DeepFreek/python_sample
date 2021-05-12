class Employee:
    def __init__(self,name,second_name,salary):
        self.name=name
        self.second_name=second_name
        self.salary=salary
    def give_raise(self,value=5000):
        self.salary+=value
    def show_salary(self):
        print(self.salary)

Sergey=Employee("sergey","groshev",20000)
Sergey.show_salary()
Sergey.give_raise()
Sergey.show_salary()
Sergey.give_raise(10000)
Sergey.show_salary()

