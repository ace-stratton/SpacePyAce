# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 06:49:09 2024

@author: Ace Stratton

This file will handle all OBC test interactions
"""

import sys
sys.path.insert(0, 'C:/Users/user/Desktop/SpacePy_Ace/fidl')
from OBCClientApp import FP_API_OBC
from ModuleIdClientApp import FP_API_MODULEID
from timeClientApp import FP_API_TIME
import Interface



api = FP_API_OBC()
moduleMac = 51


def getUptime():
	
	payloadBytes = api.req_get_uptime()
	DictOut = Interface.getReturn(payloadBytes, moduleMac, api)
	out = DictOut["uint32__uptime"]
	#print(out)
	
	return(out)


def getVersion():
	
	api = FP_API_MODULEID()
	payloadBytes = api.req_getModuleVersionInfo()
	Result = Interface.getReturn(payloadBytes, moduleMac, api)
	output = vars(Result['s__settings'])
	Result2 = output['s__fwVersion']
	value = vars(Result2)
	Major = value['uint16__Major']
	Minor = value['uint16__Minor']
	Patch = value['uint16__Patch']
	out = [Major, Minor, Patch]
	#print(out)
	
	return(out)

def getTime():
	api = FP_API_TIME()
	payloadBytes = api.req_get_time()
	Result = Interface.getReturn(payloadBytes, moduleMac, api)
	output = vars(Result['s__time'])
	Hour = output['uint8__hour']
	Min = output['uint8__min']
	Sec = output['uint8__sec']
	out = [Hour, Min, Sec] 
	print(output)
	
	return(out)

def getDate():
	
	api = FP_API_TIME()
	payloadBytes = api.req_get_date()
	Result = Interface.getReturn(payloadBytes, moduleMac, api)
	output = vars(Result['s__date'])
	Day = output['uint8__day']
	Month = output['uint8__mon']
	Year = output['uint16__year']
	out = [Day, Month, Year]
	
	return(out)
	
	
	