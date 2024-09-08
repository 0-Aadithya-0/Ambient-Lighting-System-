import sys
import time
import paho.mqtt.client as mqtt
import dxcam
import numpy as np
import cv2
from Tools.scripts.generate_global_objects import Printer
from memory_profiler import profile
from colorthief import ColorThief
Host = "127.0.0.1"


@profile
def main():

    def SS_Getter():

        screen = dxcam.create(output_color="BGRA")#BGRA is the output format that consumes the least memory
        frame = cv2.resize(src=screen.grab(), dsize=(320, 240))#320p
        #frame = cv2.pyrDown() #downsample 2x
        if frame is None: return #dxcam returns non if no news frames are available
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGBA)
        cv2.imwrite("ss.jpg", frame)

    def RGB_Publisher():
        def colorfinder():
            ct = ColorThief("ss.jpg")  # gets half the job done
            color = ct.get_palette(color_count=4, quality=1)
            return color
        
        def show_palette(rgb_vals,count):#(optional)-> fucn to show the colour palette
            #Cerate a blank image of size 800x800 with 3 color
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

        def tuple_to_str(t):
            st = str(t)
            return st

        def mqtt_handler():
            client = mqtt.Client("RGB_val")
            while client.connect(Host):
                print("----------Trying to connect to broker-----------")
            client.loop_start()
            client.publish("lights/RGB_val","HEY NIGESH",qos= 1 )



            #print(f"----------printed value:{payload}-----------")


        #show_palette(colorfinder( ), 4)
        mqtt_handler()
        #print(colorfinder())



    
    
    
    while True:
        #SS_Getter()
        RGB_Publisher()
        # Remove this break
        #need to publish continues data to mqtt broker




if __name__ == '__main__':

    main( )
