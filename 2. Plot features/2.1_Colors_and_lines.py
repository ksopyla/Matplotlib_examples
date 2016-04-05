# 2.1 Changing colors and line widths

import pylab as pl
import numpy as np

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
C, S = np.cos(X), np.sin(X)

# create a new figure with dimensions 10x8 inches, set dpi to 80
pl.figure(figsize=(10, 8), dpi=80)

# plot cosine using blue color, line width of 2 px, dotted
pl.plot(X, C, color="blue", linewidth=3, linestyle=":")

# plot sine using red color, line width of 2.5 px, dashed
pl.plot(X, S, color="red",  linewidth=2.5, linestyle="--")

print "2.2 Changing line colors and widths"
pl.show()