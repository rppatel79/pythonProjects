from sense_hat import SenseHat
import time
import basher
import snake_games
import marble_maze

sense = SenseHat()
def main():
	while True:
		sense.stick.direction_any = None

		sense.show_message("UP basher, LEFT snake, DOWN marble maze")

		event = sense.stick.wait_for_event(emptybuffer=True)
		direction = event.direction
		print ("got event",flush=True)
		if direction == "right":
                	#RANDOM
			print ("not done yet",flush=True)
		elif direction  == "left":
			print ("starting snake",flush=True)
			snake_games.start()
		elif direction == "up":
			print ("starting basher",flush=True)
			basher.start()
		elif direction == "down":
			print ("starting marble_maze",flush=True)
			marble_maze.start()
		else:
			print("Unknown command")
		sense.clear()

if __name__ == "__main__":
	main()
