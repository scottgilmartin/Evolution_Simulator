from game_of_life_helper_functions import simulate
import numpy   
import random
from sim_config import SPRITE_HEIGHT, SPRITE_WIDTH, death_limit, birth_limit


class Sprite:
    """
    A sprite is associated with a dna matrix which can be mutated and drawn into a corresponding avatar representation, 
    as displayed when running the evolution simulator. This way every avatar has it's own associated dna, which can be
    slightly modified by mutation and this mutated dna then used to create a new similar avatar. 
    In the evolution simulator, the dna of the selected avatar is mutated in (grid_size**2) different ways 
    and so (grid_size**2) similar avatars are produced in the next generation.
    """
    STEPS_NUM = 5  # number of times we apply the game of life simulation,
    #  changing this affects how the avatar image is drawn from dna

    def __init__(self, dna):
        """
        Initialize dna matrix.
        """
        self.dna = dna

    def mutation(self):
        """
        Mutate sprite dna to produce dna for a new associated sprite.
        """
        new_dna = self.mutate(self.dna)
        return Sprite(new_dna)

    def draw(self):
        """
        Turn the barcode-like dna matrix into cohesive forms by applying the game of life simulation,
        converting the dna of a sprite into its 'avatar' image representation.
        """
        new_mat = simulate(self.dna, self.STEPS_NUM, SPRITE_WIDTH, SPRITE_HEIGHT, death_limit, birth_limit)                                            
        img = numpy.zeros((SPRITE_WIDTH, SPRITE_HEIGHT))

        for x in range(SPRITE_WIDTH):  # Make the avatar symmetrical across Y axis
            for y in range(SPRITE_HEIGHT): 
                if y < SPRITE_HEIGHT / 2:
                    img[x, y] += new_mat[x, y]
                else:
                    img[x, y] += new_mat[x, SPRITE_HEIGHT- y]
        return img

    @staticmethod  
    def mutate(mat):
        """
        Randomly mutate the dna matrix by giving every pixel a 1% chance to change state.
        """
        copy_mat = numpy.zeros((SPRITE_WIDTH, SPRITE_HEIGHT))  # copy the input matrix into copy_mat
        for n in range(SPRITE_WIDTH):
            for m in range(SPRITE_HEIGHT):
                copy_mat[n, m] += mat[n, m]

        for n in range(SPRITE_WIDTH):
            for m in range(SPRITE_HEIGHT):
                
                if (n - SPRITE_WIDTH / 2) ** 2 + (m - SPRITE_HEIGHT / 2) ** 2 < (SPRITE_WIDTH / 2.5) ** 2: 
                    # only want to act on the pixels within the defined circle
                    
                    if random.randint(0, 100) > 99:  # 1% chance to change state
                        
                        if copy_mat[n, m]:   
                            copy_mat[n, m] = False   # True becomes False and vice versa
                        else:
                            copy_mat[n, m] = True
        return copy_mat
