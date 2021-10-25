import tkinter
import numpy
from PIL import Image, ImageDraw, ImageFont

def ConvertGroup(group):
    arr = []    

    for i in range(len(group)):
        arr.append(numpy.array(group[i]))        

    return arr

def GetPointsMinMax(points):    
    xMax = points[numpy.argmax(points[:, 0]), 0]
    xMin = points[numpy.argmin(points[:, 0]), 0]
    yMax = points[numpy.argmax(points[:, 1]), 1]
    yMin = points[numpy.argmin(points[:, 1]), 1]    
    return xMin, yMin, xMax, yMax

def GetGroupMinMax(group):    
    xMin = numpy.inf
    yMin = numpy.inf
    xMax = -numpy.inf
    yMax = -numpy.inf

    for i in range(len(group)):
        if len(group[i]) > 0:
            xMinTemp, yMinTemp, xMaxTemp, yMaxTemp = GetPointsMinMax(group[i])

            xMin = min(xMin, xMinTemp)
            yMin = min(yMin, yMinTemp)
            xMax = max(xMax, xMaxTemp)
            yMax = max(yMax, yMaxTemp)
    
    return numpy.array((xMin, yMin)), numpy.array((xMax, yMax))    

def TransformPoints(points, minPoint, maxPoint, outputSize, spacing):    
    inputSize = maxPoint - minPoint
    scale = max(inputSize[0], inputSize[1])
    
    #map to [-0.5, 0.5]
    points = (points - minPoint) / scale - 0.5

    #map to [spacing, size - spacing]
    points = points * (outputSize - spacing * 2) + outputSize / 2   

    # [-outputSize / 2 + spacing, outputSize / 2 - spacing]
    # [ spacing, outputSize - spacing]
    #
    # [spacing, outputSize - spacing]

    return points

def TransformGroup(group, min, max, size, spacing):  
    for i in range(len(group)):
        if len(group[i]) > 0:
            group[i] = TransformPoints(group[i], min, max, size, spacing)    
    return group

def DrawPoints(points, context, width):
    for i in range(len(points) - 1):          
        context.line([tuple(points[i]), tuple(points[i + 1])], fill = 'white', width = width)

def DrawGroup(group, context, width):
    for i in range(len(group)):
        if len(group[i]) > 1:
            DrawPoints(group[i], context, width)   

def ParseImage(group : list) -> list:
    #The space between the image and the border
    borderSpacing = numpy.array((3, 3))
    outputImageSize = numpy.array((28, 28))
    lineWidth = 4  
    
    #Create an image double the size    
    img = Image.new('L', tuple(outputImageSize * 2))
    context = ImageDraw.Draw(img)     

    #get the top-left and bottom-right most points
    group = ConvertGroup(group)
    minPoint, maxPoint = GetGroupMinMax(group)      

    group = TransformGroup(group, minPoint, maxPoint, outputImageSize * 2, borderSpacing * 2)    

    DrawGroup(group, context, lineWidth)    

    #img = img.transpose(Image.FLIP_TOP_BOTTOM)       

    img = img.resize((outputImageSize[0], outputImageSize[1]), Image.LANCZOS)   
    
    return (numpy.array(img.getdata())).tolist()