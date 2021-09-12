import requests
import time
import os
import configparser
import logging
import sys
from sense_hat import SenseHat

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

WUurl ="https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?"

sense = SenseHat()
sense.clear()

config_file = 'config.txt'

def read_config(property):
	config = configparser.ConfigParser()
	config.read_file(open(config_file))
	return config.get('wunderground',property)

def c_to_f(input_temp):
	# convert input_temp from Celsius to Fahrenheit
	return (input_temp * 1.8) + 32

def get_cpu_temp():
	# 'borrowed' from https://www.raspberrypi.org/forums/viewtopic.php?f=104&t=111457
	# executes a command at the OS to pull in the CPU temperature
	res = os.popen('vcgencmd measure_temp').readline()
	return float(res.replace("temp=", "").replace("'C\n", ""))


# use moving average to smooth readings
def get_smooth(x):
	# do we have the t object?
	if not hasattr(get_smooth, 't'):
		# then create it
		get_smooth.t = [x, x, x]
	# manage the rolling previous values
	get_smooth.t[2] = get_smooth.t[1]
	get_smooth.t[1] = get_smooth.t[0]
	get_smooth.t[0] = x
	# average the three last temperatures
	xs = (get_smooth.t[0] + get_smooth.t[1] + get_smooth.t[2]) / 3
	return xs


def get_temp():
	# ====================================================================
	# Unfortunately, getting an accurate temperature reading from the
	# Sense HAT is improbable, see here:
	# https://www.raspberrypi.org/forums/viewtopic.php?f=104&t=111457
	# so we'll have to do some approximation of the actual temp
	# taking CPU temp into account. The Pi foundation recommended
	# using the following:
	# http://yaab-arduino.blogspot.co.uk/2016/08/accurate-temperature-reading-sensehat.html
	# ====================================================================
	# First, get temp readings from both sensors
	t1 = sense.get_temperature_from_humidity()
	t2 = sense.get_temperature_from_pressure()
	# t becomes the average of the temperatures from both sensors
	t = (t1 + t2) / 2
	#print("t1="+str(t1)+"t2="+str(t2))
	# Now, grab the CPU temperature
	t_cpu = get_cpu_temp()
	#print("CPU T="+str(t_cpu))
	# Calculate the 'real' temperature compensating for CPU heating
	t_corr = t - ((t_cpu - t) / 1.5)
	# Finally, average out that value across the last three readings
	t_corr = get_smooth(t_corr)
	# convoluted, right?
	# Return the calculated temperature
	return t_corr

#def get_temp():
#	sense.clear()
#	return sense.get_temperature()

def get_pressure():
	sense.clear()
	return sense.get_pressure()

def get_humidity():
	sense.clear()
	return sense.get_humidity()

def push_results(temperaturef,pressure,humidity):
	WU_station_id =read_config('WU_station_id')
	WU_station_pwd =read_config('WU_station_pwd')
	WUcreds = "ID="+ WU_station_id + "&PASSWORD="+ WU_station_pwd
	date_str = "&dateutc=now"
	action_str = "&action=updateraw"

	humidity_str = "{0:.2f}".format(humidity)
	pressure_str = "{0:.2f}".format(hpa_to_inches(pressure))
	tempf_str = "{0:.2f}".format(temperaturef)

	query_str="&humidity="+humidity_str+"&tempf="+tempf_str+"&baromin"+pressure_str+action_str
	logging.debug("Uploading query str["+query_str+"]")

	upload_to_wunderground = True
	
	if upload_to_wunderground:
		r = requests.get(
			WUurl +
			WUcreds +
			date_str +
			query_str)
		logging.info("Received " +str(r.status_code)+" "+str(r.text))

def hpa_to_inches(pressure_in_hpa):
	pressure_in_inches_of_m = pressure_in_hpa * 0.02953
	return pressure_in_inches_of_m

def kmh_to_mph(speed_in_kmh):
	speed_in_mph= speed_in_kmh * 0.621371
	return speed_in_mph

if __name__ == "__main__":
	while True:
		sleep_time_min = int(read_config('Sleep_Time_Min'))
		logging.info ("About to sleep for ["+str(sleep_time_min)+"]")
		time.sleep(sleep_time_min*60)
		logging.info(c_to_f(get_temp()),get_pressure(),get_humidity())
