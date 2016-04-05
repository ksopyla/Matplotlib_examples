# 2.5 Moving spines

import pylab as pl
import numpy as np

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
C, S = np.cos(X), np.sin(X)
pl.figure(figsize=(10, 8), dpi=80)
pl.plot(X, C, color="blue", linewidth=2, linestyle=":")
pl.plot(X, S, color="red",  linewidth=2.5, linestyle="--")
pl.xlim(X.min() * 1.2, X.max() * 1.2)
pl.ylim(C.min() * 1.2, C.max() * 1.2)

# get current spines, move bottom and left one to figure center
ax = pl.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# apply ticks after moving spines
pl.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
          [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
pl.yticks([-1, -0.5, 0, 0.5, +1],
          [r'$-1$',r'$-0.5$', r'$0$',r'$0.5$', r'$+1$'])
          
print "2.5 Moving spines"
pl.show()