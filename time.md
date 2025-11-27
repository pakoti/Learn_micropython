Here are the different ways to get time in MicroPython on ESP8266:

## 1. Basic Time Functions (Always Available)

```python
import time

# Get ticks since boot (milliseconds)
print(f"Ticks since boot: {time.ticks_ms()} ms")

# Get ticks since boot (microseconds)
print(f"Ticks since boot: {time.ticks_us()} us")

# Simple delays
time.sleep(1)           # Sleep for 1 second
time.sleep_ms(500)      # Sleep for 500 milliseconds
time.sleep_us(1000)     # Sleep for 1000 microseconds
```

## 2. Real-Time Clock (RTC) - Limited

```python
import machine

# Create RTC object
rtc = machine.RTC()

# Set RTC time (manually)
# Format: (year, month, day, weekday, hour, minute, second, microsecond)
rtc.datetime((2024, 1, 15, 0, 14, 30, 0, 0))  # Jan 15, 2024, 2:30:00 PM

# Get current RTC time
current_time = rtc.datetime()
print(f"RTC Time: {current_time}")

# Unpack the tuple
year, month, day, weekday, hour, minute, second, microsecond = current_time
print(f"Date: {year}-{month:02d}-{day:02d}")
print(f"Time: {hour:02d}:{minute:02d}:{second:02d}")
```

## 3. Get Time from Internet (NTP) - Requires WiFi

```python
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
# connect_wifi('YourWiFiSSID', 'YourPassword')
# sync_time_from_ntp()
```

## 4. Simple Time Formatting Function

```python
import machine

def get_formatted_time():
    rtc = machine.RTC()
    t = rtc.datetime()
    
    # Format: "2024-01-15 14:30:25"
    return f"{t[0]}-{t[1]:02d}-{t[2]:02d} {t[4]:02d}:{t[5]:02d}:{t[6]:02d}"

def get_time_only():
    rtc = machine.RTC()
    t = rtc.datetime()
    
    # Format: "14:30:25"
    return f"{t[4]:02d}:{t[5]:02d}:{t[6]:02d}"

# Test
print(f"Full time: {get_formatted_time()}")
print(f"Time only: {get_time_only()}")
```

## 5. Create a Simple Clock

```python
import machine
import time

def simple_clock():
    rtc = machine.RTC()
    
    while True:
        t = rtc.datetime()
        print(f"{t[4]:02d}:{t[5]:02d}:{t[6]:02d}", end='\r')
        time.sleep(1)

# Run the clock (press Ctrl+C to stop)
# simple_clock()
```

## 6. Measure Execution Time

```python
import time

def measure_time():
    start = time.ticks_ms()
    
    # Code to measure
    time.sleep(2.5)
    
    end = time.ticks_ms()
    elapsed = time.ticks_diff(end, start)
    print(f"Execution time: {elapsed} ms")

measure_time()
```

## 7. Timezone Adjustment (Manual)

```python
import machine

def set_time_with_timezone(hour_offset=0):
    rtc = machine.RTC()
    current = rtc.datetime()
    
    # Adjust hour
    new_hour = (current[4] + hour_offset) % 24
    
    # Create new datetime tuple
    new_time = (current[0], current[1], current[2], current[3], 
                new_hour, current[5], current[6], current[7])
    
    rtc.datetime(new_time)
    print(f"Time adjusted by {hour_offset} hours")

# Example: Add 5 hours for timezone
# set_time_with_timezone(5)
```

## Quick Start - Just Want Current Time?

```python
import machine
rtc = machine.RTC()
t = rtc.datetime()
print(f"Time: {t[4]:02d}:{t[5]:02d}:{t[6]:02d}")
print(f"Date: {t[2]:02d}/{t[1]:02d}/{t[0]}")
```

## Important Notes:

- **Without WiFi**: Time resets on power cycle (starts from 2000 or last set time)
- **With WiFi**: Use NTP to get accurate internet time
- **RTC battery**: Most ESP8266 boards don't have RTC battery backup
- **Time drift**: Internal RTC may drift over time without periodic NTP sync

**Start with the basic RTC functions** if you don't have WiFi, or use NTP if you're connected to the internet!