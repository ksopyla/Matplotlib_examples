#%%

# import necessary libraries
import matplotlib.pyplot as pl
import numpy as np


n = 100
x = np.linspace(0, 10, n, endpoint=True)


# y1 = 1.2 * (x + np.random.rand(x.shape[0]))
# y2 = 2 * (x + np.random.rand(x.shape[0]))
# y3 = 2.4 * (x + np.random.rand(x.shape[0]))

y1 = 1.2 * x + np.random.rand(x.shape[0])
y2 = 2 * x +0.5+ np.random.rand(x.shape[0])
y3 = 2.4 *x +0.8+ np.random.rand(x.shape[0])

pl.plot(x, y1, color='blue', alpha=1.00)
pl.fill_between(x, 0, y1, color='blue', alpha=0.1)

pl.plot(x, y2, color='green', alpha=1.00)
pl.fill_between(x,y1, y2, color='green', alpha=.25)

pl.plot(x, y3, color='red', alpha=1.00)
pl.fill_between(x,y2, y3, color='red', alpha=.25)



pl.show()

# %%
