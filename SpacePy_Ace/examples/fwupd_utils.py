import sys
import random, signal, threading

from pygs import pygs, go, gs, consts, misc

class FWUpdTimeout(Exception):
    def __init__(self, bytesWritten, message="GS timeout"):
        self.bytesWritten = bytesWritten
        self.message = message
        super().__init__(self.message)

def SendFWUpdPacket(satId, moduleMac, filePayload, gsArgs):
    gs1 = gs.NewGS(*gsArgs)
    bytesWritten = 0
    resultBytes = go.Slice_byte()
    result = ""

    print("/esmgw/{}/estp/2:{}:{}/esfwupd".format(moduleMac, moduleMac, satId))
    # Dial a host (module) with one or more config options
    conn : gs.Conn
    conn = gs1.Dial("/esmgw/{}/estp/2:{}:{}/esfwupd".format(moduleMac, moduleMac, satId))

    # Optionally subscribe for notifications
    isRead : bool

    def notify():
        print(isRead + " burst completed")


    data = gs.DataResult()
    def dataNotify():
        print("Data notify:")
        print(bytes(data.Data))
        nonlocal bytesWritten
        bytesWritten = len(bytes(data.Data))

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
        try:
            # Read and write as well as dial can throw
            print("PyGS writing data")
            isRead = "Write"
            conn.Write(filePayload)


            print("PyGS reading result")
            isRead = "Read"
            conn.Read(resultBytes)
            conn.Close()
        except Exception as error:
            if str(error) == "i/o timeout":
                raise FWUpdTimeout(bytesWritten)
            
    t = threading.Thread(target=start)
    t.start()
    t.join()
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    conn.Close()

    for b in resultBytes:
        result += chr(b)
    print(result)

    return resultBytes

def GetFWUpdBytes(filePath):
    if filePath == "":
        return go.Slice_byte(bytes())

    firmware = bytes()
    with open(filePath, 'rb') as binary_file:
        firmware = binary_file.read()
    return go.Slice_byte(firmware)

def PrepareFirmwarePayload(filePath, isBundle, moduleType: consts.ModuleTypeId):
    if filePath == "":
        return go.Slice_byte(bytes())

    firmware = bytes()
    with open(filePath, 'rb') as binary_file:
        if isBundle:
            firmware = misc.FWUpdPrepareBundlePayload(go.Slice_byte(binary_file.read()))
        else:
            firmware = misc.FWUpdPrepareBinaryPayload(go.Slice_byte(binary_file.read()), moduleType)
    return go.Slice_byte(firmware)

def PrepareFWUpdCmdId(cmd):
    cmdId = random.getrandbits(32) << 16 | random.getrandbits(32)
    print(cmdId)
    if cmd == consts.FWUpdCmd_Upload:
        cmdId = cmdId | 0x8000000000000000
    return cmdId
