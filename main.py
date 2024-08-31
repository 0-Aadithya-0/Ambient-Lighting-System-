import dxcam
import numpy
import cv2
from memory_profiler import profile


@profile
def capture_ss():
    while True:
        screen = dxcam.create(output_color="BGR")
        frame = cv2.resize(src=screen.grab(), dsize=(320, 240))
        if frame is None: continue
        break





capture_ss()
