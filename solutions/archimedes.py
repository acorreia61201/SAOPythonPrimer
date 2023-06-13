import numpy as np

def vertices(n):
    pi = np.pi # define pi locally from numpy
    vertices = [] # placeholder list for vertices
    for i in range(n):
        xi = 0.5*np.cos(2*pi*i/n) # x coordinate
        yi = 0.5*np.sin(2*pi*i/n) # y coordinate
        vertices.append((xi, yi)) # populate list with vertex
    return vertices

def perimeter(points):
    n = len(points) # get num of points from the input list
    peri = 0 # placeholder for perimeter
    for i in range(n):
        x1 = points[i] # get the current point
        x0 = points[i-1] # get the previous point; if i=0, this is the last point
        xdiff = x1[0] - x0[0] # difference in x coords
        ydiff = x1[1] - x0[1] # difference in y coords
        edge = np.sqrt(xdiff**2 + ydiff**2) # calculate edge length
        peri += edge # add the edge to the perimeter
    return peri
