from pygs import pygs, go, gs, consts
import signal, threading

# Enabling verbose to see all of the logs that are usually native to the Go Comms core
pygs.Verbose(enable=True)

# Module mac, Satellite ID, CmdType and the payload are pretty much the only parameters that differ
# for the different EnduroSat modules (on this level, that is)
moduleMac = 17
satId = 2
cmdType = 1302
payload=go.Slice_byte(bytes([9, 14, 0, 24, 0, 0, 0, 0, 0, 0]))
resultBytes = go.Slice_byte()

# We'll reuse the GSSD config.yml which has everything needed already configured.
# Since we want to communicate a CP command through a Mac Dongle connection we
# set the MacGWConn, TPConn and CPConn options.
# And since the config.yml for the GSSD by default is configured for working with a GS UHF underneath
# we'll have to reconfigure the comm serial device it talks to.
gs1 = gs.NewGS(
	gs.WithFile("../gssd/config.yml"),
    	gs.WithMacGWConn(macProtoId=consts.MacProtoId_TP),
	gs.WithCommSerial("/dev/ttyACM1", 115200, "1s"),
	gs.WithTPConn(tpProtoId=consts.TPProtoId_CP, packetId=13, hostContext=13),
	gs.WithCPConn(cmdId=13, cmdType=cmdType, cpTripType=consts.CPTripType_ImmediateRes),
)

conn : gs.Conn
conn = gs1.Dial("/esmgw/{}/estp/2:{}:{}/escp".format(moduleMac, moduleMac, satId))


isRead : bool

# We want to be notified on every successful TP burst
def notify():
	print(isRead + " burst completed")

# We want to be notified on all the data that we receive from the satellite
data = gs.DataResult()
def dataNotify():
	print("Data notify:")
	print(bytes(data.Data))

# And we want to monitor all incoming and outgoing frames, on mac (macgw, amac, etc.) level
frame = gs.FrameResult()
def frameNotify():
	if frame.IsRead:
		print('Incoming Mac frame from {}, to {} - {}\n'.format(frame.RemoteAddr, frame.LocalAddr, bytes(frame.Data)))
	else:
		print('Outgoing Mac frame from {}, to {} - {}\n'.format(frame.LocalAddr, frame.RemoteAddr, bytes(frame.Data)))

onNotify = pygs.PyNotify()
onNotify.CallBack(notify)
conn.Subscribe(pygs.PyToGsNotify(onNotify))

onDataNotify = pygs.PyDataNotify(Data=data)
onDataNotify.CallBack(dataNotify)
conn.SubscribeData(pygs.PyToGsDataNotify(onDataNotify))

onFrameNotify = pygs.PyFrameNotify(Frame=frame)
onFrameNotify.CallBack(frameNotify)
conn.SubscribeFrame(pygs.PyToGsFrameNotify(onFrameNotify))

# Handle Ctrl+C
signal.signal(signal.SIGINT, lambda sig, frame: (conn.Cancel()))

def start():
# Read and write as well as dial can throw
	print("PyGS writing data")
	isRead = "Write"
	conn.Write(payload)

	print("PyGS reading result")
	isRead = "Read"
	conn.Read(resultBytes)

t = threading.Thread(target=start)
t.start()
t.join()

conn.Close()

print("Result:", bytes(resultBytes))
