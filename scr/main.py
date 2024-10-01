import sys
import time

from fastgrab import screenshot
import numpy as np
import cv2
from memory_profiler import profile
import fast_colorthief


@profile
def main():
    while_count = 0
    #start_time = time.time( )

    def SS_Getter():
        # BGRA is the output format that consumes the least memory
        try:
            frame = cv2.resize(screenshot.Screenshot( ).capture( ), dsize=(1280, 720))  # 320p
        except cv2.error:
            return
        # frame = cv2.pyrDown() #downsample 2x
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGBA)
        #cv2.imwrite("ss.jpg", frame)

        return frame

    def colorfinder(image):

        color = fast_colorthief.get_palette(image, color_count=3, quality=1, use_gpu=False)
        return color

    def show_palette(rgb_vals, count):  # (optional)-> fucn to show the colour palette
        # Cerate a blank image of size 800x800 with 3 color
        image = np.zeros((800, 800, 3), dtype=np.uint8)
        if count == 1:
            image[:] = rgb_vals[0]
        if count == 2:
            image[:, :400] = rgb_vals[0]
            image[:, 400:] = rgb_vals[0]
        if count == 3:
            image[:400, :] = rgb_vals[0]
            image[400:, :400] = rgb_vals[1]
            image[400:, 400:] = rgb_vals[2]
        if count == 4:
            image[:400, :400] = rgb_vals[0]  # left top
            image[400:, :400] = rgb_vals[1]  # left bottom
            image[:400, 400:] = rgb_vals[2]  # right top
            image[400:, 400:] = rgb_vals[3]  # right bottom
        image = cv2.resize(image, (200,200))
        cv2.imshow("colour palette", image)
        cv2.waitKey(1000)
        cv2.destroyAllWindows( )

        #def tuple_to_str(t):
        #st = str(t)
        #return st

        # show_palette(colorfinder( ), 3)

    while True:  #time.time() - start_time < 1:
        #while_count += 1
        #print(f'found {while_count} RGB value {colorfinder(SS_Getter( ))}')
        #time.sleep(3)
        show_palette(colorfinder(SS_Getter()),1)
        # Remove this
        # break
        # need to publish continues data to mqtt broker


if __name__ == '__main__':
    main( )
