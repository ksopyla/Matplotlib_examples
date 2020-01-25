# 2.6 Adding legend
# import necessary libraries
import matplotlib.pyplot as pl
import numpy as np


n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
C, S = np.cos(X), np.sin(X)
pl.figure(figsize=(10, 8), dpi=80)

# add labels to sine and cosine
pl.plot(X, C, color="blue", linewidth=2, linestyle=":", label="cosine")
pl.plot(X, S, color="red",  linewidth=2.5, linestyle="--", label="sine")

pl.xlim(X.min() * 1.2, X.max() * 1.2)
pl.ylim(C.min() * 1.2, C.max() * 1.2)
ax = pl.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
pl.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
          [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
pl.yticks([-1, 0, +1],
          [r'$-1$', r'$0$', r'$+1$'])
          
# display legend
# possible locations: right, center left, upper right, lower right,	best, center
# lower left, center right, upper left, upper center, lower center, 

pl.legend(loc='best')
#pl.legend()
          
print("2.6 Adding legend")
pl.show()