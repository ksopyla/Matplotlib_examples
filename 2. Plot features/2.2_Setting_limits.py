
import pylab as pl
import numpy as np

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
C, S = np.cos(X), np.sin(X)

pl.figure(figsize=(10, 8), dpi=80)
pl.plot(X, C, color="blue", linewidth=2, linestyle=":")
pl.plot(X, S, color="red",  linewidth=2.5, linestyle="--")

#set x and y limits to 120% of extremes
pl.xlim(X.min() * 1.2, X.max() * 1.2)
pl.ylim(C.min() * 1.2, C.max() * 1.2)

print "2.3 Setting plot limits"
pl.show()