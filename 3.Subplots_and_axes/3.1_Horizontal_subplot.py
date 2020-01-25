# import necessary libraries
import matplotlib.pyplot as pl
import numpy as np

n = 256
# create linear space from -pi to pi
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
# create sine and cosine vectors
C, S = np.cos(X), np.sin(X)


# 3.1 Horizontal subplot
pl.figure(figsize=(6, 4))
pl.subplot(2, 1, 1)
pl.plot(X,S, color="red")

pl.subplot(3, 2, 5)
pl.plot(X,C, color="blue")

pl.subplot(3, 2, 6)
pl.plot(X,S, color="green")


pl.tight_layout()
pl.show()