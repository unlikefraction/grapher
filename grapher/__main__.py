from grapher import Grapher

g = Grapher(['cos(x)', '1 - ((x^2)/factorial(2)) + (x^4)/factorial(4)'], lb=-3, ub=3, label=True, lol='lower center', title='Taylor Polynomial for cos(x)')
g.plot()

g = Grapher(['cosx', 'sinx'], label=True, title='cosx vs sinx')
g.plot()
