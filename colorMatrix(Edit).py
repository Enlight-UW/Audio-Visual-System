#!/usr/bin/env python
from samplebase import SampleBase

class Rainbow:
    g = 0
    b = 0
    r = 255
    size = 1
    step = 0
    positive = True
        
    def updateColor(col):
        if positive:
            col += size
        else:
            col -= size
            
        if col <= 0 or col >= 255:
            if col < 0:
                col = 0
            elif col > 255:
                col = 255
            step += 1 # Goes to the next step in the rainbow fade
            positive = not positive # since each step adds or subtracts from the variable
            if step >= 3: # loops the steps
                step = 0
        return col
    
    def nextColor():
        if step == 0:
            g = updateColor(g)
        elif step == 1:
            r = updateColor(r)
        else:
            b = updateColor(b)
            
        return [r,g,b]
        

class colorMatrix(SampleBase):
    
    def __init__(self, *args, **kwargs):
        super(colorMatrix, self).__init__(*args, **kwargs)

    def run(self):
        colorRow = [[0,0,0]]
        rainbow = Rainbow()
        offset_canvas = self.matrix.CreateFrameCanvas()
        while True: # Instead do while the 
            for j in range(self.matrix.width):
                # Using arraylist so you only need to make 1 new color at a time
                if j == 0 and len(colorRow) >= self.matrix.width: # To save memory
                    colorRow.remove(0)
                    colorRow.add(rainbow.nextColor())
                    
                elif len(colorRow) < len(colorRow):
                    colorRow.add(rainbow.nextColor())
                    
                color = colorRow[j]
                
                for i in range(self.matrix.width):
                    # if grid part is on
                    offset_canvas.SetPixel(i, j, color[0], color[1], color[2])
                    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                    

# Main function
if __name__ == "__main__":
    mat = colorMatrix()
    if (not mat.process()):
                print('broked')
