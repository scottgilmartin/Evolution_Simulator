from grid import Grid
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy
from sprite import Sprite
from game_of_life_helper_functions import determine_life
from sim_config import SPRITE_WIDTH, SPRITE_HEIGHT

CCMAP = mpl.colors.ListedColormap(['#4b0057', '#40418A', '#7551B4', '#604CDD', '#FF62F2', '#FF3B5A'])
FIG,AX = plt.subplots()
SELECTED_SPRITES=[]

class EvolutionSim:
    """
    An evolution simulation, which takes the input dna and generates a grid of mutations and the corresponding avatar
    representations. User selects an avatar with the mouse, and the dna of the selected avatar is mutated to create
    the next generation of avatars.
    
    """

    def __init__(self, dna_mat, evolution_num, grid_size):
        """
        Initialize the first generation of sprites and grid to add them to.
        """
        self.sprites = [Sprite(dna_mat) for i in range(grid_size ** 2)]
        self.grid = Grid(grid_size)
        self._img_grid_mat = None 
        self._dna_grid_mat = None #None until we draw the sprites as matrices and add these to the image/dna list in Grid

    @property
    def img_grid_mat(self): 
        """
        A grid sized matrix where every individual sprite avatar is a sub-matrix, 
        this is what the user sees when running the simulation and selecting avatars.
        """
        if self._img_grid_mat is None:
            self.construct_grid()
        return self._img_grid_mat

    @property
    def dna_grid_mat(self): 
        """
        A grid sized matrix where every individual sprite dna matrix is a sub-matrix
        """
        if self._dna_grid_mat is None:
            self.construct_grid()
        return self._dna_grid_mat

    def evolve_grid(self):
        """
        Creates a list of the mutated sprites based on the previous avatar selection
        and adds them to the new grid.
        """
        mutated_sprites = [sprite.mutation() for sprite in self.sprites]
        for sprite in mutated_sprites:
            self.grid.add_sprite(sprite)

    def construct_grid(self):
        """
        Use the construct_grid() method from the Grid class to create the grid matrices.
        """
        self._img_grid_mat, self._dna_grid_mat = self.grid.construct_grid()

def onclick(event): #maybe work this into ES class
    """
    Detects click coordinates on active figure, converts the coordinates into (row,col) of the grid matrix
    and stores them as globals to be read by the simulation.
    """
    click_coord = [event.xdata, event.ydata]
    global row, col
    col = int(click_coord[0] / SPRITE_WIDTH)
    row = int(click_coord[1] / SPRITE_HEIGHT)
    plt.close(FIG)

def gen_initial_dna():
    """
    Generate initial dna to be fed into the simulation and create the first generation of mutations.
    """
    init_dna_mat=numpy.zeros((SPRITE_WIDTH,SPRITE_HEIGHT))
    for n in range(SPRITE_WIDTH):
        for m in range(SPRITE_HEIGHT):        
            if (n-SPRITE_WIDTH/2)**2+(m-SPRITE_HEIGHT/2)**2<(SPRITE_WIDTH/2.5)**2: #only generate pixels within this circle
                if determine_life(n,m,SPRITE_WIDTH,SPRITE_HEIGHT):
                    init_dna_mat[n,m]=True
    return init_dna_mat

def run_simulation(dna_mat, evolution_num, grid_size):
    """
    Run the evolution simulation for the specified number of steps. At each step user clicks an avatar, the dna associated
    with this avatar is extracted and fed back into the simulation loop to create a new generation of mutations similar to the
    chosen avatar. Repeat until number of steps = evolution_num.
    """

    for _ in range(evolution_num):
        sim = EvolutionSim(dna_mat, evolution_num, grid_size)
        sim.evolve_grid() #generate the mutations from the input dna_mat
        img_grid_mat = sim.img_grid_mat #built with construct_grid() method, the grid of avatars that is displayed while sim runs
        
        FIG,AX = plt.subplots() ## need to explain more what's going on after this point                                 
        AX.matshow(img_grid_mat, cmap=CCMAP)
        FIG.canvas.mpl_connect('button_press_event', onclick) #detect events on a figure, used to get user mouse click coords
        plt.show()

        plt.pause(1) #allow the plot to show before waiting for click event

        if plt.waitforbuttonpress():
            break #exit simulation by pressing any key
        else:
            selected_sprite = sim.grid.img_grid[(grid_size * col) + row] #clicking an avatar feeds its position back to here using (row,col)
            selected_dna = sim.grid.dna_grid[(grid_size * col) + row]
            SELECTED_SPRITES.append(selected_sprite)
            dna_mat = selected_dna #set the dna_mat to the dna of the selected avatar, this feeds back into the loop allowing the next generation to be mutations of the selected avatar
            plt.close()
            
    return SELECTED_SPRITES


def view_evolution(sprites):
    """
    Shows the evolution throughout the simulation,
    shows every selected avatar in reverse chronological order.
    """
    G0 = sprites[0]

    for i in range(1, len(sprites)):
        evolution_result = numpy.concatenate((sprites[i], G0), axis=1)
        G0 = evolution_result

    plt.matshow(evolution_result, cmap=CCMAP)

#initialize and run the simulation, and view the result.
                    
dna_mat=gen_initial_dna() 

grid_size=4 
  
evolution_num=20 

run_simulation(dna_mat, evolution_num, grid_size)

view_evolution(SELECTED_SPRITES)

