from pygs import pygs, go, gs, consts, event_notifier
import json, base64, signal, threading

def onDataSent(data):
	print("d", end='')
def onDataRecv(data):
	print("D", end='')
def onSyncSent(data):
	print("s", end='')
def onSyncRecv(data):
	print("S", end='')
def onStatusSent(data):
	print("a")
def onStatusRecv(data):
	print("A")

syncSent = event_notifier.Get(event_notifier.EventNotifierId_TPSyncSent)
syncSent.Subscribe(event_notifier.NewFuncEventObserver(onSyncSent, syncSent))

syncRecv = event_notifier.Get(event_notifier.EventNotifierId_TPSyncRecv)
syncRecv.Subscribe(event_notifier.NewFuncEventObserver(onSyncRecv, syncRecv))

statusSent = event_notifier.Get(event_notifier.EventNotifierId_TPStatusSent)
statusSent.Subscribe(event_notifier.NewFuncEventObserver(onStatusSent, statusSent))

statusRecv = event_notifier.Get(event_notifier.EventNotifierId_TPStatusRecv)
statusRecv.Subscribe(event_notifier.NewFuncEventObserver(onStatusRecv, statusRecv))

dataSent = event_notifier.Get(event_notifier.EventNotifierId_TPDataSent)
dataSent.Subscribe(event_notifier.NewFuncEventObserver(onDataSent, dataSent))

dataRecv = event_notifier.Get(event_notifier.EventNotifierId_TPDataRecv)
dataRecv.Subscribe(event_notifier.NewFuncEventObserver(onDataRecv, dataRecv))

payload=go.Slice_byte(bytes([0,48,48,48,84,76,77,84,82,46,84,88,84,0]))

resultBytes = go.Slice_byte()
result = ""

gs1 = gs.NewGS(
	gs.WithFile("../gssd/config.yml"),
	gs.WithMacConn(macProtoId=consts.MacProtoId_TP),
	gs.WithMacGWConn(macProtoId=consts.MacProtoId_TP),
	gs.WithTPConn(tpProtoId=consts.TPProtoId_CP, packetId=13, hostContext=13),
	gs.WithCPConn(cmdId=13, cmdType=1450, cpTripType=consts.CPTripType_ImmediateRes),
)

pygs.Verbose(True)

# Dial a host (module) with one or more config options
# Dial() Address format: "/<mac_proto>[:<mac_addr>]/<tp_proto>/<sys_type>:<sys_addr>:<mac_addr>/<present_proto>"
conn : gs.Conn
rfConn : gs.Conn

conn = gs1.Dial("/esmgw/51/estp/2:0:51/escp")

# Handle Ctrl+C
signal.signal(signal.SIGINT, lambda sig, frame: (conn.Cancel()))

def start():
	# Read and write as well as dial can throw
	conn.Write(payload)
	conn.Read(resultBytes)

t = threading.Thread(target=start)
t.start()
t.join()

conn.Close()

for b in resultBytes:
	result += chr(b)

print(result)
