import unittest
from calc import calculadora

class test_calc(unittest.TestCase):
    
    def test_1_mas_1(self):
        calc = calculadora()
        calc.ingresar('1')
        calc.ingresar('+')
        calc.ingresar('1')
        calc.ingresar('=')

        self.assertEqual(calc.display(), 2)

    def test_2_mas_2(self):
        calc = calculadora()
        calc.ingresar('2')
        calc.ingresar('+')
        calc.ingresar('2')
        calc.ingresar('=')

        self.assertEqual(calc.display(), 4)

    def test_5_mas_5(self):
        calc = calculadora()
        calc.ingresar('5')
        calc.ingresar('+')
        calc.ingresar('5')
        calc.ingresar('=')

        self.assertEqual(calc.display(), 10)

    def test_1_mas_2_mas_3(self):
        calc = calculadora()
        calc.ingresar('1')
        calc.ingresar('+')
        calc.ingresar('2')
        calc.ingresar('+')
        calc.ingresar('3')
        calc.ingresar('=')

        self.assertEqual(calc.display(), 6)

    def test_2_mas_2_mas_4(self):
        calc = calculadora()
        calc.ingresar('2')
        calc.ingresar('+')
        calc.ingresar('2')
        calc.ingresar('+')
        calc.ingresar('4')
        calc.ingresar('=')

        self.assertEqual(calc.display(), 8)

    def test_3_mas_5_mas_9(self):
        calc = calculadora()
        calc.ingresar('3')
        calc.ingresar('+')
        calc.ingresar('5')
        calc.ingresar('+')
        calc.ingresar('9')
        calc.ingresar('=')

        self.assertEqual(calc.display(), 17)

    def test_2_mas_2_mas_12(self):
        calc = calculadora()
        calc.ingresar('2')
        calc.ingresar('+')
        calc.ingresar('2')
        calc.ingresar('+')
        calc.ingresar('1')
        calc.ingresar('2')
        calc.ingresar('=')

        self.assertEqual(calc.display(), 16)

    def test_2_mas_2_mas_4_mas_15(self):
        calc = calculadora()
        calc.ingresar('2')
        calc.ingresar('+')
        calc.ingresar('2')
        calc.ingresar('+')
        calc.ingresar('4')
        calc.ingresar('+')
        calc.ingresar('1')
        calc.ingresar('5')
        calc.ingresar('=')

        self.assertEqual(calc.display(), 23)

    def test_2_mas_2_mas_14_mas_15(self):
        calc = calculadora()
        calc.ingresar('2')
        calc.ingresar('+')
        calc.ingresar('2')
        calc.ingresar('+')
        calc.ingresar('1')
        calc.ingresar('4')
        calc.ingresar('+')
        calc.ingresar('1')
        calc.ingresar('5')
        calc.ingresar('=')

        self.assertEqual(calc.display(), 33)

    def test_10_mas_10_mas_10_mas_10(self):
        calc = calculadora()
        calc.ingresar('1')
        calc.ingresar('0')
        calc.ingresar('+')
        calc.ingresar('1')
        calc.ingresar('0')
        calc.ingresar('+')
        calc.ingresar('1')
        calc.ingresar('0')
        calc.ingresar('+')
        calc.ingresar('1')
        calc.ingresar('0')
        calc.ingresar('=')

        self.assertEqual(calc.display(), 40)

if __name__ == '__main__':
    unittest.main()