import signal, threading, sys
from pygs import pygs, consts, go, gs
pygs.Verbose(enable=True)
sys.path.insert(0, 'C:/Users/user/Desktop/SpacePy_Ace/fidl')

def ace_test(payload_bytes, subsystem):

	### subsystem ###

	if subsystem == "FP_API_EPSII_BP_1":
		from EPSII_BP_1ClientApp import FP_API_EPSII_BP_1
		api = FP_API_EPSII_BP_1()
		moduleMac = 102

	elif subsystem == "FP_API_TIME":
		from timeClientApp import FP_API_TIME
		api = FP_API_TIME()
		moduleMac = 51	
	elif subsystem == "FP_API_OBC":
		from OBCClientApp import FP_API_OBC
		api = FP_API_OBC()
		moduleMac = 51
		
	#elif subsystem == "FP_API_EPSII_BP_2":
		#from EPSII_BP_1ClientApp import FP_API_EPSII_BP_2
		#api = FP_API_EPSII_BP_2()
		

	else:
		print('invalid subsystem')


	if payload_bytes == "GetBatteryInfo":
		payloadBytes = api.req_GetBatteryInfo()
	elif payload_bytes == "Time":
		payloadBytes = api.req_get_time()
	elif payload_bytes == "UpTime":
		payloadBytes = api.req_get_uptime()
		
	else:
		print('wrong command')

	######## Start

	
	payload=go.Slice_byte(payloadBytes)
	resultBytes = go.Slice_byte()

	gs1 = gs.NewGS(
		gs.WithFile("./config.yml"),
	    	gs.WithMacGWConn(macProtoId=consts.MacProtoId_FP),
		gs.WithCommSerial("COM3", 115200, "1s"),
	)

	conn : gs.Conn
	conn = gs1.Dial("/esmgw/{}/esfp".format(moduleMac))

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


	#print(resultBytes)
	parsedResult = api.resp_parse(resultBytes)
	#print(parsedResult['uint8__nConOpsMode'])

	#print(parsedResult['int64__BattCurrent'])
	#print(parsedResult)
	

	return (parsedResult)
