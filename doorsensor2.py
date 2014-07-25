import time
import RPi.GPIO as io
io.setmode(io.BCM)

door_pin = 25


io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp

while True:
    if io.input(door_pin):
        print("Door Open")
    else:
        print("Door Closed")
    time.sleep(5)
