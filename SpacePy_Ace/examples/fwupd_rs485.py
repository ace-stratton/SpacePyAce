from pygs import pygs, go, gs, consts
from fwupd_utils import SendFWUpdPacket, FWUpdTimeout, GetFWUpdBytes, PrepareFirmwarePayload, PrepareFWUpdCmdId

pygs.Verbose(enable=True)

def SendFWUpdBundle(moduleMac: int, satId: int, cmd: consts.FWUpdCmd, bundlePath : str=""):
    cmdId = PrepareFWUpdCmdId(cmd)
    fwBytes = PrepareFirmwarePayload(bundlePath, isBundle=True, moduleMac=moduleMac)
    print("Sending payload with size {}".format(len(fwBytes)))
    gsArgs = (
        gs.WithFile("../gssd/config.yml"),
        gs.WithMacGWConn(macProtoId=consts.MacProtoId_TP),
        gs.WithTPConn(tpProtoId=consts.TPProtoId_FWUpd, packetId=cmdId, hostContext=cmdId),
        gs.WithFWUpdConn(cmd=cmd, isBundle=True, fileName=""),
    )

    SendFWUpdPacket(satId, moduleMac, fwBytes, gsArgs)

def SendFWUpd(moduleMac: int, moduleType: consts.ModuleTypeId, satId: int, cmd: consts.FWUpdCmd, bundlePath : str=""):
    cmdId = PrepareFWUpdCmdId(cmd)
    fwBytes = PrepareFirmwarePayload(bundlePath, isBundle=False, moduleType=moduleType)
    print("Sending payload with size {}".format(len(fwBytes)))
    gsArgs = (
        gs.WithFile("../gssd/config.yml"),
        gs.WithMacGWConn(macProtoId=consts.MacProtoId_TP),
        gs.WithTPConn(tpProtoId=consts.TPProtoId_FWUpd, packetId=cmdId, hostContext=cmdId),
        gs.WithFWUpdConn(cmd=cmd, isBundle=False, fileName=""),
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

    SendFWUpdPacket(satId, moduleMac, fwBytes, gsArgs)


moduleMac = 17
moduleType = consts.ModuleTypeId_UHF
satId = 2
SendFWUpd(moduleMac, moduleType, satId, consts.FWUpdCmd_Upload, "OBC_STDPF_STM32H_release_4.0.0.bin")
SendFWUpd(moduleMac, moduleType, satId, consts.FWUpdCmd_Status)
SendFWUpd(moduleMac, moduleType, satId, consts.FWUpdCmd_Update)
