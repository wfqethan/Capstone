import math

def euc_dist(maxVec, pixel1, pixel2):
    """
    This function takes in a vector of maximum values for the sample's different data types and two pixels as
    vectors of their features and calculates the Euclidean distance. It then normalizes these differences for 
    each scan type so there isn't uneven weighting for a given feature type. Finally, it returns the adjusted 
    Euclidean distance.
    
    This function assumes that only numeric data is in the pixel features.
    
    inputs: a 1D numpy array containing the maximum values of a given sample's scan types
            a 1D numpy array containing the feature values of the pixel being examined
            a 1D numpy array containing the feature values of the neighboring pixel
    
    outputs: a numeric value describing the normalized euclidean distance between the pixel and its neighbor
    """
    dist_sqrd = 0
    
    #calculate the normalized square of the euclidean distance. 
    for i in range(len(pixel1 + 1)):
        diff = 0
        diff = (pixel1[i] - pixel2[i])/maxVec[i]
        
        dist_sqrd += diff
    
    dist = math.sqrt(sum(dist_sqrd))
    
    return dist
