from pynput.mouse import Button,Controller 
import time

mouse = Controller() 

def air_mouse(): 
	while True:
		click_count = 0 
		f = open("data.txt", "r") 
		line = f.readlines()
		line = line[-1] 
		if (len(line)<=1):
			# Handling the inputs to move the mouse
			if (int(line)==0): 
				mouse.press(Button, right)
				mouse.release(Button, left) 
			else: 
				if click_count > 0: 
					mouse.release(Button, left)
					click_count-=1
				else: 
					mouse.press(Button, left)

		else: 
			accec = line.split(";") 
			x = float(accec[0])
			y = float(accec[1])
			z = float(accec[2])
			mouse.move(-x/2, z) 

		if not line: 
			break 

		f.close() 
		time.sleep(0.05) 


def drawing(): 
	pass


if __name__ == "__main__":
	drawing() 
	air_mouse() 
