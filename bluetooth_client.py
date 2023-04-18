
import os
import sys
import time
import logging
import logging.config
import json #Uses JSON package
# import cPickle as pickle #Serializing and de-serializing a Python object structure
from bluetooth import * #Python Bluetooth library

uuid = "7c7dfdc9-556c-4551-bb46-391b1dd27cc0"
addr = None
bleService = find_service( uuid = uuid, address = addr )
print(bleService)
clientSocket=BluetoothSocket( RFCOMM )
bleServiceInfo = bleService[0]
print(bleServiceInfo)
clientSocket.connect((bleServiceInfo['host'], bleServiceInfo['port']))
clientSocket.send("hello")