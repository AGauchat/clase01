import unittest
from Juego import juego_adivinar

class TestsComparador(unittest.TestCase) :

    def test_7634_vs_6951(self):
        ju = juego_adivinar()
        regular, bien = ju.comparador(7634, 6951)
        self.assertEqual(regular, 1)
        self.assertEqual(bien, 0)

    def test_4673_vs_5713(self):
        ju = juego_adivinar()
        regular, bien = ju.comparador(4673, 5713)
        self.assertEqual(regular, 1)
        self.assertEqual(bien, 1)

    def test_4836_vs_1234(self):
        ju = juego_adivinar()
        regular, bien = ju.comparador(4836, 1234)
        self.assertEqual(regular, 1)
        self.assertEqual(bien, 1)

    def test_1234_vs_1234(self):
        ju = juego_adivinar()
        regular, bien = ju.comparador(1234, 1234)
        self.assertEqual(regular, 0)
        self.assertEqual(bien, 4)

    def test_1957_vs_1970(self):
        ju = juego_adivinar()
        regular, bien = ju.comparador(1957, 1970)
        self.assertEqual(regular, 1)
        self.assertEqual(bien, 2)

    def test_6485_vs_5836(self):
        ju = juego_adivinar()
        regular, bien = ju.comparador(6485, 5836)
        self.assertEqual(regular, 3)
        self.assertEqual(bien, 0)

    

if __name__ == '__main__':
    unittest.main()