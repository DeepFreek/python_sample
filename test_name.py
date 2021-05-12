from tests import get_formatted_Name
import unittest

class test(unittest.TestCase):
    def setUp(self):
        self.names_2="Sergey Groshev"
        self.names_3="Sergey Groshev Anatolievich"

    def test_2_name(self):
        formatted_name=get_formatted_Name("Sergey","Groshev")
        self.assertEqual(formatted_name,self.names_2)

    def test_3_name(self):
        formatted_name=get_formatted_Name("Sergey","Groshev","Anatolievich")
        self.assertEqual(formatted_name,self.names_3)

unittest.main()