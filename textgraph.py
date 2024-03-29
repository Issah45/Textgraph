import os, time, termcolor

def display(content, color="white", end="\n", x=0, y=0):
	a = ""
	b = ""
	
	for i in range(x):
		a += " "
	for i in range(y):
		b += "\n"
	
	c = termcolor.colored(b+a+content, color)
	print(c, end=end)

def update(fps):
	time.sleep(1/fps)
	os.system("clear")

display("▀█▀ █▀▀ ▀▄▀ ▀█▀ █▀▀ █▀█ ▄▀█ █▀█ █ █")
display(" █  ██▄ █ █  █  █▄█ █▀▄ █▀█ █▀▀ █▀█")
display("0.1.7      ->       Codename Starry")

update(2)

def rectangle(x, y, width, height, color="white"):
	width = width * 2
	
	w = []
	rect = []
	
	o = ""
	
	for i in range(width):
		w.append("█")
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

def prompt(p, color="white"):
	display(p, color=color, end="")
	a = input()
	return a
