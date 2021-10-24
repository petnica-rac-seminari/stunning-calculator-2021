import random
from matplotlib import pyplot
import numpy
import image_parse

def ShowPoints(points):    
    pyplot.plot(points[:, 0], points[:, 1], 'bo')    

points = numpy.array([()])
points.resize((100, 2))

for x in range(100):
    points[x] = (random.random(), random.random())

ShowPoints(points)

image_parse.ParseImage(points)

pyplot.show()