from time import perf_counter, sleep
import pydirectinput as pdi

import threading
def right_d():
    pdi.keyDown('right')

print(perf_counter())
threading.Thread(target=right).start()
print(perf_counter())