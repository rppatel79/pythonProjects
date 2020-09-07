import curses
import RPi.GPIO as GPIO

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

GPIO.setup(32,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)

GPIO.output(7,False)
GPIO.output(11,False)
GPIO.output(13,False)
GPIO.output(15,False)

GPIO.output(32,False)
GPIO.output(36,False)
GPIO.output(38,False)
GPIO.output(40,False)


#Get the curses window, turn off echoing of keyboard to script,
#turn on instance (no waiting) key response, and use special values for
#cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
	while True:
		char = screen.getch()
		if char == ord('q'):
			GPIO.output(7,True)
			GPIO.output(11,True)
			GPIO.output(13,True)
			GPIO.output(15,True)

			GPIO.output(32,True)
			GPIO.output(36,True)
			GPIO.output(38,True)
			GPIO.output(40,True)

			break
		elif char == curses.KEY_DOWN:
			print ("down")
			GPIO.output(7,False)
			GPIO.output(11,True)
			GPIO.output(13,False)
			GPIO.output(15,True)

			GPIO.output(32,False)
			GPIO.output(36,True)
			GPIO.output(38,False)
			GPIO.output(40,True)

		elif char == curses.KEY_UP:
			print ("up")
			GPIO.output(7,True)
			GPIO.output(11,False)
			GPIO.output(13,True)
			GPIO.output(15,False)

			GPIO.output(32,True)
			GPIO.output(36,False)
			GPIO.output(38,True)
			GPIO.output(40,False)
		elif char == curses.KEY_RIGHT:
			print ("right")
			GPIO.output(7,False)
			GPIO.output(11,True)
			GPIO.output(13,True)
			GPIO.output(15,False)

			GPIO.output(32,False)
			GPIO.output(36,True)
			GPIO.output(38,True)
			GPIO.output(40,False)
		elif char == curses.KEY_LEFT:
			print ("left")
			GPIO.output(7,True)
			GPIO.output(11,False)
			GPIO.output(13,False)
			GPIO.output(15,True)

			GPIO.output(32,True)
			GPIO.output(36,False)
			GPIO.output(38,False)
			GPIO.output(40,True)

		elif char == 10:
			print ("stop")
			GPIO.output(7,False)
			GPIO.output(11,False)
			GPIO.output(13,False)
			GPIO.output(15,False)

			GPIO.output(32,False)
			GPIO.output(36,False)
			GPIO.output(38,False)
			GPIO.output(40,False)

finally:
	curses.nocbreak(); screen.keypad(0); curses.echo()
	curses.endwin()
	GPIO.cleanup()
