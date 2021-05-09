# Museum player version 2.0

A simple media player that runs on a raspberry pi 4 board.
The script is in python and it works using the vlc library.

Python-vlc source package: https://pypi.org/project/python-vlc/

------

### Description

This Media Player uses vlc-python library to interact with vlc and to play a video. When executed the first video is played in loop mode, then when a button is pressed it switch to the one-shot video, which is played only one time. When the second video reaches the end it returns to the first one which is played in loop mode.
When connected to the power the raspberry automatically runs the program after the lxde enviroment is setup.

This player is intended to be used in a museum in order to exhibit videos show in loop mode, it was studied to work on a button base system designed to be pressed with a foot in relation to the pandemic necessities.

------

### Instructions for installing the player

**Important!**
Disable raspberry screensaver installing xscreensaver

**How to make it startup on boot:**

 - Create .desktop file to be run after Desktop is loaded

   mkdir /home/pi/.config/autostart
   nano /home/pi/.config/autostart/player.desktop

 - Code inside the player.desktop file that you have created:

   [Desktop Entry]
   Type=Application
   Name=Player
   Exec=/usr/bin/python /home/pi/player.py

------

### Script position for the player to run
Place python script in -> **/home/pi/player.py**

### How to remove the autostart
If you want to remove the autostart delete **player.desktop** file -> path /home/pi/.config/autostart

### Contributions and improvments
Every contribution or suggestion is well accepted, the program was already tested and some bugs have already been resolved.

