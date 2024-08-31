
import time
import dxcam
import numpy
import cv2
from memory_profiler import profile
from colorthief import ColorThief


@profile
def main():
    def capture_ss():

        screen = dxcam.create(output_color="BGRA")
        frame = cv2.resize(src=screen.grab(), dsize=(320, 240))
        if frame is None: return
        cv2.imwrite("ss.jpg", frame)
        time.sleep(0.5)

    def colorfinder():

        ct = ColorThief("ss.jpg")
        print(ct.get_palette(color_count=4, quality=1))

    while True:
        capture_ss()
        colorfinder()
        break


if __name__ == '__main__':
    main( )
