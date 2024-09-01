
import time
from typing import List, Any

import dxcam
import numpy as np
import cv2
from memory_profiler import profile
from colorthief import ColorThief


@profile
def main():

    def capture_ss():

        screen = dxcam.create(output_color="BGRA")
        frame = cv2.resize(src=screen.grab(), dsize=(320, 240))
        if frame is None: return
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGBA)
        cv2.imwrite("ss.jpg", frame)
        time.sleep(0.5)

    def colorfinder():

        ct = ColorThief("ss.jpg")
        color = ct.get_palette(color_count=4,quality=1)
        print(color)

        def show_palette(rgb_vals,count):

            #Create a blank image of size 800x800 with 3 color channels (BGR)
            image = np.zeros((800, 800, 3), dtype=np.uint8)
            if count == 1 :
                image[:] =rgb_vals[0]
            if count == 2 :
                image[:,:400] =rgb_vals[0]
                image[:,400:] = rgb_vals[0]
            if count == 3 :
                image[:400,:] = rgb_vals[0]
                image[400:,:400] = rgb_vals[1]
                image[400:,400:] = rgb_vals[2]
            if count == 4 :
                image[:400, :400] = rgb_vals[0]  # left top
                image[400:, :400] = rgb_vals[1]  # left bottom
                image[:400, 400:] = rgb_vals[2]  # right top
                image[400:, 400:] = rgb_vals[3]  # right bottom

            cv2.imshow("colour palette",image )
            cv2.waitKey(3000)
            cv2.destroyAllWindows()

        #show_palette(color,1)

    while True:
        capture_ss()
        colorfinder()




if __name__ == '__main__':
    time.sleep(4)
    main( )
