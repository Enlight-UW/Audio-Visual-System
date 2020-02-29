#!/usr/bin/env python
from samplebase import SampleBase
import random
import keyboard

class snake(object):

	def __init__(self):
		self.gameScreen = [[0]*31]*31

		self.snakeX = 16
		self.snakeY = 16
		self.snakeXdelta = 1
		self.snakeYdelta = 0
		self.oldXdelta = startXdelta
		self.oldYdelta = startYdelta
		self.alive = True;

		self.currentDotX = 5
		self.currentDotY = 10

		self.snakeBody = [[16,16]]

	def cycle(self):

            if(self.alive):

		checkDotEat()
		getUserInput()

		self.snakeX += snakeXdelta
		self.snakeY += snakeYdelta

		checkUserDeath()
                updateSnake()
                updateScreen()

            return

	def updateScreen(self):
            self.gameScreen = [[0]*31]*31

            for x in range(0, len(snakeBody)-1):
                self.gameScreen[snakeBody[x][0]][snakeBody[x][1]] = 1

            self.gameScreen[currentDotX][currentDotY] = 1
            return
        

        def updateSnake(self)
            for x in range(0, len(snakeBody)-1):
                self.snakeBody[x+1] = self.snakeBody[x]

            self.snakeBody[0] = [self.snakeX, self.snakeY]
            return
        

	def getUserInput(self):

            key = keyboard.read_key()
            
            if key == "w":
                print("W was pressed!")
                self.snakeYdelta = 1
                self.snakeXdelta = 0
            else if key == "a":
                print("a was pressed!")
                self.snakeYdelta = 0
                self.snakeXdelta = -1
            else if key == "s":
                print("s was pressed!")
                self.snakeYdelta = -1
                self.snakeXdelta = 0
            else if key == "d":
                print("d was pressed!")
                self.snakeYdelta = 0
                self.snakeXdelta = 1

            return            
                
            
        def checkDotEat(self):
            if((snakeX == currentDotX) & (snakeY == currentDotY)):
		self.snakeBody.append([-1,-1])
		self.currentDotX = (random.random() * 100) % 32
		self.currentDotY = (random.random() * 100) % 32
	    return

        def checkUserDeath(self):
            for x in range(0, len(snakeBody)):
		if ((snakeX == snakeBody[x][0]) | (snakeY == snakeBody[x][1])):
                    self.alive = False
            return

        def getGameScreen(self):
            return self.gameScreen
            

class colorMatrix(SampleBase):
    
	def __init__(self, *args, **kwargs):
		super(colorMatrix, self).__init__(*args, **kwargs)

	#
	def run(self):
		#create virtual matrix
                snake = snake()
		offset_canvas = self.matrix.CreateFrameCanvas()
		#forever
		while True:
                        snake.cycle()
                    
			for x in range(0, self.matrix.width):
				#column, row, red, blue, green
				offset_canvas.SetPixel(1, x, 255, 0, 0)
				offset_canvas = self.matrix.SwapOnVSync(offset_canvas)

			for x in range(0, self.matrix.width):
				offset_canvas.SetPixel(1, x, 0, 0, 0)


# Main function
if __name__ == "__main__":
	#Create colorMatrix
	mat = colorMatrix()

	if (not mat.process()):
				print('broked')
