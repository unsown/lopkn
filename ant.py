#Langton's Ant - www.101computing.net/langtons-ant



import turtle

import time

from random import randint



#Change this value to speed up or slow down this animation

animationSpeed=2



gridSize = 15

myPen = turtle.Turtle()

myPen.shape("turtle")

myPen.tracer(0)

myPen.speed(0)

myPen.color("#000000")

topLeft_x=-180

topLeft_y=180



#Draw the grid on screen (intDim is the width of a cell on the grid)

def drawGrid(grid,intDim):

  global gridSize

  global ant_row, ant_col, ant_direction

  #Clear the screen

  myPen.clear()

  for i in range(0,gridSize+1):

    myPen.penup()

    myPen.goto(topLeft_x,topLeft_y-i*intDim)

    myPen.pendown()

    myPen.goto(topLeft_x+gridSize*intDim,topLeft_y-i*intDim)

  for i in range(0,gridSize+1):

    myPen.penup()

    myPen.goto(topLeft_x+i*intDim,topLeft_y)

    myPen.pendown()

    myPen.goto(topLeft_x+i*intDim,topLeft_y-gridSize*intDim)

  for i in range(0,gridSize):

    myPen.penup()

    myPen.goto(topLeft_x+i*intDim+10,topLeft_y+10)

    myPen.write(chr(65+i))

  for i in range(1,gridSize+1):

    myPen.penup()

    myPen.goto(topLeft_x-15,topLeft_y-i*intDim+10)

    myPen.write(str(i)) 



  myPen.setheading(0)

  myPen.goto(topLeft_x,topLeft_y-intDim)

  for row in range (0,gridSize):

      for col in range (0,gridSize):

    		if grid[row][col]>0:

    		  box(intDim)

    		myPen.penup()

    		if row==ant_row and col==ant_col:

    		  myPen.color("#FF0000")

    		  x = myPen.xcor()

    		  y = myPen.ycor()

    		  myPen.goto(x+12,y+12)

    		  myPen.setheading(ant_direction)

    		  myPen.stamp()

    		  myPen.goto(x,y)

    		  myPen.color("#000000")

    		  myPen.setheading(0)

    		  

    		myPen.forward(intDim)

    		myPen.pendown()	

      myPen.setheading(270) 

      myPen.penup()

      myPen.forward(intDim)

      myPen.setheading(180) 

      myPen.forward(intDim*gridSize)

      myPen.setheading(0)

      myPen.pendown()





# This function draws a box by drawing each side of the square and using the fill function

def box(intDim):

    myPen.begin_fill()

    # 0 deg.

    myPen.forward(intDim)

    myPen.left(90)

    # 90 deg.

    myPen.forward(intDim)

    myPen.left(90)

    # 180 deg.

    myPen.forward(intDim)

    myPen.left(90)

    # 270 deg.

    myPen.forward(intDim)

    myPen.end_fill()

    myPen.setheading(0)





#Randomely populate the grid    

def randomGrid():

  global gridSize

  grid = []

  for row in range(0,gridSize):

   grid.append([])

   for col in range(0,gridSize):

      grid[row].append(randint(0,1))

  return grid    



#Create an empty grid    

def emptyGrid():

  global gridSize

  grid = []

  for row in range(0,gridSize):

   grid.append([])

   for col in range(0,gridSize):

      grid[row].append(0)

  return grid   



####################### MAIN PROGRAM STARTS HERE ######################

gridSize = 15

grid=emptyGrid()



#Position the Ant

ant_row = randint(5,10)

ant_col = randint(5,10)

ant_direction = randint(0,3)*90



#Start animating the grid

while ant_row>=0 and ant_row<gridSize and ant_col>=0 and ant_col<gridSize :

  #Change the direction of the ant based on the colour of the cell it's on

  if grid[ant_row][ant_col]==0:

     ant_direction-=90

     if ant_direction<0:

       ant_direction+=360

  else:   

     ant_direction+=90

     if ant_direction>=360:

       ant_direction-=360

  

  drawGrid(grid,25) #25 is the width of each square on the grid

  myPen.getscreen().update()	

  time.sleep(1/animationSpeed)

  #Apply Langton's Ant rules

  #Change the colour of the cell the ant was on

  if grid[ant_row][ant_col]==0:

     grid[ant_row][ant_col]=1

  else:   

     grid[ant_row][ant_col]=0

  

  #Move ant by 1 cell in the new direction

  if ant_direction==0:

    ant_col+=1

  elif ant_direction==90:

    ant_row-=1

  elif ant_direction==180:

    ant_col-=1

  elif ant_direction==270:

    ant_row+=1

