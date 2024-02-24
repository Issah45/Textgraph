import os, time, termcolor

def display(content, color="white"):
	c = termcolor.colored(content, color)
	print(c)

def update(delay):
	time.sleep(delay)
	os.system("clear")
