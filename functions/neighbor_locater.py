import numpy as np

def neighbor_locater(x, y):
    """
    This function takes in the xy location of a pixel in a 3D array of information and locates its neighbors.
    
    input: x - The row of pixels that contains the pixel in question
           y - The column of pixels that contains the pixel in question
    
    output: neighbors - a 2D array containing the xy location of the 8 nearest neighbors
    """
    
    neighbors = np.empty([8, 2])
    
    neighbors[0, 0] = x - 1
    neighbors[0, 1] = y - 1
    
    neighbors[1, 0] = x - 1
    neighbors[1, 1] = y
    
    neighbors[2, 0] = x - 1
    neighbors[2, 1] = y + 1
    
    neighbors[3, 0] = x
    neighbors[3, 1] = y - 1
    
    neighbors[4, 0] = x
    neighbors[4, 1] = y + 1
    
    neighbors[5, 0] = x + 1
    neighbors[5, 1] = y - 1
    
    neighbors[6, 0] = x + 1
    neighbors[6, 1] = y
    
    neighbors[7, 0] = x + 1
    neighbors[7, 1] = y + 1
    
    return neighbors
