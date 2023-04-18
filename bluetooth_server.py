import os
import glob
import time
from bluetooth import *

connection = False
server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "7c7dfdc9-556c-4551-bb46-391b1dd27cc0"

advertise_service( server_sock, "PiServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ] 
#                   protocols = [ OBEX_UUID ] 
                    )
while True:           
	if(connection == False):
		print("Waiting for connection on RFCOMM channel %d" % port)
		client_sock, client_info = server_sock.accept()
		connection = True
		print("Accepted connection from ", client_info)
	try:
		data = client_sock.recv(1024)
		print("incoming data", data)
	except IOError:
		print("Connection disconnected!")
		client_sock.close()
		connection = False
	except BluetoothError:
		print("Something wrong with bluetooth")
	except KeyboardInterrupt:
		print("\nDisconnected")
		client_sock.close()
		server_sock.close()
		break
		
		