#%%
# import necessary libraries
import matplotlib.pyplot as pl
import numpy as np

#%%

X = np.arange(1,21)
Y = np.sqrt(X)
S = np.random.rand(X.shape[0]) * 300


# rgb colors, reddish, greenish
rgb = np.array([[255,20,20],
[20,255,20]
])
# normalize to float from [0,1]
rgb= rgb/255.0

# gen 0,1,0,1.. indexes
idx = [ i%2 for i in range(X.shape[0])]

# choose colors alternately
T = rgb[idx,:]

pl.axes([0.025, 0.025, 0.95, 0.95])
pl.scatter(X, Y, s=S, c=T, alpha=.5)


pl.show()

# %%
