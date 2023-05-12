import unittest
from carros import Carro

class TestCarros(unittest.TestCase):
    def setUp(self):
        self.carro1 = Carro('Hamilton', 'Mercedes', 'W10', 350, 1.5)
        self.carro2 = Carro('Bottas', 'Mercedes', 'W10', 350, 1.5)
        self.carro3 = Carro('Vettel', 'Ferrari', 'SF90', 350, 1.5)
        
    def teste(self):
        self.assertEqual(self.carro1.media, 233.33333333333334)
        self.assertEqual(self.carro2.media, 233.33333333333334)
        self.assertEqual(self.carro3.media, 233.33333333333334)



if __name__ == '__main__':
    unittest.main()
    