# import necessary libraries
import matplotlib.pyplot as pl
import numpy as np


x = np.arange(-5,5,step=0.1)

pl.figure(figsize=(6, 4))


pl.subplot(2, 2, 1)
# tu będzie wykres
y1 = np.log(x**2)
pl.xlim(-5, 5)
pl.ylim(-3, 3)
pl.plot(x, y1)
pl.title('tytył wykresu 1')

pl.subplot(2, 2, 2)
y2 = np.log(np.abs(x))
pl.xlim(-5, 5)
pl.ylim(-3, 3)
pl.plot(x,y2)
pl.title('tytył wykresu 2')

pl.subplot(2, 2, 3)
y3 = np.tan(np.log(x+5))
pl.xlim(-5, 5)
pl.ylim(-3, 3)
pl.plot(x,y3)
pl.title('tytył wykresu 3')

pl.subplot(2, 2, 4)
y4 = np.cos(np.exp(x))
pl.xlim(-5, 5)
pl.ylim(-3, 3)
pl.plot(x,y4)
pl.title('tytył wykresu 4 ')

pl.tight_layout()
pl.show()