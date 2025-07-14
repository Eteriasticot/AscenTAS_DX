import pydirectinput as pdi
import pygetwindow as gw
import time
import os
from win32com.shell import shell, shellcon

inputCodes = {'u':'up', 'd':'down', 'r':'right', 'l':'left', 'j' : ' ', 'f' : 'x', 'e' : 'enter'}
inputStates = {'u':False, 'd':False, 'r':False, 'l':False}


FileName = 'inputs.txt' #default 'inputs.txt', change that to your txt file and make sure the file is in the same directory


def timeToSec(t:str) -> float:
    times:list = t.split(':')
    if len(times) == 2:
        time:float = float(times[0])*60 + float(times[1])
        return time
    elif len(times) == 1:
        time:float = float(times[0])
        return time
    else:
        return "temps invalide"
    
def openAscentDX():
    ascent_window = gw.getWindowsWithTitle("Ascent DX")[0]
    ascent_window.minimize()
    ascent_window.maximize()
    

def read_inputs(file:str)-> list:
    f = open(file, 'r')
    x = f.readline()
    lines = list()
    while x != '':
        lines.append(x)
        x = f.readline()
    inputs = list()
    for x in lines: 
        input = x.strip().split(' ')
        input[1] = timeToSec(input[1])
        inputs.append(input)
    return inputs

def timeToDiff_inputs(inputs:list):
    prevTime = 0
    for x in inputs:
        buffer = x[1]
        x[1] -= prevTime
        if x[1] < 0:
            x[1] = 0
        prevTime = buffer
    return inputs

def resetRun():
    pdi.press('down')
    pdi.press('enter')
    for _ in range(5):
        pdi.press('down')
    pdi.press('enter')
    pdi.press('down')
    pdi.press('enter')
    time.sleep(1)
    pdi.keyDown('enter')
    time.sleep(1)
    pdi.keyUp('enter')

def input_read(inp:str):
    if inp in ['u', 'd', 'r', 'l']:
        if inputStates[inp]:
            pdi.keyUp(inputCodes[inp])
        else:
            pdi.keyDown(inputCodes[inp])
        inputStates[inp] = not(inputStates[inp])
    else:
        pdi.keyDown(inputCodes[inp])
        pdi.keyUp(inputCodes[inp])

def playInputs(inputs:list):
    for inp, t in inputs:
        time.sleep(t)
        input_read(inp)


if __name__ == '__main__':
    openAscentDX()
    resetRun()
    
    inputs = read_inputs(FileName)
    inputs = timeToDiff_inputs(inputs)
    playInputs(inputs)