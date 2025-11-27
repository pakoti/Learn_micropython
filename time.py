import network
import ntptime
import machine
import time

def connect_wifi(ssid, password):
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    if not sta.isconnected():
        print('Connecting to WiFi...')
        sta.connect(ssid, password)
        while not sta.isconnected():
            time.sleep(0.5)
    print('WiFi connected!')
    print('IP address:', sta.ifconfig()[0])

def sync_time_from_ntp():
    try:
        print("Syncing time from NTP server...")
        ntptime.settime()  # Sync with NTP server
        print("Time synchronized successfully!")
        
        # Get the synchronized time
        rtc = machine.RTC()
        current_time = rtc.datetime()
        print(f"Current time: {current_time[0]}-{current_time[1]:02d}-{current_time[2]:02d} {current_time[4]:02d}:{current_time[5]:02d}:{current_time[6]:02d}")
        
        return current_time
    except Exception as e:
        print(f"Failed to sync time: {e}")
        return None

# Usage (replace with your WiFi credentials):

# uncomment this section to work
# connect_wifi('YourWiFiSSID', 'YourPassword')
# sync_time_from_ntp()