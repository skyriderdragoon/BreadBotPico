import modules.sensor as sensor
from modules.Data import Data
import time
import uasyncio

reading = 0
from typing import Optional

_Data: Optional[Data] = None  # Initialize _Data as a global variable

async def Get():
    global _Data, reading
    while True:
        distance = uasyncio.wait_for(sensor.get_distance(), 5)
        t_sta = time.ticks_ms()
        if _Data is None:
            _Data = Data(distance)
            print("Data object created")
        
        completed = await _Data.Check_Status(distance)
        if completed:
            print("Bread is done!")
            # Add code to handle when the bread is done
            return((_Data, True, 0))
        else:
            _Data.Add_Measurement(distance)
            reading += 1
            print("Measurement added")
            t_end= time.ticks_ms()
            elapsed = time.ticks_diff(t_end, t_sta)
            return((_Data, False, elapsed))
        
async def Task():
    returns = await Get()
    time = 30 - returns[2]
    await uasyncio.sleep(time)