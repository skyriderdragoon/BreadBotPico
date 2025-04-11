import network
import secrets as s
import time

def Setup():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print('Connecting to Home WiFi')
    wlan.connect(s.SSID, s.PASS)
        
    print(wlan.isconnected())
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
                break
        max_wait -= 1
        print('waiting for connection...')
        time.sleep(2)
    # Manage connection errors
    if wlan.status() != 3:
        print('Network Connection has failed')
    else:
        print('connected')
        status = wlan.ifconfig()
        print( 'ip = ' + status[0] )