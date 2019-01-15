from sprite import Sprite
from game_of_life_helper_functions import determine_life
import unittest
import numpy


class SpriteTests(unittest.TestCase):

    def setUp(self):
        self.x=48
        self.y=48
        init_dna_mat=numpy.zeros((self.x, self.y))
        for n in range(48):
            for m in range(48):        
                if (n-self.x/2)**2+(m-self.y/2)**2<(self.x/2.5)**2: #only generate pixels within this circle
                    if determine_life(n,m,self.x,self.y):
                        init_dna_mat[n,m]=True
        self.sprite=Sprite(init_dna_mat)
                        

    def test_mutation(self):
        ## Build a sprite and assert that its mutation method works as expected
        self.assertEqual(len(self.sprite.mutation().dna), 48,'check mutation preserves matrix size')
        self.assertNotEqual(sum(sum(self.sprite.mutation().dna)), sum(sum(self.sprite.mutation().dna)),
        'check that two mutations of the same dna are different, and therefore also different to the original dna')
        #there is a small chance that the two mutations will actually be the same and throw this error. Run again.
 
    def test_draw(self):
        ## Build a sprite and assert that its mutation method works as expected
        self.assertEqual(len(self.sprite.draw()), 48,'check drawing sprite preserves matrix size')
        self.assertNotEqual(sum(sum(self.sprite.dna)), sum(sum(self.sprite.draw())),'check that drawing does something to dna')
 
      
if __name__ == '__main__':
    unittest.main()