import warnings
import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting

def polynm_background(raw, n):
    """
    This function takes in a raw spectra as a .txt file and a user desired degree, n, of polynomial
    fitting. It returns the background data and the backgrounded data as np arrays
    """
    
    p_init = models.Polynomial2D(degree = n)
    fit_p = fitting.LevMarLSQFitter()
    
    x, y = raw.shape
    
    yy, xx = np.mgrid[0:x, 0:y]

    with warnings.catch_warnings():
        # Ignore model linearity warning from the fitter
        warnings.simplefilter('ignore')
        p = fit_p(p_init, xx, yy, data)
    
    bkg = p(xx, yy)
    final = data - bkg
    
    return bkg, final
