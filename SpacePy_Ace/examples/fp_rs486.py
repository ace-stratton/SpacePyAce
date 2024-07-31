from pygs import pygs, go, gs, consts
import signal, threading

pygs.Verbose(enable=True)

moduleMac = 51
payload=go.Slice_byte(bytes([14,0,24,0,0,0,0,0,0]))
resultBytes = go.Slice_byte()

gs1 = gs.NewGS(
	gs.WithFile("../gssd/config.yml"),
    	gs.WithMacGWConn(macProtoId=consts.MacProtoId_FP),
	gs.WithCommSerial("/dev/ttyACM1", 115200, "1s"),
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

print("Result:", bytes(resultBytes))
