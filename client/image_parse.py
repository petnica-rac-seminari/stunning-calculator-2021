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
    #get the top-left and bottom-right most points
    minPoint, maxPoint = GetMinMaxPoints(points)

    #The space between the image and the border
    borderSpacing = numpy.array((3, 3))
    outputImageSize = numpy.array((28, 28))
    lineWidth = 4    
    
    #Map the points to [0, 1]
    points = (points - minPoint) / (maxPoint - minPoint)
        
    #Create an image double the size
    img = Image.new('L', tuple(outputImageSize * 2))
    context = ImageDraw.Draw(img)     

    #Draw lines
    for i in range(len(points) - 1):  
        point1 = points[i] * (outputImageSize * 2 - borderSpacing * 4) + borderSpacing * 2
        point2 = points[i + 1] * (outputImageSize * 2 - borderSpacing * 4) + borderSpacing * 2
        context.line([tuple(point1), tuple(point2)], fill = 'white', width = lineWidth)
        
    #img = img.transpose(Image.FLIP_TOP_BOTTOM)   

    img = img.resize((outputImageSize[0], outputImageSize[1]), Image.LANCZOS) 

    img.show()

    return numpy.array(img.getdata())