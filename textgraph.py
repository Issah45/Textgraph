import os, time, termcolor

def display(content, color="white"):
	c = termcolor.colored(content, color)
	print(c)

def update(fps):
	time.sleep(1/fps)
	os.system("clear")
