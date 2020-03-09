#!/usr/bin/env python
from samplebase import SampleBase
import datetime
        

class colorMatrix(SampleBase):
    
    def __init__(self, *args, **kwargs):
        # 5 per number(4 numbers) + 4 spaces + 1 colon + 1 since 0 start, 32x32
        self.offset_x = 32 - 26
        self.offset_y = 8 # 9 height of number - 1 since 0 start
        super(colorMatrix, self).__init__(*args, **kwargs)
        
    def getNumber(self, num):
        numMatrix = [] #5 x 9
        if num == 0:
            for i in range(3):
                numMatrix.append([i + 1, 0])
                numMatrix.append([i + 1, 8])
            for i in range(7):
                numMatrix.append([0, i + 1])
                numMatrix.append([4, i + 1])
        elif num == 1:
            numMatrix.append([1, 0]) # top part
            #numMatrix.append([2, 7])
            #numMatrix.append([4, 7])
            for i in range(9):
                numMatrix.append([2, i]) # line down
            for i in range(2):
                numMatrix.append([i, 8]) #(left)line at bottom
                numMatrix.append([i, 1]) # Line at top
                numMatrix.append([i + 3, 8]) #(right) line at bottom
        elif num == 2:
            numMatrix.append([0, 1])
            for i in range(3):
                numMatrix.append([i + 1, 0]) # top line
                numMatrix.append([0, i + 6]) # bottom side line
                numMatrix.append([4 - i, i + 3]) # Diagonal line
            for i in range(2):
                numMatrix.append([4, i + 1]) # right side line
            for i in range(4):
                numMatrix.append([i + 1, 7]) # bottom line
        elif num == 3:
            numMatrix.append([0, 1])
            numMatrix.append([0, 7])
            for i in range(3):
                numMatrix.append([i + 1, 0]) # top line
                numMatrix.append([4, i + 5]) # bottom side line
                numMatrix.append([4, i + 1]) # top side line
                numMatrix.append([i + 1, 4]) # mid line
                numMatrix.append([i + 1, 8]) # bot line
        elif num == 4:
            numMatrix.append([4, 5])
            for i in range(9):
                numMatrix.append([4, i]) # line down
            for i in range(3):
                numMatrix.append([i, 3 - i]) # diagonal top
                numMatrix.append([i, 4 - i]) # diagonal below
                numMatrix.append([i, 5]) # line across
        elif num == 5:
            for i in range(5):
                numMatrix.append([i, 0]) # top line
            for i in range(4):
                numMatrix.append([i, 8]) # bot line
                numMatrix.append([i, 3]) # mid line
                numMatrix.append([4, i + 4]) # right line
            for i in range(2):
                numMatrix.append([0, i + 1]) # left line
        elif num == 6:
            numMatrix.append([1,1])
            for i in range(6):
                numMatrix.append([0, i + 2]) # left line
            for i in range(3):
                numMatrix.append([i + 2, 0]) # top line
                numMatrix.append([i + 1, 4]) # mid line
                numMatrix.append([i + 1, 8]) # bot line
                numMatrix.append([4, i + 5]) # right line
        elif num == 7:
            numMatrix.append([4, 1])
            for i in range(5):
                numMatrix.append([i, 0]) # Top line
            for i in range(3): # Diagonal line
                numMatrix.append([0, 6 + i])
                numMatrix.append([1, 4 + i])
                numMatrix.append([2, 2 + i])
                numMatrix.append([3, 1 + i])
        elif num == 8:
            for i in range(3):
                numMatrix.append([i + 1, 0])
                numMatrix.append([i + 1, 4])
                numMatrix.append([i + 1, 8])
                numMatrix.append([0, i + 1])
                numMatrix.append([0, i + 5])
                numMatrix.append([4, i + 1])
                numMatrix.append([4, i + 5])
        elif num == 9:
            for i in range(3):
                numMatrix.append([i + 1, 0])
                numMatrix.append([i + 1, 4])
                numMatrix.append([0, i + 1])
            for i in range(8):
                numMatrix.append([4, i + 1])
                
        return numMatrix
    
    def getTimeMat(self, num, x_offset):
        time_matrix = []
        for pos in self.getNumber(int(num/10)): # first num
            pos[0] += 8
            pos[1] += 8 + x_offset
            time_matrix.append(pos)
                
        for pos in self.getNumber(int(num%10)): # Second num
            pos[0] += 8 + 6 + x_offset # 6 for the 2nd number
            pos[1] += 8
            time_matrix.append(pos)
            
        return time_matrix
    
    def updateTime(self):
        time = datetime.datetime.now()
        hour = time.hour % 12
        minute = time.minute
        
        # Keep track of previous matrix
        for pos in self.getTimeMat(hour, 0):
            """Not sure if x, y or y, x, doesn't really matter if the matrix 
            can be tilted either way"""
            self.offset_canvas.SetPixel(pos[0], pos[1], 255, 255, 255)
            
        for pos in self.getTimeMat(minute, 13):
            self.offset_canvas.SetPixel(pos[0], pos[1], 255, 255, 255)
                
        self.offset_canvas = self.matrix.SwapOnVSync(self.offset_canvas)

    def run(self):
        self.offset_canvas = self.matrix.CreateFrameCanvas()
        while True: # Instead do while the 
            self.updateTime()
            
                    

# Main function
if __name__ == "__main__":
    mat = colorMatrix()
    if (not mat.process()):
                print('broked')
