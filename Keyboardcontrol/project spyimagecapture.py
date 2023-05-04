import time

from djitellopy import tello
import keyboardcontrol as kc
from time import sleep
import cv2

''' imported the main module'''
from time import sleep

kc.init()
me = tello.Tello()
me.connect()
# '''printing ou the battery for monitoring the power the battery has'''
print(me.get_battery())

global img



def geykeyboardinput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kc.getkey("Left"):
        lr = speed
    elif kc.getkey("Right"):
        lr = -speed

    if kc.getkey("UP"):
        fb = speed
    elif kc.getkey("Down"):
        fb = -speed

    if kc.getkey("UP"):
        ud = -speed
    elif kc.getkey("s"):
        ud = speed

    if kc.getkey("a"):
        yv = speed
    elif kc.getkey("d"):
        yv =-speed

    return [lr, fb, ud, yv]



if kc.getkey("q"): yv = me.land();time.sleep(4)
if kc.getkey("e"): yv = me.takeoff()

if kc.getkey('c'):
    cv2.imwrite(f'Resources/images/{time.time()}.jpg')
    time.sleep(0.3)
    #this where the image get saved#





me.takeoff()


while True:
    vals = geykeyboardinput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    """ size of an image"""
    cv2.imshow("image", img)

    cv2.waitkey(1)
    """Delaying """


    print(kc.getkey("s"))

    #key bc was merged with image capture#

    #This script is used to control a Tello drone using keyboard controls and
    # display the drone's video stream. The script uses the djitellopy and
    # keyboardcontrol libraries to connect to the drone and control its movement,
    # and the cv2 library to display the video stream.
    # The script first initializes the keyboardcontrol library and connects to the drone.
    # Then it prints the battery level of the drone.

