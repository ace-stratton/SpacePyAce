
import multiprocessing
import time

from pygs import go, gs, consts
from fwupd_utils import PrepareFWUpdHex, PrepareFWUpdCmdId, SendFWUpdPacket, FWUpdTimeout

cmd = consts.FWUpdCmd_Upload
cmdId = PrepareFWUpdCmdId(cmd)
moduleMac = 17
satId = 2
file = PrepareFWUpdHex("app_274.hex")
fileSize = len(file)
print("Sending payload with size {}".format(fileSize))
addresses = consts.AddressMap()
addresses.Add(val="esmgw/1")
addresses.Add(val="esamac/0")
addresses.Add(val="esugw/0")
addresses.Add(val="estp/1:0:0")

gsArgs = (
    gs.WithFile("../gssd/config.yml"),
    gs.WithGSConn("1s", "1s", "1s", "1s", 1500),
    gs.WithMacGWConn(macProtoId=consts.MacProtoId_TP),
    gs.WithTPConn(tpProtoId=consts.TPProtoId_FWUpd, packetId=cmdId, hostContext=cmdId),
    gs.WithFWUpdConn(cmd=cmd, isBundle=False),
    gs.WithFWUpdBundle(
        SubModule=0,
        ModuleType=0,
        ModuleConfig=1,
        BoardRevision=1,
        CPUType=1,
        FWType=1,
        FWVerMaj=1,
        FWVerMin=0,
        Flags=0
    ),
)

while True:
    try:
        print("Sending FWUpd with cmdId: {}".format(cmdId))
        SendFWUpdPacket(satId, moduleMac, file, gsArgs)
    except FWUpdTimeout as timeout:
        if timeout.bytesWritten >= fileSize:
            break
