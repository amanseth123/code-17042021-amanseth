import unittest
from pythonMain import *
class TestBMI(unittest.TestCase):
    #def testbmi(self):
        #self.assertAlmostEqual(BMI(0,0),0)
    def test_value(self):
        self.assertRaises(ValueError,BMI,-1,-1)
        self.assertRaises(ZeroDivisionError,BMI,0,0)
    def test_type(self):
        self.assertRaises(TypeError,BMI,2+3j,2+3j)
        self.assertRaises(TypeError,BMI,True,True)
        self.assertRaises(TypeError,BMI,"Hello","Hello")
    


