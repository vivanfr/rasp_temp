#!/usr/bin/python

from os import system, path			
from time import sleep, strftime
import sys

system('modprobe w1-gpio')
system('modprobe w1-therm')

# directory 
dir_temp = "/sys/bus/w1/devices/w1_bus_master1/28-031661fa43ff/w1_slave"

#write temperature history 
t_file = open(path.join('/home/pi/Working','result.txt'), 'w')


# read temperature
def read_file(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    return lines
	
#Write temperature to text file
def wtofile(value):

	if t_file:
		t_file.write(value)
	else:
		print("need to create a new file")
	#write to file in real-time	
	sys.stdout.flush()
	t_file.flush()

def convert_temp(temp):	

	temp_raw = temp.split("=")[1]	
	temp_final = round(int(temp_raw) / 1000, 2)	
	return temp_final

	
if __name__ == '__main__':

	while True:
		
		lines = read_file(dir_temp)		
		temp = convert_temp(lines[1])
		
		# write ambient temperature every hours
		if strftime("%M:%S")== "00:00":
			
			val = strftime("%A, %H:%M:%S")+ " Temperature : "+ str(temp)+"\n"		 
			wtofile(val)
		
		#print (strftime("%A, %H:%M:%S"),"temperature","=",temp) # affichage a l'ecran		
