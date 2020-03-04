#!/usr/bin/env python
from samplebase import SampleBase
import random
import time
import termios
import sys
import tty

def _find_getch():

        def _getch():
                fd = sys.stdin.fileno()
                old_settings = termios.tcgettr(fd)
                try:
                        tty.setraw(fd)
                        ch = sys.stdin.read(1)
                finally:
                        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                return ch

        return _getch

class snake(object):

    def __init__(self):
        self.gameScreen = []

        self.snakeX = 16
        self.snakeY = 16
        self.snakeXdelta = 1
        self.snakeYdelta = 0
        self.oldXdelta = self.snakeXdelta
        self.oldYdelta = self.snakeYdelta
        self.alive = True;

        self.currentDotX = 5
        self.currentDotY = 10
        self.snakeBody = [[16,16]]
        return

    def cycle(self):

        if(self.alive):
            self.checkDotEat()
            #self.getUserInput()

            self.snakeX = (self.snakeX + self.snakeXdelta)%32
            self.snakeY = (self.snakeY + self.snakeYdelta)%32

            self.checkUserDeath()
            self.updateSnake()
            self.updateScreen()

        return

    def updateScreen(self):
        self.gameScreen = [[0 for x in range(32)] for y in range(32)]

        #for each element of the snake body, draw a 1 on the matrix        
        for x in range(0, len(self.snakeBody)):
            self.gameScreen[self.snakeBody[x][0]][self.snakeBody[x][1]] = 1
        
        #draw the pellet
        #self.gameScreen[self.currentDotX][self.currentDotY] = 1
        self.gameScreen[5][5] = 1
        return


    def updateSnake(self):
        for x in range(0, len(self.snakeBody)-1):
            self.snakeBody[x+1] = self.snakeBody[x]

        self.snakeBody[0] = [self.snakeX, self.snakeY]
        return


    def getUserInput(self):
        
        char = _find_getch()
        print(char) 
        return


    def checkDotEat(self):
        if((self.snakeX == self.currentDotX) & (self.snakeY == self.currentDotY)):
            self.snakeBody.append([-1,-1])
            self.currentDotX = (random.random() * 100) % 32
            self.currentDotY = (random.random() * 100) % 32
        return

    def checkUserDeath(self):
        for x in range(1, len(self.snakeBody)):
            if ((self.snakeX == self.snakeBody[x][0]) | (self.snakeY == self.snakeBody[x][1])):
                self.alive = False
        return

    def getGameScreen(self):
        return self.gameScreen


class colorMatrix(SampleBase):

    def __init__(self, *args, **kwargs):
        self.snake = snake()
        super(colorMatrix, self).__init__(*args, **kwargs)


    def run(self):

        #create virtual matrix
        
        offset_canvas = self.matrix.CreateFrameCanvas()
        tmp_matrix = snake.getGameScreen

        #forever
        while True:
            self.snake.cycle()
            tmp_matrix = self.snake.getGameScreen()
            color = 0

            for x in range(0, self.matrix.width):
                for y in range(0, self.matrix.height):
                    #column, row, red, blue, green
                    color = tmp_matrix[x][y]
                    offset_canvas.SetPixel(x, y, 255*color, 0, 0)

            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
            print("End of Cycle!")

# Main function
if __name__ == "__main__":
    #Create colorMatrix
    mat = colorMatrix()

    if (not mat.process()):
        print('broked')
