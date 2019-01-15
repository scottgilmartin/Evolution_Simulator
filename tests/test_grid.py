from grid import Grid
from sprite import Sprite
from game_of_life_helper_functions import determine_life
import unittest
import numpy


class GridTests(unittest.TestCase):

    def setUp(self):
        self.x=48
        self.y=48
        self.grid_num=4
        self.init_dna_mat=numpy.zeros((self.x, self.y))
        for n in range(48):
            for m in range(48):        
                if (n-self.x/2)**2+(m-self.y/2)**2<(self.x/2.5)**2: #only generate pixels within this circle
                    if determine_life(n,m,self.x,self.y):
                        self.init_dna_mat[n,m]=True
        self.grid=Grid(self.grid_num)
        self.grid2=Grid(self.grid_num)
        self.grid3=Grid(self.grid_num)
        self.sprites=[Sprite(self.init_dna_mat) for i in range(self.grid_num**2)]
        self.mutated_sprites=[sprite.mutation() for sprite in self.sprites]
        self.grid2.add_sprite(self.sprites[0])
        
        for sprite in self.mutated_sprites:
            self.grid3.add_sprite(sprite)
            
        self.mutation_grid=self.grid3.construct_grid()
        self.img_grid = mutation_grid[0]
        self.dna_grid = mutation_grid[1]
#        
#        print(len(img_grid[0]))
                        

    def test_add_sprite(self):
        ## Build a sprite and assert that its mutation method works as expected
        self.assertLess(len(self.grid.img_grid), len(self.grid2.img_grid),'check adding sprite increases length of grid.img_grid')
        self.assertEqual(len(self.grid3.img_grid), self.grid_num**2,'check adding sprites gives correct length')
   
    def test_construct_grid(self):
        ## Build a sprite and assert that its mutation method works as expected
        self.assertEqual(len(self.mutation_grid),2,'check mutation_grid contains both sub-grids')
        self.assertEqual(len(self.img_grid),self.grid_num*self.x,'check the grid is the correct size')
        self.assertGreater(sum(sum(self.img_grid)),0,'check the grid contains pixels')
      
if __name__ == '__main__':
    unittest.main()