import os


def main():
	end=True
	count=0
	while end:
		if count==0:
			menu()
			count+=1	
		value=input("enter the respective operation you want to perform: ")
		end=bool(operation(value))


def menu():
		print(''' 
				This are the list of the operation that we can perform in advanced mode

			Press 1 : To see the history of an image
			Press 2 : To check which ports are being already used
			Press 3 : List the networks we have
			Press 4 : Create a network
			Press 5 : Remove a network
			Press 6 : List all the volumes
			Press 7 : Create a volume
			Press 8 : Remove a volume
			Press 0 : Check the log of the container
			Press c : To clear the screen
			Press e : To exit advanced mode
			Press i : To know about this project or tool
			Press m : To display this menu again
			Press s : To check status of docker services
			Press v : To show the version of the docker installed ( if installed )
		''')


def operation(i):
	if i == '1':
		name=input("Enter the name of the image: ")
		os.system('docker history {0}'.format(name))
	
	elif i == '2':
		os.system('netstat -tnlp')
	
	elif i == '3':
		os.system('docker network ls')
	
	elif i == '4':
		driver=input("Enter the driver name to use: ")
		subnet=input("Enter the subnet to use: ")
		name=input("Enter the name of the network: ")
		os.system('docker network create --driver {0} --subnet {1}/16 {2}'.format(driver,subnet,name))
	
	elif i == '5':
		name=input("Enter the name of the network: ")
		os.system('docker network rm {0}'.format(name))
		
	elif i == '6':
		os.system('docker volume ls ')
	
	elif i == '7':
		name=input("Enter the name of the volume: ")
		os.system('docker volume create {}'.format(name))
	
	elif i == '8':
		name=input("Enter the name of the volume: ")
		os.system('docker volume rm {}'.format(name))
	
	elif i == '0':
		name=input("Enter the name of the container: ")
		os.system('docker logs {0}'.format(name))
	
	elif i == 'c':
		os.system('clear')
	
	elif i == 'e':
		return 0
	
	elif i == 'i':
		os.system('cat readme.txt')
	
	elif i == 'm':
		menu()
	
	elif i == 's':
		print('Ctrl + C to exit from the operation')
		print()
		print()
		os.system('systemctl status docker.service')
	
	elif i == 'v':
		os.system('docker version')
	
	else:
		print("Oops! Doc Doc not able to understand your operation. Knidly recheck")
	
	input()
	return 1



if __name__=="__main__":
	main()
