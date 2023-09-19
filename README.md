# Fixing Galaga

My Galaga mini arcade cabinet stopped working, so I came up with a Rube Goldberg-esque way to fix it involving robots, Raspberry Pis, and Arduinos.

![](https://raw.githubusercontent.com/nickbild/fixing_galaga/main/media/teaser.jpg)

## How It Works

After gutting the arcade cabinet, I installed a new 320x240 LCD display of the same size as the original (so I wouldn't have to figure out how to interface with the original).  The display, along with the joystick and buttons, are wired to a Raspberry Pi 4 computer that fits inside the casing.  The Pi runs [fbcp-ili9341](https://github.com/juj/fbcp-ili9341) to use the LCD as its main display.  It also runs [arcade.py](https://github.com/nickbild/fixing_galaga/blob/main/arcade.py), which handles input from the joystick and buttons.

The arcade operates in two modes — "drive" and "game", which are toggled by the "Start" button.  In drive mode, the script sends HTTP requests to a laptop ([api.py](https://github.com/nickbild/fixing_galaga/blob/main/api.py)) that issues ROS2 commands over WiFi that control the movements of the robot.  In game mode, HTTP requests are sent to an Arduino Nano 33 IoT attched to a Raspberry Pi 3, running RetroPie and emulating Galaga, that acts as a keyboard emulator.  This allows remote keystrokes to be sent to control the action in the game.

The robot is outfitted with an Espressif ESP-EYE camera board, and runs the excellent [ESP32 MJPEG Streaming Server](https://github.com/arkhipenko/esp32-cam-mjpeg) that is super-fast, allowing for sub-second video streaming delays that make the driving and gaming experiences great.  I tried several other video streaming solutions first that were unacceptable, due to having 1 second plus delays.  The video feed is streamed to the Raspberry Pi 4 in the arcade cabinet using VLC.

To use the system, the arcade is put in drive mode, and the robot is driven in front of a TV that is hooked up the the Galaga emulator.  Video of Galaga is now being streamed to the arcade cabinet's display, so the device is switched into game mode.  Now, the arcade controls can be used to control the Galaga emulator.

## Media

## Bill of Materials

- 1 x Mini arcade cabinet
- 1 x 320x240 LCD display
- 1 x Raspberry Pi 4
- 1 x Raspberry Pi 3
- 1 x Arduino Nano 33 IoT
- 1 x iRobot Create 3
- 1 x Espressif ESP-EYE

## About the Author

[Nick A. Bild, MS](https://nickbild79.firebaseapp.com/#!/)
