import numpy as np

def sin(x):
    return np.sin(x)

def d(x, func):
    dx = 0.01
    eq = f"({func.replace('x', f'(x + {dx})') + f' - {func}'})/dx"
    print(eq)
    return eval(eq)

x = np.arange(0, 1, step=0.1)
print(d(x, 'x**2'))
