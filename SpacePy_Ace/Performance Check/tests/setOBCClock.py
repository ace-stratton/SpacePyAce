# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 04:53:53 2024

@author: Ace Stratton

Sets the OBC clock via the RTC clock on the computer
"""
import sys, signal, threading
sys.path.insert(0,'C:/Users/user/Desktop/SpacePy_Ace/Performance Check')
sys.path.insert(0, 'C:/Users/user/Desktop/SpacePy_Ace/fidl')

from datetime import datetime
from pygs import pygs, consts, go, gs
from timeClientApp import FP_API_TIME

pygs.Verbose(enable=True)

api = FP_API_TIME()
moduleMac = 51

currentDateTime = datetime.now()



Hr = currentDateTime.hour
Min = currentDateTime.minute
Sec = currentDateTime.second
us = currentDateTime.microsecond
ms = us//1000
us = us - ms*1000

time_handler = FP_API_TIME(rawSerDesSupport=False)

s__time = time_handler.struct_stime(uint8__hour=Hr, uint8__min=Min, uint8__sec=Sec, uint16__ms=ms, uint16__us=us)





payloadBytes = api.req_set_time(s__time)

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
	print("PyGS writing data")
	conn.Write(payload)

	print("PyGS reading result")
	conn.Read(resultBytes)
		

t = threading.Thread(target=start)

t.start()
t.join()

conn.Close()

