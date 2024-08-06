# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 00:24:03 2024

@author: Ace Stratton

This is a function to easier access setting and getting power outputs for the 
Power Distribution Module (PDM)
"""

import signal, threading, sys
sys.path.insert(0, 'C:/Users/user/Desktop/SpacePy_Ace/fidl')
from EPSII_PDM_1ClientApp import FP_API_EPSII_PDM_1

from pygs import pygs, consts, go, gs

pygs.Verbose(enable=True)
api = FP_API_EPSII_PDM_1()
moduleMac = 120

def PDMSetPower(VoltageBus, channel, ONoff):
	
	"""
	Voltage Bus: Opts: 3 = 3.3V, 5 = 5V, 12 = 12V
	channel Opts: "Power1" "Power2" "MasterEnable"
	"""
	
	if VoltageBus == 3: 
		if channel == 'Power1':
			if ONoff == 'ON':
				filter_mask = api.enum_SGPO_Bitmask.SGPO_BITMASK_SGPOBM_3V3_CH1_MASTERENABLE
				values_mask = api.enum_SGPO_ON_Off_Bitmask.SGPO_ON_OFF_BITMASK_SGPOBM_3V3_CH1_MASTERENABLE
				payloadBytes = api.req_SetPowerOutputs(filter_mask, values_mask)
				
				
			elif ONoff == 'OFF':
				filter_mask = api.enum_SGPO_Bitmask.SGPO_BITMASK_SGPOBM_3V3_CH1_MASTERENABLE
				values_mask = api.enum_SGPO_ON_Off_Bitmask.SGPO_ON_OFF_BITMASK_SGPOBM_SWITCH_OFF
				payloadBytes = api.req_SetPowerOutputs(filter_mask, values_mask)
				
				
		elif channel == 'Power2':
			if ONoff == 'ON':
				filter_mask = api.enum_SGPO_Bitmask.SGPO_BITMASK_SGPOBM_3V3_CH2_MASTERENABLE
				values_mask = api.enum_SGPO_ON_Off_Bitmask.SGPO_ON_OFF_BITMASK_SGPOBM_3V3_CH2_MASTERENABLE
				payloadBytes = api.req_SetPowerOutputs(filter_mask, values_mask)
				
				
			elif ONoff == 'OFF':
				filter_mask = api.enum_SGPO_Bitmask.SGPO_BITMASK_SGPOBM_3V3_CH2_MASTERENABLE
				values_mask = api.enum_SGPO_ON_Off_Bitmask.SGPO_ON_OFF_BITMASK_SGPOBM_SWITCH_OFF
				payloadBytes = api.req_SetPowerOutputs(filter_mask, values_mask)
		
	elif VoltageBus == 5:
		if channel == 'Power1':
			if ONoff == 'ON':
				filter_mask = api.enum_SGPO_Bitmask.SGPO_BITMASK_SGPOBM_5V_CH1_MASTERENABLE
				values_mask = api.enum_SGPO_ON_Off_Bitmask.SGPO_ON_OFF_BITMASK_SGPOBM_5V_CH1_MASTERENABLE
				payloadBytes = api.req_SetPowerOutputs(filter_mask, values_mask)
				
				
			elif ONoff == 'OFF':
				filter_mask = api.enum_SGPO_Bitmask.SGPO_BITMASK_SGPOBM_5V_CH1_MASTERENABLE
				values_mask = api.enum_SGPO_ON_Off_Bitmask.SGPO_ON_OFF_BITMASK_SGPOBM_SWITCH_OFF
				payloadBytes = api.req_SetPowerOutputs(filter_mask, values_mask)
				
				
		elif channel == 'Power2':
			if ONoff == 'ON':
				filter_mask = api.enum_SGPO_Bitmask.SGPO_BITMASK_SGPOBM_5V_CH2_MASTERENABLE
				values_mask = api.enum_SGPO_ON_Off_Bitmask.SGPO_ON_OFF_BITMASK_SGPOBM_5V_CH2_MASTERENABLE
				payloadBytes = api.req_SetPowerOutputs(filter_mask, values_mask)
				
				
			elif ONoff == 'OFF':
				filter_mask = api.enum_SGPO_Bitmask.SGPO_BITMASK_SGPOBM_5V_CH2_MASTERENABLE
				values_mask = api.enum_SGPO_ON_Off_Bitmask.SGPO_ON_OFF_BITMASK_SGPOBM_SWITCH_OFF
				payloadBytes = api.req_SetPowerOutputs(filter_mask, values_mask)
				
	elif VoltageBus == 12:
		if channel == 'Power1':
			if ONoff == 'ON':
				filter_mask = api.enum_SGPO_Bitmask.SGPO_BITMASK_SGPOBM_12V_MASTERENABLE
				values_mask = api.enum_SGPO_ON_Off_Bitmask.SGPO_ON_OFF_BITMASK_SGPOBM_12V_MASTERENABLE
				payloadBytes = api.req_SetPowerOutputs(filter_mask, values_mask)
				
				
			elif ONoff == 'OFF':
				filter_mask = api.enum_SGPO_Bitmask.SGPO_BITMASK_SGPOBM_12V_MASTERENABLE
				values_mask = api.enum_SGPO_ON_Off_Bitmask.SGPO_ON_OFF_BITMASK_SGPOBM_SWITCH_OFF
				payloadBytes = api.req_SetPowerOutputs(filter_mask, values_mask)
			
	else:
		print("Invalid setPDM Input")
	
	payload=go.Slice_byte(bytes(payloadBytes))
	resultBytes = go.Slice_byte()

	gs1 = gs.NewGS(
		gs.WithFile("./config.yml"),
	    	gs.WithMacGWConn(macProtoId=consts.MacProtoId_FP),
		gs.WithCommSerial("COM3", 115200, "1s"),
	)
	

	conn : gs.Conn
	conn = gs1.Dial("/esmdg/esmgw/{}/esfp".format(moduleMac))

	# Handle Ctrl+C
	signal.signal(signal.SIGINT, lambda sig, frame: (conn.Cancel()))


	def start():
		# Read and write as well as dial can throw
		#print("PyGS writing data")
		conn.Write(payload)

		#print("PyGS reading result")
		conn.Read(resultBytes)
			

	t = threading.Thread(target=start)

	t.start()
	t.join()

	conn.Close()
	
	
	
	Result = api.resp_parse(bytes(resultBytes))
	Value = vars(Result['e__SGPO_SetError__Err'])
	#parsedResult = api.enum_SGPO_SetError(Result['e__SGPO_SetError__Err'])
	outInt = Value['value']
	output = api.enum_SGPO_SetError.ValuesDict.get(outInt)
	
	
	# Assume response_obj is the object you want to inspect

	

	#print(resultBytes)
	
	
	
	
	return(output)
