import numpy as np

def trapezoidal(a, b, n, f):
    grid = np.linspace(a, b, n) # grid with n points and bounds [a, b]
    dx = (b-a)/(n-1) # separation between points
    sum = f(a) + f(b) # placeholder containing endpoints
    for i in range(1, n-1): # iterate over all points except first and last
        sum += 2*f(grid[i]) # add each contribution
    return sum*dx/2 # multiply prefactor

def montecarlo(a, b, n, f):
    grid = np.random.uniform(a, b, n) # random grid of n points in domain [a, b]
    V = b - a # 1D volume
    sum = 0 # placeholder for summation
    for i in grid:
        sum += f(i) # add contributions from each element
    return sum*V/n # multiply prefactor
