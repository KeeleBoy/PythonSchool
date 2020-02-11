#Cube Calculation
#Author Kyle Warchuck
#9/6/17
#This program displays the area of a cube side, along with
#The total area and volume

face = int(input ("please enter Face width; "))
faceArea = face * face
totalarea = 6 * faceArea
totalvolume = face * face * face
print("The face area is = ", int(faceArea))
print("The total area of the cube is = ", int(totalarea))
print("The total volume of the cube is = ", int(totalvolume))
