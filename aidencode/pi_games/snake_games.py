from sense_emu import SenseHat
from sense_hat import SenseHat
from random import randint
import time
import print_sensehat_number

sense = SenseHat()

direction = "right"

blank = (0,0,0)
snake_color = (255,0,255)
fruit_color = (255,100,0)


def make_fruit(position,fruit_position,color):

	fruit_position[0] = randint(0,7)
	fruit_position[1] = randint(0,7)
	while fruit_position in position:
		fruit_position[0] = randint(0,7)
		fruit_position[1] = randint(0,7)
	print('Made fruit at:'+str(fruit_position))
	sense.set_pixel(fruit_position[0],fruit_position[1],fruit_color)


def draw_snake(position,color):
	for cell in position:
		sense.set_pixel(cell[0],cell[1],color)

def joystick_start_game(event):
	global has_click_middle_button

	has_click_middle_button = True
	print('You clicked in the middle')

def joystick_moved(event):
	global direction

	direction = event.direction
	print(direction)
	move_snake(snake_position,fruit_position,direction)

def move_snake(position,fruit_position,direction):
	global score

	if direction == "right":
		print("right")
		# remove the last element
		lastPosition = position.pop(len(position)-1)
		# make the last element white
		sense.set_pixel(lastPosition[0],lastPosition[1],blank)

		# get the first element
		item = position[0]
		newFirstPosition =[(item[0]+1)%8,item[1]]
		position.insert(0,newFirstPosition)
		sense.set_pixel(newFirstPosition[0],newFirstPosition[1],snake_color)
	elif direction  == "left":
		print ("left")
		# remove the last element
		lastPosition = position.pop(len(position)-1)
		# make the last element white
		sense.set_pixel(lastPosition[0],lastPosition[1],blank)

		# get the first element
		item = position[0]
		newFirstPosition =[(item[0]-1)%8,item[1]]
		position.insert(0,newFirstPosition)
		sense.set_pixel(newFirstPosition[0],newFirstPosition[1],snake_color)
	elif direction == "up":
		print("up")
		# remove the last element
		lastPosition = position.pop(len(position)-1)
		# make the last element white
		sense.set_pixel(lastPosition[0],lastPosition[1],blank)

		# get the first element
		item = position[0]
		newFirstPosition =[item[0],(item[1]-1)%8]
		position.insert(0,newFirstPosition)
		sense.set_pixel(newFirstPosition[0],newFirstPosition[1],snake_color)
	elif direction == "down":
		print("down")
		# remove the last element
		lastPosition = position.pop(len(position)-1)
		# make the last element white
		sense.set_pixel(lastPosition[0],lastPosition[1],blank)

		# get the first element
		item = position[0]
		newFirstPosition =[item[0],(item[1]+1)%8]
		position.insert(0,newFirstPosition)
		sense.set_pixel(newFirstPosition[0],newFirstPosition[1],snake_color)
	else:
		print("unknown")

	if position[0] == fruit_position:
		score = score +1
		print("Your score is: "+str(score))
		make_fruit(position,fruit_position,fruit_color)

score =0
snake_position = [[2, 4],
         [3, 4],
	 [4, 4]]
fruit_position=[-1,-1]

sense.clear()

has_click_middle_button = False

while True:
	sense.stick.direction_any =joystick_start_game 

	# wait for the users to click the middle button
	# TODO:  THIS CODE SHOULD BE REPLACE WITH AN EVENT
	while not has_click_middle_button:
		time.sleep(5)

	#reset the game
	has_click_middle_button = False
	score =0
	draw_snake(snake_position,snake_color)
	make_fruit(snake_position,fruit_position,fruit_color)
	time.sleep(1)

	sense.stick.direction_any = joystick_moved

	game_time_sec =30
	start_time= time.perf_counter()

	while time.perf_counter()-start_time < game_time_sec:
		time.sleep(1)

	print ("Times UP!!")

	sense.clear()
	for i in range(0,3):
		print_sensehat_number.show_number(score, 200,0,60)
		time.sleep(0.4)
		sense.clear()
		time.sleep(0.4)
