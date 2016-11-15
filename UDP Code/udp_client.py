import socket
import sys

def Main():
	robot_info = {}
	# Open jimmy info file and create dictionary
	with open("jimmy_client_info.txt","r") as fin:
		for line in fin:
			line = line.strip('\n')
			parts = line.split(',')
			temp = {}
			temp['host'] = parts[1]
			temp['port'] = int(parts[2])
			robot_info[parts[0]] = temp
	
	print robot_info
	
	robot  = raw_input("Please enter in which robot-> ")
	data = raw_input("Please input the message you want to be sent-> ")

	while robot != "q":
		try:
			host = robot_info[robot]['host']
			HOST = '{}'.format(host) 
			PORT = robot_info[robot]['port'] 
			print HOST
			print PORT
				
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			sock.sendto(data + "\n", (HOST, PORT))
			robot  = raw_input("Please enter in which robot-> ")
			data = raw_input("Please input the message you want to be sent-> ")
			print "Sent:     {}".format(data)
		except:
			print "Please input a value robot name"
			robot  = raw_input("Please enter in which robot-> ")
			data = raw_input("Please input the message you want to be sent-> ")

if __name__ == "__main__":
	Main()
