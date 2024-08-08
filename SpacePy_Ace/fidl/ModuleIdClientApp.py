# ********************************************************************************************
# * @file ModuleIdClientApp.py
# * @brief MAC FP client Python implementation generator
# ********************************************************************************************
# * @version           interface ModuleId v0.1
# *
# * @copyright         (C) Copyright EnduroSat
# *
# *                    Contents and presentations are protected world-wide.
# *                    Any kind of using, copying etc. is prohibited without prior permission.
# *                    All rights - incl. industrial property rights - are reserved.
# *
# *-------------------------------------------------------------------------------------------
# * GENERATOR: org.endurosat.generators.macchiato.binders.Gen_Py v1.11
# *-------------------------------------------------------------------------------------------
# * !!! Please note that this code is fully GENERATED and shall not be manually modified as
# * all changes will be overwritten !!!
# ********************************************************************************************

from SerDesHelpers import SerDesHelpers

class FP_API_MODULEID:
    def __init__(self, rawSerDesSupport : bool = False):
        self.const_MODULEID_PROTOCOL_ID = 256
        self.rawSerDesSupport = rawSerDesSupport
        self.versionMajor=0
        self.versionMinor=1


        #
        # Response parsers map
        #
        self.responseParsersDict = {}
        self.responseParsersDict[0] = self.resp_getModuleVersionInfo

    class enum_SwImgType:
        SWIMGTYPE_BOOTLOADER = 0
        SWIMGTYPE_BOOTLOADER_DEBUG = 1
        SWIMGTYPE_APPLICATION = 2
        SWIMGTYPE_APPLICATION_DEBUG = 3
        SWIMGTYPE_OTHER = 4
    
        ValuesDict = {
            SWIMGTYPE_BOOTLOADER : 'SWIMGTYPE_BOOTLOADER', 
            SWIMGTYPE_BOOTLOADER_DEBUG : 'SWIMGTYPE_BOOTLOADER_DEBUG', 
            SWIMGTYPE_APPLICATION : 'SWIMGTYPE_APPLICATION', 
            SWIMGTYPE_APPLICATION_DEBUG : 'SWIMGTYPE_APPLICATION_DEBUG', 
            SWIMGTYPE_OTHER : 'SWIMGTYPE_OTHER'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_MODULEID.enum_SwImgType()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_MODULEID.enum_SwImgType.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_MODULEID.enum_SwImgType.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class struct_BasicVersion:
        def __init__(self, uint16__Major = 0, uint16__Minor = 0, uint16__Patch = 0):
            self.uint16__Major = uint16__Major
            self.uint16__Minor = uint16__Minor
            self.uint16__Patch = uint16__Patch
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__Major)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__Minor)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__Patch)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_MODULEID.struct_BasicVersion()
    
            currentPos = pos
            
            (resultInstance.uint16__Major, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__Minor, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__Patch, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 6
    
    class struct_VersionInfo:
        def __init__(self, uint16__moduleType = 0, s__fwVersion = None, a__uint8__8__buildTime = [], a__uint8__11__buildDate = [], a__uint8__30__buildDescription = [], e__SwImgType__activeImageType = 0, uint8__activeImageId = 0, a__uint8__30__hwSerialNumber = [], s__hwVersion = None):
            self.uint16__moduleType = uint16__moduleType
            self.s__fwVersion = s__fwVersion
            self.a__uint8__8__buildTime = a__uint8__8__buildTime
            self.a__uint8__11__buildDate = a__uint8__11__buildDate
            self.a__uint8__30__buildDescription = a__uint8__30__buildDescription
            self.e__SwImgType__activeImageType = e__SwImgType__activeImageType
            self.uint8__activeImageId = uint8__activeImageId
            self.a__uint8__30__hwSerialNumber = a__uint8__30__hwSerialNumber
            self.s__hwVersion = s__hwVersion
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__moduleType)
            
            result += self.s__fwVersion.serialize()
            actualLen = len(self.a__uint8__8__buildTime)
            
            result += SerDesHelpers.serdesType_basicArray.serialize("uint8", self.a__uint8__8__buildTime, 8)
            actualLen = len(self.a__uint8__11__buildDate)
            
            result += SerDesHelpers.serdesType_basicArray.serialize("uint8", self.a__uint8__11__buildDate, 11)
            actualLen = len(self.a__uint8__30__buildDescription)
            
            result += SerDesHelpers.serdesType_basicArray.serialize("uint8", self.a__uint8__30__buildDescription, 30)
            
            result += FP_API_MODULEID.enum_SwImgType(self.e__SwImgType__activeImageType).serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__activeImageId)
            actualLen = len(self.a__uint8__30__hwSerialNumber)
            
            result += SerDesHelpers.serdesType_basicArray.serialize("uint8", self.a__uint8__30__hwSerialNumber, 30)
            
            result += self.s__hwVersion.serialize()
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_MODULEID.struct_VersionInfo()
    
            currentPos = pos
            
            (resultInstance.uint16__moduleType, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.s__fwVersion, bytesProcessed) = FP_API_MODULEID.struct_BasicVersion.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.a__uint8__8__buildTime, bytesProcessed) = SerDesHelpers.serdesType_basicArray.deserialize("uint8", data, currentPos, 8)
            currentPos += bytesProcessed
            
            
            (resultInstance.a__uint8__11__buildDate, bytesProcessed) = SerDesHelpers.serdesType_basicArray.deserialize("uint8", data, currentPos, 11)
            currentPos += bytesProcessed
            
            
            (resultInstance.a__uint8__30__buildDescription, bytesProcessed) = SerDesHelpers.serdesType_basicArray.deserialize("uint8", data, currentPos, 30)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__SwImgType__activeImageType, bytesProcessed) = FP_API_MODULEID.enum_SwImgType.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__activeImageId, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.a__uint8__30__hwSerialNumber, bytesProcessed) = SerDesHelpers.serdesType_basicArray.deserialize("uint8", data, currentPos, 30)
            currentPos += bytesProcessed
            
            
            (resultInstance.s__hwVersion, bytesProcessed) = FP_API_MODULEID.struct_BasicVersion.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 95
    

    ############################################################################################################
    """
    Request function for FIDL method: getModuleVersionInfo
        - function ID: 00000000
        - description: Get SAT module versioning information
    """
    def req_getModuleVersionInfo(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_MODULEID_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000000
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000000, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: getModuleVersionInfo
        - function ID: 00000000
        - description: Get SAT module versioning information
    """
    def resp_getModuleVersionInfo(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_MODULEID_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000000):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_MODULEID.struct_VersionInfo.deserialize(data, currentPos)
        responseInstance["s__settings"] = field
        currentPos += bytesProcessed
    
        return responseInstance


    ############################################################################################################
    """
    Deserializes the provided bytearray and returns a dictionary of parsed values for the response;
    functionId parameter shall be supplied if the class is used in rawSerDesSupport mode, otherwise
    it is extracted from the FP header
    """
    def resp_parse(self, respBytes, functionId : int = 0):
        if not self.rawSerDesSupport:
            # try to parse FunctionProtocol header
            (fpHeaderInstance, bytesProcessed) = SerDesHelpers.struct_FPHeader.deserialize(respBytes, 0)
            funcId = fpHeaderInstance.u32FuncId

            if fpHeaderInstance.u16ProtoId != self.const_MODULEID_PROTOCOL_ID:
                raise Exception("Unsupported protocol ID", fpHeaderInstance.u16ProtoId)
        else:
            funcId = functionId

        if funcId in self.responseParsersDict:
            respParserFunc = self.responseParsersDict[funcId]
            return respParserFunc(respBytes) if respParserFunc is not None else None
        else:
            raise Exception('Unsupported function id', hex(funcId))
    ############################################################################################################
    """
    Returns the Protocol version as a string vM.m
    """
    def get_version(self):
        return f'v{self.versionMajor}.{self.versionMinor}'
    ############################################################################################################

