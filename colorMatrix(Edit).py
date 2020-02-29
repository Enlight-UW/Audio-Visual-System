#!/usr/bin/env python
from samplebase import SampleBase

class Rainbow(object):
    def __init__(self):
        self.g = 0
        self.b = 0
        self.r = 255
        self.size = 1
        self.step = 0
        self.positive = True
        self.lastTime = 0
        self.outputHeights = []
        self.setUpTestOutputs()
        
    def setUpTestOutputs(self):
        file = open("test(Dynasty).txt","r")
        with file as rl:
            for line in rl.readlines():
                lines = line.split(",")
        
        for line in lines:
            if len(line) > 0:
                self.outputHeights.append(int(line))
        
    def updateColor(col, self):
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
        else:
            self.b = self.updateColor(self.b)
            
        return [self.r,self.g,self.b]
        

class colorMatrix(SampleBase):
    
    def __init__(self, *args, **kwargs):
        self.colorRow = []
        self.rainbow = Rainbow()
        self.WAIT_MICROSECONDS = 20000
        self.volumeBased = False
        super(colorMatrix, self).__init__(*args, **kwargs)

    def updateImageFB(self):
        for i in range(self.matrix.width):
            self.turnPixelOn(i, self.outputHeights[self.lastTime * self.matrix.width + i])

    def turnPixelOn(x, maxY, self):
        offset_canvas = self.matrix.CreateFrameCanvas()
          # Using arraylist so you only need to make 1 new color at a time
        if x == 0 and len(self.colorRow) >= self.matrix.width: # To save memory
            self.colorRow.remove(0)
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
                offset_canvas.SetPixel(self.matrix.width - 1 - y, x, color[0], color[1], color[2])
            else:
                offset_canvas.SetPixel(self.matrix.width - 1 - y, x, 0, 0, 0)
                
        offset_canvas = self.matrix.SwapOnVSync(offset_canvas)

    def run(self):
        while True: # Instead do while the 
            self.lastTime += 1# = int(clip.getMicrosecondPosition() / self.WAIT_MICROSECONDS)
            
                #delay from processing the data. Also maybe from slow Java GUI
            #if self.volumeBased:
            #    updateImageVB()
            #else:
            self.updateImageFB()
                
            self.usleep(self.WAIT_MICROSECONDS)
                    

# Main function
if __name__ == "__main__":
    mat = colorMatrix()
    if (not mat.process()):
                print('broked')
