#!/usr/bin/python

from os import system
from time import sleep, strftime




system('modprobe w1-gpio')
system('modprobe w1-therm')

# directory 
dir_temp = "/sys/bus/w1/devices/w1_bus_master1/28-031661fa43ff/w1_slave"

#write temperature history 
t_file = open('result.txt', 'w')


# read 
def read_file(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def wtofile(value):
	if t_file:
		t_file.write(value)
	else:
		print("need to create a new file")


def convert_temp(temp):	
	temp_raw = temp.split("=")[1]	
	temp_final = round(int(temp_raw) / 1000)	
	return temp_final

	
if __name__ == '__main__':

	while True:
		lines = read_file(dir_temp)		
		temp = convert_temp(lines[1])
		# write ambient temperature every hours
		if strftime("%M:%S")== "00:00":
				value = strftime("%A, %H:%M")+ " Temperature : "+ str(temp)+"\n"
		 
				wtofile(value)
		
		print (strftime("%A, %H:%M:%S"),"temperature","=",temp) # affichage a l'ecran		
