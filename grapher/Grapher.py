import numpy as np
import matplotlib.pyplot as plt
import math

e = math.e # e = 2.718281828459045
pi = math.pi # pi = 3.141592653589793

def sin(x):
    return np.sin(x)

def cos(x):
    return np.cos(x)

def tan(x):
    return np.tan(x)

def cosec(x):
    return 1/sin(x)

def sec(x):
    return 1/cos(x)

def cot(x):
    return 1/tan(x)

def factorial(x):
    '''
    Factorial/Repeted Multiplication of number x.
    factorial(3) # 3*2*1
    >>> 6
    '''
    return np.math.factorial(x)

def sqrt(x):
    '''
    Square Root of a number x.
    sqrt(49)
    >>> 7.0
    '''
    return round(x**(0.5), 2)

def cbrt(x):
    '''
    Cube Root of a Number x.
    print(cbrt(125))
    >>> 5.0
    '''
    return round(x**(1./3.), 2)

def ln(x):
    return np.log(x)

def log(x, base=10):
    '''
    Find Logarithm of a number x.
    log(100)
    >>> 2.0

    log(64, 2)
    >>> 6.0
    '''
    return ln(x)/ln(base)

class Grapher:
    def __init__(self, fx, lb=-10, ub=10, step=0.01, label=True, grid=False, xlabel='x', title=None, lol="upper left", linestyle='-', mode='light', style=None):
        self.fx = fx
        self.lb = float(lb)
        self.ub = float(ub)
        self.step = float(step)
        self.grid = grid
        self.label = label
        self.x = np.arange(self.lb, self.ub, step=self.step)
        self.xlabel = xlabel
        self.ylabel = f'f ({xlabel})'
        self.title = title
        self.lol = lol
        self.linestyle = linestyle
        self.mode = mode
        self.style = style

    def valid_function(self, f):
        '''
        Create a human readable str(equation) to a more executable form.
        sinx -> sin(x)
        2^4 -> 2**4
        '''
        eq = f.replace('^', '**')
        if 'x' not in eq and len(eq) > 0:
            eq += '* x/x'

        eq = eq.replace('sinx', 'sin(x)')
        eq = eq.replace('cosx', 'cos(x)')
        eq = eq.replace('tanx', 'tan(x)')
        eq = eq.replace('cosecx', 'cosec(x)')
        eq = eq.replace('secx', 'sec(x)')
        eq = eq.replace('cotx', 'cot(x)')
        eq = eq.replace('lnx', 'ln(x)')
        eq = eq.replace('logx', 'log(x)')

        return eq

    def plot(self):
        '''
        Plot the graphs of many equations on one graph to see the relations between the graphs.
        You can use it to see how well Taylor Series match with the actuall graph of a function.

        Eg:
        g = Grapher(['sin(x)', 'x - ((x**3)/factorial(3)) + (x**5)/factorial(5)'], lb=-3, ub=3, grid=True)
        g.plot()
        '''
        if self.mode == 'dark':
            plt.style.use('dark_background')

        if self.style is not None:
            plt.style.use(self.style)

        x = self.x
        for f in self.fx:
            eq = self.valid_function(f)
            y = eval(eq)
            plt.plot(x, y, self.linestyle, label=f'{self.ylabel} = {str(f)}')
        if self.label:
            plt.legend(loc=self.lol)

        if self.grid:
            plt.grid()

        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        if self.title is not None:
            plt.title(self.title)

        plt.show()


if __name__ == '__main__':
    g = Grapher(['log(x)', 'lnx'], lb=-3, ub=3, label=True, lol='lower center', title='Taylor Polynomial for cos(x)')
    g.plot()
