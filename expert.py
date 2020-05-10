import os



def main():
	end=True
	count=0
	os.system('docker pull centos:latest')
	os.system('clear')
	print("""
		Whenever you enter into the expert mode 
		this mode tries to check that you have atleast a centos image ( latest )
		and if not then it will download the image to perform the future operations """)
	while end:
		if count==0:
			menu()
			count+=1	
		value=input("enter the respective operation you want to perform: ")
		end=bool(operation(value))






def menu():
		print(''' 
				This are the list of the operation that we can perform in expert mode

			Press 1 : To create a image with Python installed
			Press 2 : To create a image with Webserver installed
			Press 3 : To create a image with some basic Linux commands installed
			Press 4 : To install docker compose in your system
			Press 5 : To launch own word press Blog site ( using Infrastructure as Code )
			Press 6 : Launch Python Shell
			Press 7 : Launch Webserver
			Press c : To clear the screen
			Press e : To exit form expert mode
			Press i : To know about the project info
			Press m : To see the menu again
			Press s : To see the shortcuts that are frequently used
		''')





def operation(i):
	if i == '1':
		os.system('docker build -t mypython:v1 ./Centos+python')
	
	elif i == '2':
		os.system('docker build -t web:v1 ./Centos+webserver')
	
	elif i == '3':
		os.system('docker build -t basic:v1 ./BasicLinux')
	
	elif i == '4':
		print("installing the docker compose ")
		os.system('curl -L "https://github.com/docker/compose/releases/download/1.25.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
		print("making it executable")
		os.system('sudo chmod +x /usr/local/bin/docker-compose ')
	elif i == '5':
		os.system('docker-compose -d up')
	elif i == '6':
		os.system('docker build -t mypython:v1 ./Centos+python')
		os.system('docker run -it mypython:v1')

	elif i == '7':
		os.system('docker build -t mypython:v1 ./Centos+webserver')
		name=input("Enter the name of the container")
		os.system('docker run -dit --name {} -P web:v1'.format(name))
		print()
		print()
		print("Notedown the IP of the container and also the port no. to connect to the webserver")
		os.system('ifconfig ensp03 '.format(name))
		print()
		os.system('docker ps |grep {} '.format(name))
		print()
		print("now you can access your website using the [ IPAddress:Port ] from your base and host ( also from same network )")

	elif i == 'c':
		os.system('clear')
	
	elif i == 'e':
		return 0
	
	elif i == 'i':
		os.system('cat readme.txt')
	
	elif i == 'm':
		menu()
	
	elif i == 's':
		print("""
				The shortcuts that you can use for some specific opreations are
				Ctrl + P + Q = To exit a container without shutting down or exitting it
				Ctrl + C = To force fully exit any operation
				Ctrl + D = To close or end any operation
		""")	
	
	elif i == 'v':
		os.system('docker version')
	
	else:
		print("Oops! Doc Doc not able to understand your operation. Knidly recheck")
	
	input()
	return 1









if __name__=="__main__":
	main()
