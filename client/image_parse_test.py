import random
from matplotlib import pyplot
import numpy
import image_parse

def GenerateRandomPoints():
    points = numpy.array([()])

    count = 10
    points.resize((count, 2))

    for x in range(count):
        points[x] = (random.random(), random.random())

    return points

#points = numpy.array(points)
points = GenerateRandomPoints()

minPoint, maxPoint = image_parse.GetMinMaxPoints(points)

fig, ax = pyplot.subplots()

rect = pyplot.Rectangle((minPoint[0], minPoint[1]), maxPoint[0] - minPoint[0], maxPoint[1] - minPoint[1], fill = False)

ax.scatter(points[:, 0], points[:, 1], marker = ".")    
ax.add_patch(rect)
ax.scatter([maxPoint[0], minPoint[0]], [maxPoint[1], minPoint[1]], marker = ".")

print(points)
result = image_parse.ParseImage(points)
print(result)
pyplot.show()