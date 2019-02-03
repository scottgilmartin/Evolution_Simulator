import numpy
from sim_config import SPRITE_HEIGHT, SPRITE_WIDTH


class Grid:
    """
    The grid is the grid_size x grid_size matrix with two layers; one of sprite dna and one of the corresponding sprite 'avatars'
    that are displayed when the evolution simulator is running.
    """
    def __init__(self, grid_size):
        """
        Initialize grid size, create img_grid and dna_grid lists.
        """
        self.grid_size = grid_size  
        self.img_grid = []  # a list of the individual avatar matrices
        # which are stitched together to create the avatar layer of grid (img_grid_mat)
        self.dna_grid = []  # a list of the individual dna matrices from which
        # the corresponding avatars above are drawn, used to create the dna layer of the grid (dna_grid_mat)

    def add_sprite(self, sprite): 
        """
        Add sprite objects to the grid.
        """
        self.img_grid.append(sprite.draw())  # adding the drawn avatars
        self.dna_grid.append(sprite.dna)  # adding the corresponding dna from which the above avatars are drawn
        return self.img_grid, self.dna_grid

    def construct_grid(self):
        """
        Create the grid from the added sprites; 
        img_grid_mat is a matrix of every avatar in img_grid stitched together.
        dna_grid_mat is a matrix of every avatar in dna_grid stitched together.
        """
        img_grid_mat = numpy.zeros((self.grid_size * SPRITE_WIDTH, self.grid_size * SPRITE_HEIGHT)) 
        dna_grid_mat = numpy.zeros((self.grid_size * SPRITE_WIDTH, self.grid_size * SPRITE_HEIGHT))

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                for x in range(i * SPRITE_WIDTH, (i + 1) * SPRITE_WIDTH):
                    for y in range(j * SPRITE_HEIGHT, (j + 1) * SPRITE_HEIGHT):
                        img_grid_mat[x, y] += self.img_grid[self.grid_size * j + i][x - i * SPRITE_WIDTH, y - j * SPRITE_HEIGHT] 
                        dna_grid_mat[x, y] += self.dna_grid[self.grid_size * j + i][x - i * SPRITE_WIDTH, y - j * SPRITE_HEIGHT]
                        # stitch the individual sprites together
                        # by drawing them in the specified position in the grid matrices
        return img_grid_mat, dna_grid_mat
        

