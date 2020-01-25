# 2.4 Setting tick labels
# import necessary libraries
import matplotlib.pyplot as pl
import numpy as np


n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
C, S = np.cos(X), np.sin(X)
pl.figure(figsize=(10, 8), dpi=80)
pl.plot(X, C, color="blue", linewidth=2, linestyle=":")
pl.plot(X, S, color="red",  linewidth=2.5, linestyle="--")
pl.xlim(X.min() * 1.2, X.max() * 1.2)
pl.ylim(C.min() * 1.2, C.max() * 1.2)

# create latex-style labels for ticks
pl.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
          [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

pl.yticks([-1, 0, +1],
          [r'min', r'0', r'max'])
          
print("2.4 Setting plot tick labels")
pl.show()