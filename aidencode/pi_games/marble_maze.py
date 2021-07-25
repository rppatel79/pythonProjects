from sense_hat import SenseHat
import time

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

	new_x,new_y = check_wall(x,y,new_x,new_y)

	return new_x,new_y

def check_wall(x,y,new_x,new_y):
	if maze1[new_y][new_x] !=r:
		return new_x,new_y
	elif maze1[new_y][x] != r:
		return x, new_y
	elif maze1[y][new_x] != r:
		return new_x,y
	else:
		return x,y

sense = SenseHat()
sense.clear()

r = (255,0,0)
b = (0,0,0)
ball_color = (255,255,255)
hole_color = (220,125,0)

maze1 = [[r,r,r,r,r,r,r,r],
         [r,b,b,b,b,b,b,r],
         [r,r,r,b,r,b,b,r],
         [r,b,r,b,r,r,r,r],
         [r,b,b,b,b,b,b,r],
         [r,b,r,r,r,r,b,r],
         [r,b,b,r,b,b,b,r],
         [r,r,r,r,r,r,r,r]]

#maze1 = [[r,r,r,r,r,r,r,r],
#         [r,b,b,b,b,b,b,b],
#         [r,r,r,r,r,r,r,b],
#         [b,b,b,b,b,b,b,b],
#         [b,r,r,r,r,r,r,r],
#         [b,b,b,b,b,b,b,b],
#         [r,r,r,r,r,r,r,b],
#         [b,b,b,b,b,b,b,b]]

game_over = False

ball_x_position =1
ball_y_position =1

hole_x_position =0
hole_y_position =7

while not game_over:
	o = sense.get_orientation()
	pitch = o["pitch"]
	roll = o["roll"]
	yaw = o["yaw"]

	new_ball_x_position,new_ball_y_position = move_marble(pitch,roll,ball_x_position,ball_y_position)

	maze1[hole_y_position][hole_x_position]=hole_color
	maze1[ball_y_position][ball_x_position]=b
	sense.set_pixels(sum(maze1,[]))

	maze1[new_ball_y_position][new_ball_x_position]=ball_color
	sense.set_pixels(sum(maze1,[]))

	time.sleep(0.05)
	ball_y_position = new_ball_y_position
	ball_x_position = new_ball_x_position

	if ball_x_position == hole_x_position and ball_y_position == hole_y_position:
		sense.show_message("you WIN!")
		game_over = True
