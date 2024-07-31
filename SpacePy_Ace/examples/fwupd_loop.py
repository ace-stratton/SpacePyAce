
import multiprocessing
import time

from pygs import gs, consts
from fwupd_utils import PrepareFirmwarePayload, PrepareFWUpdCmdId, SendFWUpdPacket

for i in range(0, 100):
    print("--------------------Attempt {}--------------------".format(i+1))
    cmd = consts.FWUpdCmd_Upload
    cmdId = PrepareFWUpdCmdId(cmd)
    moduleMac = 17
    satId = 2
    moduleType = consts.ModuleTypeId_UHF2
    file = PrepareFirmwarePayload("app_274.hex", False, moduleType)
    print("Sending payload with size {}".format(len(file)))
    gsArgs = (
        gs.WithFile("../gssd/config.yml"),
        gs.WithMacGWConn(macProtoId=consts.MacProtoId_TP),
        gs.WithTPConn(tpProtoId=consts.TPProtoId_FWUpd, packetId=cmdId, hostContext=cmdId),
        gs.WithFWUpdConn(cmd=cmd, isBundle=False),
        gs.WithFWUpdBundle(
            SubModule=0,
            ModuleType=moduleType,
            ModuleConfig=1,
            BoardRevision=1,
            CPUType=1,
            FWType=1,
            FWVerMaj=1,
            FWVerMin=0,
            Flags=0
        ),
    )

    print("Sending FWUpd with cmdId: {}".format(cmdId))

    # Cleanup
    while True:
        p = multiprocessing.Process(target=SendFWUpdPacket, name="SendFWUpdPacket", args=(satId, moduleMac, file, gsArgs,))
        p.start()

        time.sleep(40.0)
        p.join(timeout=1.0)
        if p.is_alive():
            p.terminate()
            continue
        else:
            break

    print("FWUpd No. {} finished, continuing with next one".format(i+1))
