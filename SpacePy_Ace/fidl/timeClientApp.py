# ********************************************************************************************
# * @file timeClientApp.py
# * @brief MAC FP client Python implementation generator
# ********************************************************************************************
# * @version           interface time v0.1
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

class FP_API_TIME:
    def __init__(self, rawSerDesSupport : bool = False):
        self.const_TIME_PROTOCOL_ID = 24
        self.rawSerDesSupport = rawSerDesSupport
        self.versionMajor=0
        self.versionMinor=1


        #
        # Response parsers map
        #
        self.responseParsersDict = {}
        self.responseParsersDict[1] = self.resp_set_date
        self.responseParsersDict[2] = self.resp_get_date
        self.responseParsersDict[3] = self.resp_set_time
        self.responseParsersDict[4] = self.resp_get_time
        self.responseParsersDict[5] = self.resp_enable_calibration_output
        self.responseParsersDict[6] = self.resp_configure_rtc_calibration_parameters
        self.responseParsersDict[7] = self.resp_retrieve_rtc_calibration_parameters
        self.responseParsersDict[8] = self.resp_get_rtc_clock_source

    class enum_op_status:
        OP_STATUS_ERROR = 0
        OP_STATUS_OK = 1
    
        ValuesDict = {
            OP_STATUS_ERROR : 'OP_STATUS_ERROR', 
            OP_STATUS_OK : 'OP_STATUS_OK'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_TIME.enum_op_status()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_TIME.enum_op_status.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_TIME.enum_op_status.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_week_day:
        WEEK_DAY_INVALID = 0
        WEEK_DAY_MONDAY = 1
        WEEK_DAY_TUESDAY = 2
        WEEK_DAY_WEDNESDAY = 3
        WEEK_DAY_THURSDAY = 4
        WEEK_DAY_FRIDAY = 5
        WEEK_DAY_SATURDAY = 6
        WEEK_DAY_SUNDAY = 7
    
        ValuesDict = {
            WEEK_DAY_INVALID : 'WEEK_DAY_INVALID', 
            WEEK_DAY_MONDAY : 'WEEK_DAY_MONDAY', 
            WEEK_DAY_TUESDAY : 'WEEK_DAY_TUESDAY', 
            WEEK_DAY_WEDNESDAY : 'WEEK_DAY_WEDNESDAY', 
            WEEK_DAY_THURSDAY : 'WEEK_DAY_THURSDAY', 
            WEEK_DAY_FRIDAY : 'WEEK_DAY_FRIDAY', 
            WEEK_DAY_SATURDAY : 'WEEK_DAY_SATURDAY', 
            WEEK_DAY_SUNDAY : 'WEEK_DAY_SUNDAY'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_TIME.enum_week_day()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_TIME.enum_week_day.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_TIME.enum_week_day.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class struct_sdate:
        def __init__(self, uint16__year = 0, uint8__mon = 0, uint8__day = 0, e__week_day__wday = 0):
            self.uint16__year = uint16__year
            self.uint8__mon = uint8__mon
            self.uint8__day = uint8__day
            self.e__week_day__wday = e__week_day__wday
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__year)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__mon)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__day)
            
            result += FP_API_TIME.enum_week_day(self.e__week_day__wday).serialize()
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_TIME.struct_sdate()
    
            currentPos = pos
            
            (resultInstance.uint16__year, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__mon, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__day, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__week_day__wday, bytesProcessed) = FP_API_TIME.enum_week_day.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 5
    
    class struct_stime:
        def __init__(self, uint8__hour = 0, uint8__min = 0, uint8__sec = 0, uint16__ms = 0, uint16__us = 0):
            self.uint8__hour = uint8__hour
            self.uint8__min = uint8__min
            self.uint8__sec = uint8__sec
            self.uint16__ms = uint16__ms
            self.uint16__us = uint16__us
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__hour)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__min)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__sec)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__ms)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__us)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_TIME.struct_stime()
    
            currentPos = pos
            
            (resultInstance.uint8__hour, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__min, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__sec, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__ms, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__us, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 7
    
    class enum_cal_freq:
        CAL_FREQ_F001HZ = 0
        CAL_FREQ_F512HZ = 1
    
        ValuesDict = {
            CAL_FREQ_F001HZ : 'CAL_FREQ_F001HZ', 
            CAL_FREQ_F512HZ : 'CAL_FREQ_F512HZ'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_TIME.enum_cal_freq()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_TIME.enum_cal_freq.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_TIME.enum_cal_freq.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_calp_pulses:
        CALP_PULSES_RESET = 0
        CALP_PULSES_SET = 1
    
        ValuesDict = {
            CALP_PULSES_RESET : 'CALP_PULSES_RESET', 
            CALP_PULSES_SET : 'CALP_PULSES_SET'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_TIME.enum_calp_pulses()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_TIME.enum_calp_pulses.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_TIME.enum_calp_pulses.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_rtc_source:
        RTC_SOURCE_RTC_OSC_NONE = 0
        RTC_SOURCE_RTC_OSC_LSE = 1
        RTC_SOURCE_RTC_OSC_LSI = 2
        RTC_SOURCE_RTC_OSC_HSE = 3
        RTC_SOURCE_RTC_OSC_UNKNOWN = 4
    
        ValuesDict = {
            RTC_SOURCE_RTC_OSC_NONE : 'RTC_SOURCE_RTC_OSC_NONE', 
            RTC_SOURCE_RTC_OSC_LSE : 'RTC_SOURCE_RTC_OSC_LSE', 
            RTC_SOURCE_RTC_OSC_LSI : 'RTC_SOURCE_RTC_OSC_LSI', 
            RTC_SOURCE_RTC_OSC_HSE : 'RTC_SOURCE_RTC_OSC_HSE', 
            RTC_SOURCE_RTC_OSC_UNKNOWN : 'RTC_SOURCE_RTC_OSC_UNKNOWN'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_TIME.enum_rtc_source()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_TIME.enum_rtc_source.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_TIME.enum_rtc_source.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class struct_s_rtc_info:
        def __init__(self, bool__enabled = False, e__rtc_source__source = 0, uint8__rtc_asynchronous_prescaler = 0, uint16__rtc_synchronous_prescaler = 0, uint8__hse_division_factor = 0):
            self.bool__enabled = bool__enabled
            self.e__rtc_source__source = e__rtc_source__source
            self.uint8__rtc_asynchronous_prescaler = uint8__rtc_asynchronous_prescaler
            self.uint16__rtc_synchronous_prescaler = uint16__rtc_synchronous_prescaler
            self.uint8__hse_division_factor = uint8__hse_division_factor
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.bool__enabled)
            
            result += FP_API_TIME.enum_rtc_source(self.e__rtc_source__source).serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__rtc_asynchronous_prescaler)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__rtc_synchronous_prescaler)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__hse_division_factor)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_TIME.struct_s_rtc_info()
    
            currentPos = pos
            
            (resultInstance.bool__enabled, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__rtc_source__source, bytesProcessed) = FP_API_TIME.enum_rtc_source.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__rtc_asynchronous_prescaler, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__rtc_synchronous_prescaler, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__hse_division_factor, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 6
    

    ############################################################################################################
    """
    Request function for FIDL method: set_date
        - function ID: 00000001
        - description: Set internal RTC module date.
                              It will continue to be maintained automatically 
                              until there is voltage supplied to VBAT.
    """
    def req_set_date(self, s__date):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_TIME_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000001
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__date.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000001, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: set_date
        - function ID: 00000001
        - description: Set internal RTC module date.
                              It will continue to be maintained automatically 
                              until there is voltage supplied to VBAT.
    """
    def resp_set_date(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_TIME_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000001):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_TIME.enum_op_status.deserialize(data, currentPos)
        responseInstance["e__op_status__status"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: get_date
        - function ID: 00000002
        - description: Get internal RTC module date.
    """
    def req_get_date(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_TIME_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000002
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000002, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: get_date
        - function ID: 00000002
        - description: Get internal RTC module date.
    """
    def resp_get_date(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_TIME_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000002):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_TIME.enum_op_status.deserialize(data, currentPos)
        responseInstance["e__op_status__status"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_TIME.struct_sdate.deserialize(data, currentPos)
        responseInstance["s__date"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: set_time
        - function ID: 00000003
        - description: Set internal RTC module time. 
                              It will continue to be maintained automatically 
                              until there is voltage supplied to VBAT.
    """
    def req_set_time(self, s__time):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_TIME_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000003
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__time.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000003, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: set_time
        - function ID: 00000003
        - description: Set internal RTC module time. 
                              It will continue to be maintained automatically 
                              until there is voltage supplied to VBAT.
    """
    def resp_set_time(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_TIME_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000003):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_TIME.enum_op_status.deserialize(data, currentPos)
        responseInstance["e__op_status__status"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: get_time
        - function ID: 00000004
        - description: Get internal RTC module time.
    """
    def req_get_time(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_TIME_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000004
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000004, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: get_time
        - function ID: 00000004
        - description: Get internal RTC module time.
    """
    def resp_get_time(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_TIME_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000004):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_TIME.enum_op_status.deserialize(data, currentPos)
        responseInstance["e__op_status__status"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_TIME.struct_stime.deserialize(data, currentPos)
        responseInstance["s__time"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: enable_calibration_output
        - function ID: 00000005
        - description: Enable internal RTC module calibration output 
                              (can be measured on green LED on OBC 1.9).
                              The frequency should be the 'output_frequency'.
                              Once enabled it stays enabled until system reset.
    """
    def req_enable_calibration_output(self, e__cal_freq__f):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_TIME_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000005
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_TIME.enum_cal_freq(e__cal_freq__f).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000005, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: enable_calibration_output
        - function ID: 00000005
        - description: Enable internal RTC module calibration output 
                              (can be measured on green LED on OBC 1.9).
                              The frequency should be the 'output_frequency'.
                              Once enabled it stays enabled until system reset.
    """
    def resp_enable_calibration_output(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_TIME_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000005):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_TIME.enum_op_status.deserialize(data, currentPos)
        responseInstance["e__op_status__status"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: configure_rtc_calibration_parameters
        - function ID: 00000006
        - description: Configure RTC calibration parameters.
                              Configuration is retained in NVM.
    """
    def req_configure_rtc_calibration_parameters(self, e__calp_pulses__calp, uint16__calm):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_TIME_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000006
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_TIME.enum_calp_pulses(e__calp_pulses__calp).serialize()
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint16", uint16__calm)
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000006, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: configure_rtc_calibration_parameters
        - function ID: 00000006
        - description: Configure RTC calibration parameters.
                              Configuration is retained in NVM.
    """
    def resp_configure_rtc_calibration_parameters(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_TIME_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000006):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_TIME.enum_op_status.deserialize(data, currentPos)
        responseInstance["e__op_status__status"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: retrieve_rtc_calibration_parameters
        - function ID: 00000007
        - description: Read configured RTC calibration parameters.
    """
    def req_retrieve_rtc_calibration_parameters(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_TIME_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000007
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000007, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: retrieve_rtc_calibration_parameters
        - function ID: 00000007
        - description: Read configured RTC calibration parameters.
    """
    def resp_retrieve_rtc_calibration_parameters(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_TIME_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000007):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_TIME.enum_calp_pulses.deserialize(data, currentPos)
        responseInstance["e__calp_pulses__calp"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
        responseInstance["uint16__calm"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: get_rtc_clock_source
        - function ID: 00000008
        - description: Read the currently used oscillator source for the RTC clock
    """
    def req_get_rtc_clock_source(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_TIME_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000008
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000008, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: get_rtc_clock_source
        - function ID: 00000008
        - description: Read the currently used oscillator source for the RTC clock
    """
    def resp_get_rtc_clock_source(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_TIME_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000008):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_TIME.enum_op_status.deserialize(data, currentPos)
        responseInstance["e__op_status__status"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_TIME.struct_s_rtc_info.deserialize(data, currentPos)
        responseInstance["s__info"] = field
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

            if fpHeaderInstance.u16ProtoId != self.const_TIME_PROTOCOL_ID:
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

