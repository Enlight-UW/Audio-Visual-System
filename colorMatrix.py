#!/usr/bin/env python
from samplebase import SampleBase


class colorMatrix(SampleBase):
    #init
    def __init__(self, *args, **kwargs):
        super(colorMatrix, self).__init__(*args, **kwargs)

    #
    def run(self):
        #create virtual matrix
        offset_canvas = self.matrix.CreateFrameCanvas()
        #forever
        while True:
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
