from machine import Pin, PWM
import uasyncio
import bread
from modules import wifi, sensor

led1 = Pin(15, Pin.OUT)
led2 = Pin(14, Pin.OUT)
buzzer = PWM(13)
button = Pin(16, Pin.IN)

_data= None
print("BreadBot  Copyright (C) 2025  Daniel Robertson")
wifi.Setup()
sensor.Setup()
print("Setup complete")
print("Starting main loop")
print("Waiting for button press...")
led1.on()

event_loop = uasyncio.get_event_loop()
event_loop.create_task(bread.Task())
try:
    event_loop.run_until_complete(event_loop)
except KeyboardInterrupt:
    print("Keyboard interrupt received, stopping event loop")
    event_loop.stop()
    led1.off()
finally:
    event_loop.close()
    print("Event loop closed")
    led1.off()
    led1.off()
    led2.off()
    buzzer.deinit()
    print("Cleanup complete")