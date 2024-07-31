import signal, threading, sys
sys.path.insert(0, 'C:/Users/user/Desktop/SpacePy_Ace/fidl')
from EPSII_BP_1ClientApp import FP_API_EPSII_BP_1
from pygs import pygs, consts, go, gs

pygs.Verbose(enable=True)

api = FP_API_EPSII_BP_1()


payloadBytes = api.req_GetBatteryInfo()

moduleMac = 102
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



parsedResult = api.resp_parse(resultBytes)
print(parsedResult['uint8__nConOpsMode'])

print(parsedResult['int64__BattCurrent'])
print("Parsed:", parsedResult['uint8__nConOpsMode'])

#print("Result:", bytes(resultBytes))
