import unittest
from employee import Employee

class Test_Empl(unittest.TestCase):
    def setUp(self):
        self.Sergey=Employee("Sergey","Groshev",20000)
    def test_none(self):
        self.Sergey.give_raise()
        new_salary=self.Sergey.salary
        self.assertEqual(new_salary,25000)
    def test_num(self):
        self.Sergey.give_raise(10000)
        new_salary=self.Sergey.salary
        self.assertEqual(new_salary,30000)

unittest.main()