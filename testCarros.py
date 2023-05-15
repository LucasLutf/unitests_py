import unittest
from carros import Carro

class TestCarros(unittest.TestCase):
    def setUp(self):
        self.carro1 = Carro('Hamilton', 'Mercedes', 'W10', 350, 1.5)
        self.carro2 = Carro('Bottas', 'Mercedes', 'W10', 350, 1.5)
        self.carro3 = Carro('Vettel', 'Ferrari', 'SF90', 350, 1.5)
        
    def mediaVolta(self):
        self.assertEqual(self.carro1.media, 233.33333333333334)
        self.assertEqual(self.carro2.media, 233.33333333333334)
        self.assertEqual(self.carro3.media, 233.33333333333334)
        
    def ultrapassagens(self):
        self.assertEqual(self.carro1.piloto, self.carro2.equipe)
        self.assertEqual(self.carro2.piloto, self.carro1.equipe)
        self.assertEqual(self.carro3.piloto, self.carro1.equipe)
        
    



if __name__ == '__main__':
    unittest.main()
    