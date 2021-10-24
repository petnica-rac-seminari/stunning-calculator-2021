import tkinter
import numpy
from PIL import Image, ImageDraw, ImageFont

def GetMinMaxPoints(points):
    xMax = points[numpy.argmax(points[:, 0]), 0]
    xMin = points[numpy.argmin(points[:, 0]), 0]
    yMax = points[numpy.argmax(points[:, 1]), 1]
    yMin = points[numpy.argmin(points[:, 1]), 1]    
    return numpy.array((xMin, yMin)), numpy.array((xMax, yMax))

def ParseImage(points):
    minPoint, maxPoint = GetMinMaxPoints(points)

    print(points)    

    spacing = numpy.array((3, 3))
    outputSize = numpy.array((28, 28))
    line_width = 4

    minPoint = minPoint - spacing
    maxPoint = maxPoint + spacing
        
    img = Image.new('L', tuple(outputSize * 2))
    
    context = ImageDraw.Draw(img)     

    for i in range(len(points) - 1):  
        point1 = points[i] * (outputSize * 2- spacing * 2) + spacing
        point2 = points[i + 1] * (outputSize * 2 - spacing * 2) + spacing
        context.line([tuple(point1), tuple(point2)], fill = 'white', width = line_width)
        
    img = img.transpose(Image.FLIP_TOP_BOTTOM)   

    img = img.resize((outputSize[0], outputSize[1]), Image.LANCZOS) 
    
    print(img)
    #print(numpy.array(img.getdata()))
    return numpy.array(img.getdata())