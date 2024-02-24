import os, time, termcolor

def display(content, color="white", end="\n"):
	c = termcolor.colored(content, color)
	print(c, end=end)

def update(delay):
	time.sleep(delay)
	os.system("clear")

def rectangle(x, y, width, height, color="white"):
	a = []
	b = []
	
	for i in range(width):
		a.append("▇")
	for i in range(width):
		b.append(a)
	
	for i in range(x):
		print(" ")
	
	for i in range(y):
		print()
	
	for c in b:
		for d in c:
			display(d, color=color, end="")
		print()
