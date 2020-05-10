import os

def main():
	end=True
	count=0
	while end:
		if count==0:
			menu()
			count+=1
		value=input("enter the respective operation you want to perform: ")
		end=bool(opeartion(value,count))


def menu():
		print(''' 
				This are the list of the operation that we can perform in basic mode

			Press 1 : Want to see an container demo
			Press 2 : To see the list of the images you have
			Press 3 : To see the list of containers you have
			Press 4 : To launch a container
			Press 5 : To download an image
			Press 6 : To remove the container/image
			Press 7 : To stop a container OS
			Press 8 : To start a container OS
			Press 9 : To create your custom image
			Press 0 : To see the info of the container
			Press c : To clear the screen
			Press e : To exit basic mode
			Press i : To know about this project or tool
			Press m : To display this menu again
			Press s : To check status of docker services
			Press v : To show the version of the docker installed ( if installed )
		''')




def operation(i,j):
	if i == '1':
		demo()

	elif i == '2':
		os.system('docker images')

	elif i == '3':
		mode=input('''To see all containers: Press a
				To see running containers: Press Enter''')
		if mode=='a':
			os.system('docker container ls --all')
		else:
			os.system('docker container ls')	
		
	elif i == '4':
		image=input("Enter the image name: ")
		name=input("Enter the name you want to give to your container: ")
		mode=input("Enter b for background and l to get inside:")
		if mode=='b':	
			os.system('docker run -dit --name {0} {1}'.format(name,image))
		elif mode=='l':
			os.system('docker run -it --name {0} {1}'.format(name,image))
		else:
			print("Wrong Mode")
			operation(i,j)

	elif i == '5':
		image=input("Enter the name of the image you want to download ")
		os.system('docker pull {image}')

	elif i=='6':
		mode = input("Enter mode c:container i:image ")
		many = input("Enter no. of containers 1:single or all:all ")
		if mode == 'c' and many == '1':
			a = input("Enter the container name ")
			os.system('docker container rm {}'.format(a))
		elif mode == 'c' and many == "all":
			os.system('docker container rm $(docker container ls -a)')
		elif mode == 'i' and many == '1':
			a = input("Enter the image name ")
			os.system('docker image rm {}'.format(a))
		elif mode == 'i' and many == 'all':
			os.system('docker image rm $(docker images)')
		else:
			print("Wrong inputs")

	elif i == '7':
		name=input("Enter the name of the container running to stop ");
		os.system('docker stop {0}'.format(name));

	elif i == '8':
		name=input("Enter the name of the container running to start ");
		os.system('docker start {0}'.format(name));

	elif i == '9':
		name=input("Enter the name of the container you want to create an image(Note the container has to be running in background) ")
		os.system('docker commit {0}'.format(name));

	elif i == '0':
		name=input("Enter the name of the container to see its info ");
		os.system('docker inspect {0}'.format(name));

	elif i == 'c':
		os.system('clear')

	elif i == 'e':
		return 0
	
	elif i == 'i':
		os.system('cat readme.txt')
	
	elif i == 'm':
		j=0
	
	elif i == 's':
		print('Ctrl + C to exit from the operation')
		os.system('systemctl status docker.service')
	
	elif i == 'v':
		os.system('docker version')

	else:
		print("Oops! Doc Doc not able to understand your operation. Knidly recheck")
	
	input()
	return 1



def demo():
	print("Let's see the demo of a container")
	command=input("Enter the command you want to run ")
	image=input("Enter the image you want to run ")
	os.system('docker run --rm {0} {1}'.format(image,command))

if __name__ == '__main__':
    main()