import os

def main():
	print("				 Welcome to Docker to ALL ")
	input()
	print("I'm Doc Doc and I would like to be you assistant ")
	input()
	print("""	Actually I can a lot of things ( mostly Basic ) 
		so kindly choose the operation you want to do
		To see the list of operations that can be performed
			press Enter
	""")
	end=True
	
	while end:
		mainmenu()
		input()
		os.system('clear')

def mainmenu():
	level=input("enter the level of task to perform b : basic , a : advanced, e : expert and exit for exit :	")
	if level=='b':
		basic()
	elif level=='a':
		advanced()
	elif level=='e':
		expert()
	elif level=='exit':
		exit()
	else:
		print("Wrong Input")


def basic():
	os.system('python3 ./basic.py')

def advanced():
	os.system('python3 ./advanced.py')

def expert():
	os.system('python3 ./expert.py')

if __name__=="__main__":
	main()
