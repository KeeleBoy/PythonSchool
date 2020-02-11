import math

#Cube Calculation
#Author Kyle Warchuck
#9/6/17
#This program displays the area of a cube side, along with
#The total area and volume from entering one edge

#Calculations
def calcSurfaceArea():
    global surfaceArea
    surfaceArea = pow(edge,2)

def calcTotalArea():
    global totalArea
    totalArea = surfaceArea * SIDES

def calcTotalVolume():
    global totalVolume
    totalVolume = pow(edge,3)

#declare variables
edge = 0.0
surfaceArea = 0.0
totalArea = 0.0
totalVolume=0.0

#declare constant
SIDES = 6

#get input from console
edge = float(input ("please enter an edge: "))
calcSurfaceArea()
calcTotalArea()
calcTotalVolume()

#Display values
print("the value you entered is: ",(edge))
print("The surface area is: ",(surfaceArea))
print("the total area is: ",(totalArea))
print("The total volume is: ", (totalVolume))
print("program has finished")
