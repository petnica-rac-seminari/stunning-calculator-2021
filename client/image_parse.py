import tkinter
import numpy
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

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
    offset = (0, 0)    
    if (inputSize[0] > inputSize[1]):
        scale = inputSize[0]
        offset = (0, (inputSize[0] - inputSize[1]) / 2)
    else:
        scale = inputSize[1]
        offset = ((inputSize[1] - inputSize[0]) / 2, 0)    
    
    #[minPoint, maxPoint]
    #[-0.5, 0.5]
    #
    #[-outputSize / 2 + spacing, outputSize / 2 - spacing]
    #[spacing, outputSize - spacing]

    #map to [-0.5, 0.5]
    points = (points - minPoint + offset) / scale - 0.5        

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

def PlotGroup(group):
    for p in group:
        p = numpy.array(p)
        print('numpy array: ', p)        
        plt.plot(p[:, 0], p[:, 1], 'bo')    

def ParseImage(group : list) -> list:    

    #The space between the image and the border
    borderSpacing = numpy.array((6, 6))
    outputImageSize = numpy.array((28, 28))
    lineWidth = 3  
    
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

    img.show()
    
    return (numpy.array(img.getdata())).tolist()