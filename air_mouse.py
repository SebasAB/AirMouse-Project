from pynput.mouse import Button,Controller 
import time

mouse = Controller() 

def air_mouse(): 
	while True:
		click_count = 0 #to count when left click is used to press or to release 
		f = open("data.txt", "r") #open the txt file to read data
		line = f.readlines() #line will be a list that each list item will be, either a 1 or 0, or a line with x, y and z axis data
		line = line[-1] #line will take the value of the last item (the newest) of the list
		if (len(line)<=1): #if the line lenght only has 1 item then it is either left or right click
			if click_count > 0: #if there's already clicked it will be released
				mouse.release(Button, left)
				click_count-=1
			else: 
				mouse.press(Button, left) #if its not clicked it will be clicked
				click_count+=1

		else: 
			accec = line.split(";") #this will separate into a new array the items in the last line, separated by ";"
			x = float(accec[0]) #the x axis will be the position 0, all of them will be converted from str to float 
			y = float(accec[1]) #the y axis will be the position 1 
			z = float(accec[2]) #the z axis will be the position 2
			mouse.move(-x/2, z) 

		if not line: #if the line is empty the program will stop
			break 

		f.close() #the file will be closed
		time.sleep(0.05) #the program will wait 0.05s until the next iteration 


if __name__ == "__main__":
	air_mouse() #this just runs the air_mouse function 

