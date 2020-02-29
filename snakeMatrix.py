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
        self.oldXdelta = self.startXdelta
        self.oldYdelta = self.startYdelta
        self.alive = True;

        self.currentDotX = 5
        self.currentDotY = 10
        self.snakeBody = [[16,16]]
        return

    def cycle(self):

        if(self.alive):
            checkDotEat()
            getUserInput()

            self.snakeX += self.snakeXdelta
            self.snakeY += self.snakeYdelta

            checkUserDeath()
            updateSnake()
            updateScreen()

        return

    def updateScreen(self):
        self.gameScreen = [[0]*31]*31

        for x in range(0, len(snakeBody)-1):
            self.gameScreen[self.snakeBody[x][0]][self.snakeBody[x][1]] = 1

        self.gameScreen[self.currentDotX][self.currentDotY] = 1
        return


    def updateSnake(self):
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
        elif key == "a":
            print("a was pressed!")
            self.snakeYdelta = 0
            self.snakeXdelta = -1
        elif key == "s":
            print("s was pressed!")
            self.snakeYdelta = -1
            self.snakeXdelta = 0
        elif key == "d":
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
        self.snake = snake()
        super(colorMatrix, self).__init__(*args, **kwargs)

    #
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


# Main function
if __name__ == "__main__":
    #Create colorMatrix
    mat = colorMatrix()

    if (not mat.process()):
        print('broked')
