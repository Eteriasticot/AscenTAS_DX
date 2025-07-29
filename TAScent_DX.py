import pydirectinput as pdi
import pygetwindow as gw
import time
import threading
import customtkinter as ct
import json
from os import getcwd


### Hard coded settings
inputCodes = {'u':'up', 'd':'down', 'r':'right', 'l':'left', 'j' : ' ', 'f' : 'x', 'e' : 'enter'}
inputStates = {'u':False, 'd':False, 'r':False, 'l':False}
full_map = {"43":1,"108":1,"47":2,"30":2,"37":1,"85":1,"61":1,"33":1,"68":2,"42":1,"91":2,"62":1,"94":1,"12":1,"-3":1,"40":1,"53":1,"107":1,"22":2,"89":1,"46":1,"67":1,"35":3,"110":1,"9":1,"66":1,"19":1,"16":1,"84":1,"32":1,"14":1,"93":1,"6":1,"13":1,"78":3,"106":1,"41":1,"118":1,"44":1,"63":1,"87":1,"49":1,"11":1,"86":1,"112":1,"111":1,"102":3,"23":1,"50":2,"65":1,"45":1,"38":1,"1":1,"39":1,"3":2,"4":1,"5":1,"60":1,"7":1,"8":1,"70":1,"92":1,"18":2,"2":1,"0":1,"24":1,"117":1,"57":1,"15":1,"-8":1,"31":1,"29":1,"58":1,"73":1,"139":1,"-4":1,"17":1,"27":2,"34":2,"54":1,"116":1,"20":1,"88":1,"-7":1,"48":2,"69":1,"71":1,"25":1,"10":1,"104":2,"59":2,"28":1,"103":1,"90":1,"51":1,"64":1,"26":1,"100":3,"101":3,"105":2,"74":3,"75":3,"95":3,"114":1,"79":3,"83":1,"72":1,"52":1,"21":1,"119":1,"109":1,"55":2,"115":1},
connection_dic = {"43":12,"112":10,"47":2,"30":11,"54":3,"85":3,"55":2,"24":15,"68":4,"42":8,"91":9,"62":9,"94":2,"12":3,"40":12,"107":1,"89":5,"67":1,"25":3,"110":2,"66":1,"84":8,"32":2,"14":3,"41":12,"118":2,"20":4,"63":9,"87":2,"45":2,"86":7,"111":3,"37":5,"23":11,"50":1,"65":1,"49":10,"33":3,"1":2,"39":10,"3":3,"19":2,"5":1,"93":2,"7":1,"8":1,"70":2,"92":6,"18":2,"108":1,"0":4,"16":3,"69":8,"46":3,"15":3,"22":3,"31":6,"57":9,"59":2,"117":2,"58":3,"60":1,"2":2,"27":3,"34":2,"4":3,"116":2,"9":1,"13":7,"44":2,"11":3,"88":2,"71":3,"73":8,"64":3,"17":6,"103":9,"28":3,"29":3,"104":2,"51":11,"48":1,"26":3,"38":3,"6":1,"105":1,"10":5,"90":1,"119":2,"114":8,"106":3,"83":5,"72":10,"52":3,"21":4,"61":1,"109":10,"53":7,"115":2},

### GUI part

app = ct.CTk()
app.geometry("700x450")
app.title("TAScent")
app.grid_columnconfigure((0,1,2,3), weight=1)

### Settings
FileName = 'inputs.txt' #default 'inputs.txt', change that to your txt file and make sure the file is in the same directory
mantle = ct.BooleanVar(value=False)
dive = ct.BooleanVar(value=False)
vines = ct.BooleanVar(value = False)
diamond = ct.BooleanVar(value = False)
dash = ct.BooleanVar(value = False)
spawn = ct.BooleanVar(value = False)
QuitRunAtStart = ct.BooleanVar(value = False)

path = getcwd()
save_f_path = path + '/settings.json'
j_save= json.loads(open('default.json', 'r').read())

### Functions

def get_power(power:str, state:bool):
    global j_save
    if j_save["progress"]["upgrades"] == []:
        j_save["progress"]["upgrades"] = {power:state}
    else:
        j_save["progress"]["upgrades"][power] = state

def spawn_change(x:int, y:int):
    global j_save
    if x=='':
        x = 595
    if y=='':
        y = 93
    j_save["progress"]["spawn"] = {"x":int(x), "y": int(y)}
    
def reset_save():
    global j_save
    j_save = json.loads(open(getcwd()+'/default.json').read())

def load_save():
    global j_save, save_f_path
    try:
        f = open(save_f_path, 'w')
    except:
        print('ça ouvre pas enculé')
    json.dump(j_save, f, ensure_ascii=False)
    f.close()

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
    global quitRunAtStart
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
        input[0] = input[0].lower()
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

def quitRun():
    pdi.press('esc')
    pdi.press('down')
    pdi.press('down')
    pdi.press('enter')

def input_read(inp:str):
    if inp in ['u', 'd', 'r', 'l']:
        if inputStates[inp]:
            pdi.keyUp(inputCodes[inp])
        else:
            pdi.keyDown(inputCodes[inp])
        inputStates[inp] = not(inputStates[inp])
    else:
        pdi.press(inputCodes[inp])

def playInputs(inputs:list):
    for inp, t in inputs:
        time.sleep(t)
        threading.Thread(target=input_read, args=[inp]).start()

def play_run():
    global inputStates, j_save, powers
    inputStates = {'u':False, 'd':False, 'r':False, 'l':False}
    
    inputs = read_inputs(FileName)
    inputs = timeToDiff_inputs(inputs)
    
    openAscentDX()
    reset_save()
    
    for x in powers:
        print(x, ':', powers[x].get())
        get_power(x, powers[x].get())
    
    edited_save = mantle_checkbox.get() or dive_checkbox.get() or vines_checkbox.get() or diamond_checkbox.get() or dash_checkbox.get() or spawn_toggle.get()
    if edited_save:
        j_save["progress"]["first_wakeup"] = True
        j_save["progress"]['map'] = full_map
        j_save["progress"]['connections'] = connection_dic
        j_save['starts'] = 4
        j_save["progress"]['time']=10
    
    if spawn_toggle.get():
        spawn_change(x_entry.get(), y_entry.get())
            
    if quit_run_toggle.get():
        quitRun()
    time.sleep(1)
    
    # pdi.press('enter')
    # time.sleep(1)
    # quitRun()
    
    load_save()
    time.sleep(1)
    
    playInputs(inputs)
    print("fini")


### SAVE DIRECTORY SETUP

dir_label = ct.CTkLabel(app, text='Game save directory', justify='left', anchor='w', font=('CtkDefaultFont', 20))

dir_textbox = ct.CTkTextbox(app, height=28)
dir_textbox.insert('0.0', path)

def change_path():
    global path, save_f_path
    path =  ct.filedialog.askdirectory()
    save_f_path = path + '/settings.json'
    save_f_path = save_f_path.replace('/', '\\')
    dir_textbox.delete("0.0", "end")
    dir_textbox.insert('0.0', path)

dir_button = ct.CTkButton(app, text='browse', command=change_path)


### GET POWERUPS FROM START

checkbox_label = ct.CTkLabel(app, text='Get powers at the start', justify='left', anchor='w', font=('CtkDefaultFont', 20))


mantle_checkbox = ct.CTkCheckBox(app, text='Wall climb ', onvalue=True, offvalue=False)


dive_checkbox = ct.CTkCheckBox(app, text='Dive ', onvalue=True, offvalue=False)


vines_checkbox = ct.CTkCheckBox(app, text='Vines', onvalue=True, offvalue=False)


diamond_checkbox = ct.CTkCheckBox(app, text='Diamond hand', onvalue = True, offvalue = False)

dash_checkbox = ct.CTkCheckBox(app, text='Dash', onvalue = True, offvalue = False)

powers = {'grab':mantle_checkbox, 'dive':dive_checkbox, 'vines':vines_checkbox, 'scale':diamond_checkbox, 'dash':dash_checkbox}

### SET UP A CUSTOM SPAWN POINT

spawn_label = ct.CTkLabel(app, text='Set custom spawn point', justify='left', anchor='w', font=('CtkDefaultFont', 20))

spawn_toggle = ct.CTkCheckBox(app, text='Enable custom spawn point (default to first lamp if enabled)', variable = spawn, onvalue = True, offvalue = False)

x_label = ct.CTkLabel(app, text='X :', justify='left', anchor='w')
x_entry = ct.CTkEntry(app, placeholder_text='588')

y_label = ct.CTkLabel(app, text='Y :', justify='left', anchor='w')
y_entry = ct.CTkEntry(app, placeholder_text='93')


### Run settings and start run

run_label = ct.CTkLabel(app, text='Start run', justify='left', anchor='w', font=('CtkDefaultFont', 20))

quit_run_toggle = ct.CTkCheckBox(app, text='Quit previous run', variable=QuitRunAtStart, onvalue=True, offvalue=False)

start_button = ct.CTkButton(app, text='Start', command=play_run)

### PACKING ALL WIDGETS

dir_label.grid(row=0, column=0, columnspan=2, sticky='ew', padx=20, pady=0)
dir_textbox.grid(row=1, column=0, columnspan=3, sticky='ew', padx=20, pady=15)
dir_button.grid(row=1, column=3, columnspan=1, sticky='ew', padx=20, pady=15)

checkbox_label.grid(row=3, column=0, columnspan=2, sticky='ew', padx=20, pady=0)
mantle_checkbox.grid(row=4, column=0, columnspan=2, sticky='ew', padx=20, pady=5)
dive_checkbox.grid(row=4, column=2, columnspan=2, sticky='ew', padx=20, pady=5)
vines_checkbox.grid(row=5, column=0, columnspan=2, sticky='ew', padx=20, pady=5)
diamond_checkbox.grid(row=5, column=2, columnspan=2, sticky='ew', padx=20, pady=5)
dash_checkbox.grid(row=6, column=0, columnspan=2, sticky='ew', padx=20, pady=5)

spawn_label.grid(row=7, column=0, columnspan=2, sticky='ew', padx=20, pady=10)
spawn_toggle.grid(row=8, column=0, columnspan=2, sticky='ew', padx=20, pady=5)
x_label.grid(row=9, column=0, columnspan=1, sticky='w', padx=20, pady=5)
x_entry.grid(row=9, column=0, columnspan=1, padx=20, pady=5)
y_label.grid(row=9, column=1, columnspan=1, sticky='w', padx=20, pady=5)
y_entry.grid(row=9, column=1, columnspan=1, padx=20, pady=5)

run_label.grid(row=10, column=0, columnspan=2, sticky='ew', padx=20, pady=10)
quit_run_toggle.grid(row=11, column=0, columnspan=2, sticky='ew', padx=20, pady=5)
start_button.grid(row=11, column=3, columnspan=1, sticky='ew', padx=20, pady=5)

if __name__=="__main__":
    app.mainloop()