import tkinter
import numpy

from matplotlib import pyplot

def ParseImage(points : numpy.array):
    
    xMax = points[numpy.argmax(points[:, 0]), 0]
    xMin = points[numpy.argmin(points[:, 0]), 0]
    yMax = points[numpy.argmax(points[:, 1]), 1]
    yMin = points[numpy.argmin(points[:, 1]), 1]    
    
    pyplot.Line2D(xMin, 0, xMax - xMin, 0, 'g')
    pyplot.plot([xMax, xMin], [yMax, yMin], 'ro')