import os
import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

host_drive = "192.168.1.140:5000"
host_game = "192.168.1.164"

start = 26
down = 19
up = 13
right = 6
left = 5
fire = 0

hold_start = False
hold_down = False
hold_up = False
hold_right = False
hold_left = False
hold_fire = False

drive_mode = True


GPIO.setup(start, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(down, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(up, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(right, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(left, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(fire, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while True:
    # Toggle drive mode.
    if GPIO.input(start):
        if drive_mode:
            drive_mode = False
        else:
            drive_mode = True
        
        time.sleep(1) # Debounce

    # Set host for mode.
    if drive_mode:
        host = host_drive
    else:
        host = host_game

    # Button presses.
    if GPIO.input(up) and hold_up == False:
        hold_up = True
        os.system("curl http://{0}/up".format(host))
    
    elif GPIO.input(down) and hold_down == False:
        hold_down = True
        os.system("curl http://{0}/down".format(host))
    
    elif GPIO.input(left) and hold_left == False:
        hold_left = True
        os.system("curl http://{0}/left".format(host))
    
    elif GPIO.input(right) and hold_right == False:
        hold_right = True
        os.system("curl http://{0}/right".format(host))

    elif GPIO.input(fire) and hold_fire == False:
        hold_fire = True
        os.system("curl http://{0}/fire".format(host))

    elif GPIO.input(start) and hold_start == False:
        hold_start = True
        os.system("curl http://{0}/start".format(host))

    
    # Button releases.
    if GPIO.input(up) == False and hold_up:
        hold_up = False
        os.system("curl http://{0}/up_release".format(host))

    elif GPIO.input(down) == False and hold_down:
        hold_down = False
        os.system("curl http://{0}/down_release".format(host))
    
    elif GPIO.input(left) == False and hold_left:
        hold_left = False
        os.system("curl http://{0}/left_release".format(host))

    elif GPIO.input(right) == False and hold_right:
        hold_right = False
        os.system("curl http://{0}/right_release".format(host))

    elif GPIO.input(fire) == False and hold_fire:
        hold_fire = False
        os.system("curl http://{0}/fire_release".format(host))

    elif GPIO.input(start) == False and hold_start:
        hold_start = False
        os.system("curl http://{0}/start_release".format(host))
