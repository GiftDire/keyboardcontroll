from djitellopy import tello
import keyboardcontrol as kc

''' imported the main module'''
from time import sleep

kc.init()
me = tello.Tello()
me.connect()
# '''printing out the battery for monitoring the power the battery has'''
print(me.get_battery())


def geykeyboardinput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    # '''negative speed and postive speed'''
    #negative=left and right=postive same applies to foward and backwards#

    if kc.getkey("Left"):
        lr = -speed
    elif kc.getkey("Right"):
        lr = speed

    if kc.getkey("UP"):
        fb = speed
    elif kc.getkey("Down"):
        fb = -speed

    if kc.getkey("W"):
        ud = speed
    elif kc.getkey("S"):
        ud = -speed

    if kc.getkey("a"):
        yv = speed
    elif kc.getkey("d"):
        yv = -speed

    return [lr, fb, ud, yv]


if kc.getkey("q"): ll = me.land()
if kc.getkey("e"): ll = me.takeoff()





me.takeoff()


while True:
    vals = getkeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)
    #added a sleep for stability

    print(kc.getkey("s"))
#This code appears to be controlling a Tello drone using the "tello" library. The code connects to the drone and prints out the battery level.
# There is a function defined called "getkeyboardinput()" which appears to be getting input from the keyboard to control the drone's movement.
# The input keys are Left, Right, Up, Down, W, S, a, and d, which control the left-right, forward-backward, up-down and yaw/rotation movement of the drone respectively.
# The code also checks for the "q" and "e" keys, which appear to be used to land and take off the drone respectively. The while loop
# continuously gets the keyboard input and sends the corresponding rc control commands to the drone with a sleep of 0.05 seconds for stability. The code also prints out the value of "s" key.#

