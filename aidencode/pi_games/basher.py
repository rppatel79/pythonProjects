from sense_hat import SenseHat
import time
from random import randrange

# Returns the new position of the ball based upon the pitch and roll
def move_marble(pitch,roll,x,y):
	new_x = x
	new_y = y

	if 1 < pitch < 179 and x!=0:
		new_x -=1
	elif 181 < pitch < 359 and x!=7:
		new_x +=1

	if 1 < roll < 179 and y != 7:
		new_y +=1
	elif 359 > roll > 179 and y !=0:
		new_y -=1

	return new_x,new_y

def make_food(hat_grid,b,food_color,num_of_food):
	for i in range(0,num_of_food):
		x=randrange(7)
		y=randrange(7)
		
		while hat_grid[y][x] == food_color:
			x=randrange(7)
			y=randrange(7)

		hat_grid[y][x]=food_color


def start():
	sense = SenseHat()
	sense.clear()

	ball_color = (255,255,255)
	food_color = (220,125,0)

	b = (0,0,0)

	game_over = False

	ball_x_position =7
	ball_y_position =7

	hat_grid = [[b,b,b,b,b,b,b,b],
		[b,b,b,b,b,b,b,b],
		[b,b,b,b,b,b,b,b],
		[b,b,b,b,b,b,b,b],
		[b,b,b,b,b,b,b,b],
		[b,b,b,b,b,b,b,b],
		[b,b,b,b,b,b,b,b],
		[b,b,b,b,b,b,b,b]]

	num_of_food =10
	make_food(hat_grid,b,food_color,num_of_food)

	print ("Created ["+str(num_of_food)+"] food")
	score=0

	sense.set_pixels(sum(hat_grid,[]))

	while not game_over:
		o = sense.get_orientation()
		pitch = o["pitch"]
		roll = o["roll"]
		yaw = o["yaw"]

		new_ball_x_position,new_ball_y_position = move_marble(pitch,roll,ball_x_position,ball_y_position)

		if hat_grid[new_ball_y_position][new_ball_x_position] == food_color:
			score = score +1

		hat_grid[ball_y_position][ball_x_position]=b
		hat_grid[new_ball_y_position][new_ball_x_position]=ball_color
		sense.set_pixels(sum(hat_grid,[]))

		time.sleep(0.05)
		ball_y_position = new_ball_y_position
		ball_x_position = new_ball_x_position

		if score == num_of_food:
			game_over=True

	sense.show_message("You WIN!!")

if __name__ == "__main__":
	start()
