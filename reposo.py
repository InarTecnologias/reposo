import os
from os import listdir
from os.path import isfile, join
import time
import signal
import sys
import configparser

path = "/home/pi/rpi-rgb-led-matrix/examples-api-use/"

config = configparser.ConfigParser()
config.read(path + 'config.ini')
scroll_ms= config['time']['scroll_ms']
duration = config['time']['duration1']
tiempo = int(config['time']['total'])

def stringCreator(mypath):
	s=""
	
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	for img in onlyfiles:
		s =s + " " + mypath + "/" + img
	
	return s
	
def signal_term_handler(signal, frame):
    os.system("python3 /home/pi/reposo/resposo.py")
    sys.exit(0)
 
signal.signal(signal.SIGTERM, signal_term_handler)

i = -1
while True:
	i = i + 1
	time.sleep(tiempo)
	if (i < 3):
		os.system(path + 
		"demo -m " + scroll_ms + " -t " + duration + " -n 0 "
		+  "--led-chain=4 -D 2" + 
		stringCreator(path + "Reposo"))
	else:
		os.system(path + 
		"demo -m " + scroll_ms + " -t " + duration + " -n 0 "
		+  "--led-chain=4 -D 2" + 
		stringCreator(path + "Reposo"))
		i = -1
