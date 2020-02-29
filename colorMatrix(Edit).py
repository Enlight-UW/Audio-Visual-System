#!/usr/bin/env python
from samplebase import SampleBase

class Rainbow(object):
    def __init__(self):
        self.lastTime = 0
        self.g = 0
        self.b = 0
        self.r = 255
        self.size = 10
        self.step = 0
        self.positive = True
        
    def updateColor(self, col):
        if self.positive:
            col += self.size
        else:
            col -= self.size
            
        if col <= 0 or col >= 255:
            if col < 0:
                col = 0
            elif col > 255:
                col = 255
            self.step += 1 # Goes to the next step in the rainbow fade
            self.positive = not self.positive # since each step adds or subtracts from the variable
            if self.step >= 3: # loops the steps
                self.step = 0
        return col
    
    def nextColor(self):
        if self.step == 0:
            self.g = self.updateColor(self.g)
        elif self.step == 1:
            self.r = self.updateColor(self.r)
        elif self.step == 2:
            self.b = self.updateColor(self.b)
        else:
            self.step = 0
            self.nextColor()
            
        return [self.r,self.g,self.b]
        

class colorMatrix(SampleBase):
    
    def __init__(self, *args, **kwargs):
        self.colorRow = []
        self.rainbow = Rainbow()
        self.WAIT_MICROSECONDS = 20000
        self.volumeBased = False
        self.outputHeights = []
        self.setUpTestOutputs()
        self.lastTime = 0
        super(colorMatrix, self).__init__(*args, **kwargs)
        
        
    def setUpTestOutputs(self):
        file = open("test(Dynasty).txt","r")
        with file as rl:
            for line in rl.readlines():
                lines = line.split(",")
        
        for line in lines:
            if len(line) > 0:
                self.outputHeights.append(int(line))

    def updateImageFB(self):
        for i in range(self.matrix.width):
            self.turnPixelOn(i, self.outputHeights[self.lastTime * self.matrix.width + i])

    def turnPixelOn(self, x, maxY):
          # Using arraylist so you only need to make 1 new color at a time
        if x == 0 and len(self.colorRow) >= self.matrix.width: # To save memory
            del self.colorRow[0]
            tempColor = self.rainbow.nextColor()
            self.colorRow.append(tempColor)
            
        elif len(self.colorRow) < self.matrix.width:
            tempColor = self.rainbow.nextColor()
            self.colorRow.append(tempColor)
            
        color = self.colorRow[x]
                
        if maxY > self.matrix.width:
            maxY = self.matrix.width
            
        for y in range(self.matrix.width):
            if y < maxY:
                self.offset_canvas.SetPixel(self.matrix.width - 1 - y, x, color[0], color[1], 255)
            else:
                self.offset_canvas.SetPixel(self.matrix.width - 1 - y, x, 0, 0, 0)
                
        self.offset_canvas = self.matrix.SwapOnVSync(self.offset_canvas)

    def run(self):
        self.offset_canvas = self.matrix.CreateFrameCanvas()
        while True: # Instead do while the 
            self.lastTime += 1# = int(clip.getMicrosecondPosition() / self.WAIT_MICROSECONDS)
            
                #delay from processing the data. Also maybe from slow Java GUI
            #if self.volumeBased:
            #    updateImageVB()
            #else:
            self.updateImageFB()
                
            #self.usleep(self.WAIT_MICROSECONDS)
                    

# Main function
if __name__ == "__main__":
    mat = colorMatrix()
    if (not mat.process()):
                print('broked')
