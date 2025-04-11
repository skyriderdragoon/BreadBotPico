import uasyncio as asyncio
import pimoroni_i2c
import breakout_vl53l5cx

PINS_TOF= {"sda": 20, "scl": 21}
i2c = pimoroni_i2c.PimoroniI2C(**PINS_TOF, baudrate=2_000_000)
sensor = breakout_vl53l5cx.VL53L5CX(i2c)
max_retries = 10

def Setup():
    global sensor
    # Make sure to set resolution and other settings *before* you start ranging
    sensor.set_resolution(breakout_vl53l5cx.RESOLUTION_4X4)
    print("Sensor ready, call start_ranging() to start ranging")

async def get_distance():
    # Start ranging, this will block until the first frame is ready
    sensor.start_ranging()
    print("Ranging started")
    # Get the distance data from the sensor
    retries=0
    while data is None and retries < max_retries:
        if sensor.data_ready():
            data = sensor.get_data()
            # Stop ranging, this will block until the sensor has stopped ranging
            sensor.stop_ranging()
            return data.distance_avg
        else:
            print("Data unavailable, waiting for next frame \r\n Retries: ", retries)
            # Wait for the next frame
            await asyncio.sleep(0.1)
            data = sensor.get_data()
            retries += 1