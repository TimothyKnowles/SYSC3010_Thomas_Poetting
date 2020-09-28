from sense_hat import SenseHat
import sense_hat
import time

s = SenseHat()

# This is an example of reading the humidity and temperature sensors in tandem to give a feedback on
# on the weather's danger level of fire
while True:
    temp = s.get_temperature()
    hum = s.get_humidity()
    if (temp >= 90) and (hum >= 40):  # using line 6 of heat index as example
        print("POSSIBLE FIRE: \n  Temperature: %i C " % temp)
        print("  Humidity: %i %%\n" % hum)
    else:
        print("Weather is safe\n")
    time.sleep(0.9)
