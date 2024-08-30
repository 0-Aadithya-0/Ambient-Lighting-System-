import dxcam
import numpy
import cv2
from memory_profiler import profile


@profile
def capture_ss():
    while True:
        screen = dxcam.create(output_color="BGR")
        frame = screen.grab()

        if frame is None:
            continue
        frame = cv2.resize(src=frame, dsize=(640, 360))

        print(frame.shape)
        cv2.imshow("screen", frame)
        cv2.waitKey(0)
        break


capture_ss()
