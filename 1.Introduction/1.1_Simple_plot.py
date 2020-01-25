# 1.1 Simple plot

# import necessary libraries
import matplotlib.pyplot as pl
import numpy as np

# define number of samples to generate
n = 256
# create linear space from -pi to pi
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
# create sine and cosine vectors
C, S = np.cos(X), np.sin(X)
# plot cosine
pl.plot(X, C)
# plot sine
pl.plot(X, S)

print("1.1 Simple plotting example")
# show finished plot
pl.show()