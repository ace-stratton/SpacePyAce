# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 01:05:12 2024

This controls the Power channels on the bus of PADRE

@author: Ace Stratton
"""

### BEGIN @USER Change Below
"""
1 = high = on
0 = low = off
Channel 1 = Power 1
Channel 2 = Power 2
"""
# Control all 
all_ON = 1
all_OFF = 0

#Control Channels
all_CH1_ON = 0
all_CH1_OFF = 0

all_CH2_ON = 0
all_CH2_OFF = 0

#Control Individual 
CH1_3V = 1
CH1_5V = 0

CH2_3V = 1
CH2_5V = 0

ALL_12V = 1

### END @USER Change





















############################################################################
import sys

from PDMInterface import PDMSetPower

sys.path.insert(0, 'C:/Users/user/Desktop/SpacePy_Ace')

if all_ON == 1 and all_OFF == 1:
	sys.exit("Error: This is not quantum, we cannot superposition all of the channels between on and off")
elif (all_ON == 1 and (all_CH1_OFF == 1 or all_CH2_OFF == 1)) or (all_OFF == 1 and (all_CH1_ON == 1 or all_CH2_ON == 1)) :
	sys.exit("Error: This is not quantum, we cannot superposition one of the channels between on and off")
elif all_CH1_OFF == 1 and all_CH1_ON == 1:
	sys.exit("Error: This is not quantum, we cannot superposition Channel 1 between on and off")
elif all_CH2_OFF == 1 and all_CH2_ON == 1:
	sys.exit("Error: This is not quantum, we cannot superposition Channel 2 between on and off")


if all_ON == 1:
	CH1_3V = 1 
	CH1_5V = 1 
	CH2_3V = 1 
	CH2_5V = 1 
	ALL_12V = 1

if all_OFF == 1:
	CH1_3V = 0 
	CH1_5V = 0 
	CH2_3V = 0 
	CH2_5V = 0 
	ALL_12V = 0
	
if all_CH1_ON == 1:
	CH1_3V = 1 
	CH1_5V = 1 
elif all_CH1_OFF == 1:
	CH1_3V = 0 
	CH1_5V = 0 

if all_CH2_ON == 1:
	CH2_3V = 1 
	CH2_5V = 1 
elif all_CH2_OFF == 1:
	CH2_3V = 0 
	CH2_5V = 0 
"""
--------3V Channels-------
"""
if CH1_3V == 1:
	response31 = PDMSetPower(3, "Power1", 'ON')
	print("3V CH1 ENABLE:", response31)
else:
	response31 = PDMSetPower(3, "Power1", 'OFF')
	print("3V CH1 OFF:", response31)
	
if CH2_3V == 1:
	response32 = PDMSetPower(3, "Power2", 'ON')
	print("3V CH2 ENABLE:", response32)
else:
	response32 = PDMSetPower(3, "Power2", 'OFF')
	print("3V CH2 OFF:", response32)
	
	
"""
--------5V Channels-------
"""
if CH1_5V == 1:
	response51 = PDMSetPower(5, "Power1", 'ON')
	print("5V CH1 ENABLE:", response51)
else:
	response51 = PDMSetPower(5, "Power1", 'OFF')
	print("5V CH1 OFF:", response51)
	
if CH2_5V == 1:
	response52 = PDMSetPower(5, "Power2", 'ON')
	print("5V CH2 ENABLE:", response52)
else:
	response52 = PDMSetPower(5, "Power2", 'OFF')
	print("5V CH2 OFF:", response52)
	


"""
--------12V Channel-------
"""
if ALL_12V == 1:
	response121 = PDMSetPower(12, "Power1", 'ON')
	print("12V ENABLE:", response121)
else:
	response121 = PDMSetPower(12, "Power1", 'OFF')
	print("12V OFF:", response121)

