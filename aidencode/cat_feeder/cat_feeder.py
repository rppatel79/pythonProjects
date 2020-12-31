# Imports
import RPi.GPIO as GPIO
import time
import sys

wait_time = 1
if len(sys.argv) == 2:
	wait_time = float(sys.argv[1])

print("Wait Time is:",wait_time)

# set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(11, GPIO.OUT)
servo1 = GPIO.PWM(11, 50) # note 11 is pin, 50= 50 Hz pulse

try:
        #start PWM running, but with value of 0 (publse off)
        servo1.start(0)
        time.sleep(2)

        # rotate the servo 90 deg and than back
        servo1.ChangeDutyCycle(7.5) # neutral position
        time.sleep(1)
        servo1.ChangeDutyCycle(12.5) # right +90 deg position
        time.sleep(wait_time)
        servo1.ChangeDutyCycle(7.5) # neutral position
        time.sleep(1)
finally:
        servo1.stop()
        GPIO.cleanup()

print("Goodbye")
