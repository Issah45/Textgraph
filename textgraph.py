import os, time, termcolor, pyautogui

def display(content, color="white", end="\n"):
	c = termcolor.colored(content, color)
	print(c, end=end)

def update(delay):
	time.sleep(delay)
	os.system("clear")

def rectangle(x, y, width, height, color="white"):
	width = width * 2
	
	w = []
	rect = []
	
	o = ""
	
	for i in range(width):
		w.append("▇")
	for i in range(height):
		rect.append(w)
	
	for i in range(y):
		print()
	for i in range(x):
		o += " "
	
	for i in rect:
		print(o, end="")
		for j in i:
			display(j, end="", color=color)
		print()

def key(k):
	i = input()
	if i == k:
		return True
	else:
		return False
