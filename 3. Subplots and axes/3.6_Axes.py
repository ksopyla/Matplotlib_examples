# import necessary libraries
import matplotlib.pyplot as pl
import numpy as np

pl.axes([.1, .1, .5, .5])
pl.xticks(())
pl.yticks(())
pl.text(0.1, 0.1, 'axes([0.1,0.1, .5, .5])', ha='left', va='center',
        size=16, alpha=.5)

pl.axes([.2, .2, .5, .5])
pl.xticks(())
pl.yticks(())
pl.text(0.1, 0.1, 'axes([0.2,0.2,.5,.5])', ha='left', va='center',
        size=16, alpha=.5)

pl.axes([0.3, 0.3, .5, .5])
pl.xticks(())
pl.yticks(())
pl.text(0.1, 0.1, 'axes([0.3,0.3,.5,.5])', ha='left', va='center',
        size=16, alpha=.5)

pl.axes([.4, .4, .5, .5])
pl.xticks(())
pl.yticks(())
pl.text(0.1, 0.1, 'axes([0.4,0.4,.5,.5])', ha='left', va='center',
        size=16, alpha=.5)

pl.show()