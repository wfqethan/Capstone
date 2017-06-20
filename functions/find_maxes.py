import numpy as np

def find_maxes(array):
    """
    This function takes in a 3D array of intensity values for pixels in an AFM micrograph and returns the maximum
    value for each of the scan types as a vector
    
    input: numpy ndarray of 3 dimensions containing AFM scan data
    output: numpy array of 1 dimension containing the maximum value of each scan type
    """
    x, y, z = array.shape
    maxVec = np.empty(z)
    
    #initialize the maxVec to contain the 1st pixel's values
    for h in range(z):
        maxVec[h] = array[0, 0, h]
    
    #look for the maximum value for each scan type
    for i in range(z):
        for j in range(x):
            for k in range(y):
                if maxVec[i, j, k] < array[i, j, k]:
                    maxVec[i, j, k] = array[i, k, j]
                elif maxVec[i, j, k] > array[i, j, k]:
                    pass
                else:
                    pass
    
    return maxVec
