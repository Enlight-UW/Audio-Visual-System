#!/usr/bin/env python
from samplebase import SampleBase
import time

class colorMatrix(SampleBase):
    def __init__(self, *args, **kwargs):
        super(colorMatrix, self).__init__(*args, **kwargs)

    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas()
        while True:
            for x in range(0, self.matrix.width):
                offset_canvas.SetPixel(1, x, 255, 0, 0)
                offset_canvas.SetPixel(1, x-1, 0, 0, 0)
                offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                offset_canvas.SetPixel(1, x, 255, 0, 0)
                offset_canvas.SetPixel(1, x-1, 0, 0, 0)
                offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                time.sleep(.5)


# Main function
if __name__ == "__main__":
    mat = colorMatrix()
    if (not mat.process()):
                print('broked')
