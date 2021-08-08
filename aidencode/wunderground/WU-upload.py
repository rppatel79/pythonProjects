import requests
import configparser
from sense_hat import SenseHat

WUurl ="https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?"

sense = SenseHat()
sense.clear()

config_file = 'config.txt'

def read_config(property):
	config = configparser.ConfigParser()
	config.read_file(open(config_file))
	return config.get('wunderground',property)

def get_temp():
	sense.clear()
	return sense.get_temperature()

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

	r = requests.get(
		WUurl +
		WUcreds +
		date_str +
		"&humidity="+humidity_str+
		"&tempf="+tempf_str+
		"&baromin"+pressure_str+
		action_str)
	print("Received " +str(r.status_code)+" "+str(r.text))

def hpa_to_inches(pressure_in_hpa):
	pressure_in_inches_of_m = pressure_in_hpa * 0.02953
	return pressure_in_inches_of_m

def kmh_to_mph(speed_in_kmh):
	speed_in_mph= speed_in_kmh * 0.621371
	return speed_in_mph

if __name__ == "__main__":
	push_results(get_pressure(),get_pressure(),get_humidity())
