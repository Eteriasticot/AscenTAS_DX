First, you need to install python and the right libraries.

1. Installing python
You can just go to https://www.python.org and download the last version.

2. Installing the libraries
You can simply open a terminal if you're on windows or linux and type 'pip install pywin32', 'pip install pygetwindow', 'pip install pyautogui' and 'pip install pydirectinput'.

3. Making your TAS
You can now write down the inputs you want to be played in the inputs.txt file. 'u' corresponds to 'arrow up', 'd' to 'arrow down', 'l' to 'arrow left', 'r' to 'arrow right', 'j' corresponds to jump or dive, 'f' corresponds to dash and 'e' to 'enter'.
Keep one input per line in this format : 'u 00:13.378'. It should work with only the seconds but the final render would be ugly. If your run exceeds an hour, just keep iterating the minute to keep the 'xx:xx.xxx' format. The decimals are purely optional.
Each input except jump, dash and enter will be flipped with each line. So assuming you have no inputs pressed, 'r xx:xx.xxx' will turn the right input on, calling the 'r' input again will turn it off.

4. Running your TAS
Once your txt file is finished, simply save it, launch your game, stay in the menu, on the start or continue button, then launch the python file. It will reopen your game automatically and reset your save automatically too.

Have fun making your own TAS