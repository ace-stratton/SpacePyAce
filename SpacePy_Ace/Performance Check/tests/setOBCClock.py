# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 04:53:53 2024

@author: user
"""
import sys, signal, threading
sys.path.insert(0,'C:/Users/user/Desktop/SpacePy_Ace/Performance Check')
sys.path.insert(0, 'C:/Users/user/Desktop/SpacePy_Ace/fidl')

from datetime import datetime
from pygs import pygs, consts, go, gs
from timeClientApp import FP_API_TIME
import struct

pygs.Verbose(enable=True)

api = FP_API_TIME()
moduleMac = 51

currentDateTime = datetime.now()



integer_Hr = currentDateTime.hour
integer_Min = currentDateTime.minute
integer_Sec = currentDateTime.second
us = currentDateTime.microsecond
integer_ms = us//1000
integer_us = us - integer_ms*1000



s__time = struct.pack('iiiii',integer_Hr,integer_Min, integer_Sec, integer_ms, integer_us)





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

