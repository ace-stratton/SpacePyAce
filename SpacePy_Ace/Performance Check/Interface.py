# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 06:57:15 2024

@author: Ace Stratton 

This is intended to get payload bytes as needed
"""
import signal, threading, sys
sys.path.insert(0, 'C:/Users/user/Desktop/SpacePy_Ace/fidl')
sys.path.insert(0,'C:/Users/user/Desktop/SpacePy_Ace')
from pygs import pygs, consts, go, gs
pygs.Verbose(enable=True)



def getReturn(payloadBytes, moduleMac, api):
	
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
	#Value = vars(Result[variable])
	#parsedResult = api.enum_SGPO_SetError(Result['e__SGPO_SetError__Err'])
	#outInt = Value['value']
	#output = api.enum_SGPO_SetError.ValuesDict.get(outInt)
	
	
	# Assume response_obj is the object you want to inspect

	

	#print(resultBytes)
	
	
	
	
	return(Result)

