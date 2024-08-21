# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 04:17:51 2024

@author: Ace Stratton

This script is intended to handle all the test functions for the performance
tests regarding the Power Distribution Model (PDM)
"""
import sys
sys.path.insert(0, 'C:/Users/user/Desktop/SpacePy_Ace/fidl')
from EPSII_PDM_1ClientApp import FP_API_EPSII_PDM_1
import Interface



api = FP_API_EPSII_PDM_1()
moduleMac = 120


def getPDMHealthInfo(inquiry):
	
	payloadBytes = api.req_GetDeviceHealthInfo()
	out1 = Interface.getReturn(payloadBytes, moduleMac, api)
	results = vars(out1["s__GetDeviceHealthInfo"])
	#print(results)
	
	
	if inquiry == "uptime":
		out = results["int32__ActiveCPU_RunningTime"]
		return(out)
	
	if inquiry == "CPUVoltage":
		out = results["int32__ActiveCPU_Voltage"]
		return(out)
	if inquiry == "Temperatures":
		out = results["int32__ActiveCPU_Temperature"]
		out2 = results["int32__PCB_Temperature_1"]
		out3 = results["int32__PCB_Temperature_2"]
		output = [out, out2, out3]
		return(output)
	else:
		
		return(results)
	
	

