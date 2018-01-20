# 2.3 Setting ticks
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

# set ticks to show more significant values
pl.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
pl.yticks([-1, 0, +1])

print("2.3 Setting plot ticks")
pl.show()