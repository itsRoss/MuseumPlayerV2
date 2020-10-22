# Museum player version 2.0

Media player based on raspberry pi 4 board and programmed in python using python-vlc library.

Python-vlc source package: https://pypi.org/project/python-vlc/

------

### Description

This Media Player uses vlc-python library to interact with vlc and to play a video. When executed the first video is played in loop mode, then when a button is pressed it switch to the one-shot video, which is played only one time. When the second video reaches the end it return to the first one which is played in loop mode.
When connected to the power the raspberry automatically runs the program after the lxde enviroment is setup.

------

### Instructions for creating the player

**Important!**
Disable screensaver installing xscreensaver

**Autostart process:**

 - Create .desktop file to be run after Desktop is loaded

   mkdir /home/pi/.config/autostart
   nano /home/pi/.config/autostart/player.desktop

 - Code inside player.desktop:

   [Desktop Entry]
   Type=Application
   Name=Player
   Exec=/usr/bin/python /home/pi/player.py


**Script position for autostart to run**
Place python script in -> **/home/pi/player.py**

**Remove autostart**
If you want to remove autostart delete **player.desktop** file -> path /home/pi/.config/autostart
