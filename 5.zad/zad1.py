
import numpy as np
import  matplotlib.pyplot as pl

# f(x)=sin(n*x) n [1-5]

x = np.linspace(-np.pi,np.pi,100)

N = [1,2,3,4,5]

line_styles = [
    ("blue", ":"),
    ("red", "-"),
    ("green", "--"),
    ("orange", "-."),
    ("magenta", "-"),
]

pl.figure()

for n,cs in zip(N,line_styles):
    print(n,cs[0],cs[1])
    color = cs[0]
    style = cs[1]

    y= np.sin(n*x)

    label = f'sin({n}x)'
    pl.plot(x,y,
            color=color,
            linestyle=style,
            label=label)

pl.title('wykresy sin(nx)')
pl.yticks(np.arange(-1,1.5,0.5))

pl.legend()
pl.show()