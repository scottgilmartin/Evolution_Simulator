import numpy
import random

def determine_life(x,y,width,height): 
    """
    This function iterates through every point (x,y) in a matrix of size (width,height) and changes it's value from False to True
    with some probability. The probability is 0.55 inside the defined circle and 0.5 elsewhere.
    """
    alive=False
    num=random.randint(0, 100)
        
    if (x-width/2)**2+(y-height/2)**2<(width/5)**2: #greater chance to generate living pixel in this circle
            
        if num<55:      
            alive=True
    else:
        if num<50:
            alive=True  
                
    return alive

                  
def simulate(mat, steps_num, width, height, death_limit, birth_limit):
    """
    Applies the game of life simulation the specified number of times.
    """
    for _ in range(steps_num):
        gol_mat = game_of_life_simulation(mat, width, height, death_limit, birth_limit)
        mat = gol_mat
    return gol_mat


def game_of_life_simulation(mat, width, height, death_limit, birth_limit):
    """
    Alters the input matrix according to the rules of Conway's game of life. Here it is used to turn the barcode-like
    dna matrix into cohesive forms, i.e. converting the dna of a sprite into its 'avatar' image representation.
    """
    new_mat = numpy.zeros((width, height))

    for x in range(width):
        for y in range(height):
            nbs = _count_alive_neighbours(mat, x, y, width, height)
            if mat[x, y]:
                if nbs < death_limit:  #if a live pixel is surrounded by death_limit=4 pixels in the game of life, then it dies
                    new_mat[x, y] = False
                else:
                    new_mat[x, y] = True
            else:
                if nbs > birth_limit: #if a dead pixel is surrounded by birth_limit=4 pixels in the game of life, then it comes to life
                    new_mat[x, y] = True
                else:
                    new_mat[x, y] = False
    return new_mat


def _count_alive_neighbours(mat, x, y, width, height): 
    """                                                  
    Counts the no of live cells around a point (x,y).
    """
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):

            neighbour_x = x + i
            neighbour_y = y + j

            if i == 0 and j == 0:
                count = count
            elif neighbour_x < 0 or neighbour_y < 0 or neighbour_x > width - 1 or neighbour_y > height - 1:
                count = count
            elif mat[neighbour_x, neighbour_y]:
                count = count + 1
    return count
