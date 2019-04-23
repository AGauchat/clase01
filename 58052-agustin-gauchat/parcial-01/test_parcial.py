import unittest
from decimal_o_caracter import dec_o_carac

class test_parcial(unittest.TestCase):

    def test_HOLA(self):
        decimal = dec_o_carac('HOLA')
        self.fail(decimal)

    def test_5(self):
        decimal = dec_o_carac(5)
        self.assertEqual(decimal, 5)

    def test_10(self):
        decimal = dec_o_carac(10)
        self.assertEqual(decimal, 'A')

    def test_17(self):
        decimal = dec_o_carac(17)
        self.assertEqual(decimal, '11')

    def test_4095(self):
        decimal = dec_o_carac(4095)
        self.assertEqual(decimal, 'FFF')

    def test_1234(self):
        decimal = dec_o_carac(1234)
        self.assertEqual(decimal, '4D2')

    def test_234(self):
        decimal = dec_o_carac(234)
        self.assertEqual(decimal, 'EA')
    

if __name__ == '__main__':
    unittest.main()