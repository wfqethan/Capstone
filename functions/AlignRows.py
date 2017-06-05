import numpy as np
from astropy.modeling import models, fitting
import matplotlib.pyplot as plt

import warnings

data = np.genfromtxt('../Data/AFM/TXT/10-10_Z')

print (data.dtype)

p_init = models.Polynomial2D(degree = 3)
fit_p = fitting.LevMarLSQFitter()

x, y = data.shape

yy, xx = np.mgrid[0:x, 0:y]

with warnings.catch_warnings():
    # Ignore model linearity warning from the fitter
    warnings.simplefilter('ignore')
    p = fit_p(p_init, xx, yy, data)

bkg = p(xx, yy)
final = data - bkg

plt.matshow(bkg, cmap = 'viridis')
plt.matshow(final, cmap = 'viridis')

x, y = final.shape

print (x)
print (y)

alignbkg = np.empty([x, y])

for i in range(x-1):
    
    xx = np.empty(x)
    yy = np.empty(y)
    
    for j in range(y-1):
        xx[j] = final[i, j]
    
    # Fit the data using a Gaussian
    g_init = models.Polynomial1D(degree = 3)
    fit_g = fitting.LevMarLSQFitter()
    g = fit_g(g_init, xx, yy)
    
    alignbkg[i] = g(xx)
    
plt.matshow(alignbkg, cmap = 'viridis')

test1 = final - alignbkg

plt.matshow(test1, cmap = 'viridis')

plt.show()
