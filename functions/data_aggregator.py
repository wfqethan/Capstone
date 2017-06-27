def data_aggregator(sampleName):
    """
    This function takes in a sample name and parses through the files containing cleaned .txt files pertaining to the
    sample. It then combines the separate 2D scan arrays as a single 3D array, which it returns. Finally, it writes
    this 3D array to a new file as a 2D array of the pixels (x) and their z info (y).
    
    inputs: a string variable of the sample's identification
    
    outputs: the 3D array containing the aggregated data
        *writes a new file in the directory corresponding to aggregated data
    """
    
    adh = np.genfromtxt('../Data/AFM/CleanedTXT/Adhesion/%s.txt'% (sampleName))
    defor = np.genfromtxt('../Data/AFM/CleanedTXT/Deformation/%s.txt'% (sampleName))
    dis = np.genfromtxt('../Data/AFM/CleanedTXT/Dissipation/%s.txt'% (sampleName))
    modul = np.genfromtxt('../Data/AFM/CleanedTXT/LogDMTModulus/%s.txt'% (sampleName))
    stif = np.genfromtxt('../Data/AFM/CleanedTXT/Stiffness/%s.txt'% (sampleName))

    x, y = adh.shape
    z = 5
    
    aggr = np.ndarray([x, y, z])
    
    for i in range(x):
        for j in range(y):
            aggr[i, j, 0] = adh[i, j]

    for i in range(x):
        for j in range(y):
            aggr[i, j, 1] = defor[i, j]

    for i in range(x):
        for j in range(y):
            aggr[i, j, 2] = dis[i, j]

    for i in range(x):
        for j in range(y):
            aggr[i, j, 3] = modul[i, j]

    for i in range(x):
        for j in range(y):
            aggr[i, j, 4] = stif[i, j]
            
    two_dim_aggr = aggr.reshape((x*y), z)
            
    np.savetxt('../Data/AFM/AggregatedData/%s.txt'%(sampleName), two_dim_aggr) 
    
    return aggr
