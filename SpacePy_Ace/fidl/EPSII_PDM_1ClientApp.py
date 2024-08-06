# ********************************************************************************************
# * @file EPSII_PDM_1ClientApp.py
# * @brief MAC FP client Python implementation generator
# ********************************************************************************************
# * @version           interface EPSII_PDM_1 v1.0
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

class FP_API_EPSII_PDM_1:
    def __init__(self, rawSerDesSupport : bool = False):
        self.const_EPSII_PDM_1_PROTOCOL_ID = 20
        self.rawSerDesSupport = rawSerDesSupport
        self.versionMajor=1
        self.versionMinor=0


        #
        # Response parsers map
        #
        self.responseParsersDict = {}
        self.responseParsersDict[1] = self.resp_GetDeviceInfo
        self.responseParsersDict[2] = self.resp_GetPowerDistributionInfo
        self.responseParsersDict[3] = self.resp_GetDeviceHealthInfo
        self.responseParsersDict[4] = self.resp_SetPC104GPIO
        self.responseParsersDict[5] = self.resp_GetPC104GPIO
        self.responseParsersDict[6] = self.resp_GetRAWSensors
        self.responseParsersDict[7] = self.resp_SetPowerOutputs
        self.responseParsersDict[8] = self.resp_GetPowerOutputs
        self.responseParsersDict[9] = self.resp_SetBasicSettings
        self.responseParsersDict[10] = self.resp_GetBasicSettings
        self.responseParsersDict[11] = self.resp_GetFailSafeExceptions
        self.responseParsersDict[12] = self.resp_GetFailSafeErrCounters
        self.responseParsersDict[13] = self.resp_GetMainAppExceptions
        self.responseParsersDict[14] = self.resp_GetMainAppErrCounters
        self.responseParsersDict[15] = self.resp_OnESCP_ResetMainAppErrCounters
        self.responseParsersDict[16] = self.resp_OnESCP_ResetMainAppExceptions
        self.responseParsersDict[17] = self.resp_OnESCP_ResetFailAppErrCounters
        self.responseParsersDict[18] = self.resp_OnESCP_ResetFailAppExceptions
        self.responseParsersDict[19] = self.resp_GetBulkTelemetry
        self.responseParsersDict[32] = self.resp_ResetDevice
        self.responseParsersDict[33] = self.resp_ForceInstallMainApp
        self.responseParsersDict[34] = self.resp_ForceInstallFailSafeApp
        self.responseParsersDict[35] = self.resp_GetBootLoaderErrCounters
        self.responseParsersDict[36] = self.resp_ResetBootLdrErrCounters

    class enum_ESEPSII_PDM_ReservedValues:
        ESEPSII_PDM_RESERVEDVALUES_ESEPSIISSVPDM_MAX_VAL = 2147483632
        ESEPSII_PDM_RESERVEDVALUES_ESEPSIISSVPDM_UNKNOWN_VAL = 2147483647
        ESEPSII_PDM_RESERVEDVALUES_ESEPSIISSVPDM_ERROR_VAL = 2147483646
    
        ValuesDict = {
            ESEPSII_PDM_RESERVEDVALUES_ESEPSIISSVPDM_MAX_VAL : 'ESEPSII_PDM_RESERVEDVALUES_ESEPSIISSVPDM_MAX_VAL', 
            ESEPSII_PDM_RESERVEDVALUES_ESEPSIISSVPDM_UNKNOWN_VAL : 'ESEPSII_PDM_RESERVEDVALUES_ESEPSIISSVPDM_UNKNOWN_VAL', 
            ESEPSII_PDM_RESERVEDVALUES_ESEPSIISSVPDM_ERROR_VAL : 'ESEPSII_PDM_RESERVEDVALUES_ESEPSIISSVPDM_ERROR_VAL'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_EPSII_PDM_1.enum_ESEPSII_PDM_ReservedValues()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_EPSII_PDM_1.enum_ESEPSII_PDM_ReservedValues.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_EPSII_PDM_1.enum_ESEPSII_PDM_ReservedValues.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 4
    
    class enum_ESEPSII_PDM_SensorIDs:
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_NULL_ID = 0
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1P_I_ID = 1
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1P_U_ID = 2
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1P_P_ID = 3
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1P_T_ID = 4
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1R_I_ID = 5
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1R_U_ID = 6
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1R_P_ID = 7
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1R_T_ID = 8
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2P_I_ID = 9
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2P_U_ID = 10
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2P_P_ID = 11
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2P_T_ID = 12
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2R_I_ID = 13
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2R_U_ID = 14
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2R_P_ID = 15
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2R_T_ID = 16
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1P_I_ID = 17
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1P_U_ID = 18
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1P_P_ID = 19
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1P_T_ID = 20
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1R_I_ID = 21
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1R_U_ID = 22
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1R_P_ID = 23
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1R_T_ID = 24
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2P_I_ID = 25
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2P_U_ID = 26
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2P_P_ID = 27
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2P_T_ID = 28
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2R_I_ID = 29
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2R_U_ID = 30
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2R_P_ID = 31
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2R_T_ID = 32
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_P_I_ID = 33
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_P_U_ID = 34
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_P_P_ID = 35
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_P_T_ID = 36
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_R_I_ID = 37
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_R_U_ID = 38
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_R_P_ID = 39
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_R_T_ID = 40
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_TEMPERATURE_PCB_1_ID = 41
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_TEMPERATURE_PCB_2_ID = 42
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_CPU_T_ID = 43
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_CPU_AVCC_U_ID = 44
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_SYS_BUS_V_IN_MON = 45
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_BAT_RAW_V_OUT_MON = 46
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_BAT_RAW_I_1_OUT_MON = 47
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_BAT_RAW_I_2_OUT_MON = 48
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_12V_OUT_MON = 49
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_5V_OUT_MON_1 = 50
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_5V_OUT_MON_2 = 51
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_3V3_OUT_MON_1 = 52
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_3V3_OUT_MON_2 = 53
        ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_TELEMETRY_PARAMS_MAX_COUNT = 54
    
        ValuesDict = {
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_NULL_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_NULL_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1P_I_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1P_I_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1P_U_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1P_U_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1P_P_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1P_P_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1P_T_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1P_T_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1R_I_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1R_I_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1R_U_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1R_U_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1R_P_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1R_P_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1R_T_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_1R_T_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2P_I_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2P_I_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2P_U_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2P_U_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2P_P_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2P_P_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2P_T_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2P_T_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2R_I_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2R_I_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2R_U_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2R_U_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2R_P_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2R_P_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2R_T_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_3V3_2R_T_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1P_I_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1P_I_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1P_U_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1P_U_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1P_P_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1P_P_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1P_T_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1P_T_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1R_I_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1R_I_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1R_U_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1R_U_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1R_P_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1R_P_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1R_T_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_1R_T_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2P_I_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2P_I_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2P_U_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2P_U_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2P_P_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2P_P_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2P_T_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2P_T_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2R_I_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2R_I_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2R_U_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2R_U_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2R_P_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2R_P_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2R_T_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_5V_2R_T_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_P_I_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_P_I_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_P_U_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_P_U_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_P_P_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_P_P_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_P_T_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_P_T_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_R_I_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_R_I_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_R_U_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_R_U_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_R_P_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_R_P_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_R_T_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_INA_LUP_IN_12V_R_T_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_TEMPERATURE_PCB_1_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_TEMPERATURE_PCB_1_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_TEMPERATURE_PCB_2_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_TEMPERATURE_PCB_2_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_CPU_T_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_CPU_T_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_CPU_AVCC_U_ID : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_CPU_AVCC_U_ID', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_SYS_BUS_V_IN_MON : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_SYS_BUS_V_IN_MON', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_BAT_RAW_V_OUT_MON : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_BAT_RAW_V_OUT_MON', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_BAT_RAW_I_1_OUT_MON : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_BAT_RAW_I_1_OUT_MON', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_BAT_RAW_I_2_OUT_MON : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_BAT_RAW_I_2_OUT_MON', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_12V_OUT_MON : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_12V_OUT_MON', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_5V_OUT_MON_1 : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_5V_OUT_MON_1', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_5V_OUT_MON_2 : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_5V_OUT_MON_2', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_3V3_OUT_MON_1 : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_3V3_OUT_MON_1', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_3V3_OUT_MON_2 : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_ADC_3V3_OUT_MON_2', 
            ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_TELEMETRY_PARAMS_MAX_COUNT : 'ESEPSII_PDM_SENSORIDS_ESEPSIISSVPDM_TELEMETRY_PARAMS_MAX_COUNT'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_EPSII_PDM_1.enum_ESEPSII_PDM_SensorIDs()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_EPSII_PDM_1.enum_ESEPSII_PDM_SensorIDs.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_EPSII_PDM_1.enum_ESEPSII_PDM_SensorIDs.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 2
    
    class struct_ESEPSII_UIP:
        def __init__(self, int32__U = 0, int32__I = 0, int32__P = 0):
            self.int32__U = int32__U
            self.int32__I = int32__I
            self.int32__P = int32__P
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__U)
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__I)
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__P)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_EPSII_PDM_1.struct_ESEPSII_UIP()
    
            currentPos = pos
            
            (resultInstance.int32__U, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.int32__I, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.int32__P, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 12
    
    class enum_ESDI_FirmwareType:
        ESDI_FIRMWARETYPE_ESDIFT_PRODUCTION = 0
        ESDI_FIRMWARETYPE_ESDIFT_FAILSAFE = 1
    
        ValuesDict = {
            ESDI_FIRMWARETYPE_ESDIFT_PRODUCTION : 'ESDI_FIRMWARETYPE_ESDIFT_PRODUCTION', 
            ESDI_FIRMWARETYPE_ESDIFT_FAILSAFE : 'ESDI_FIRMWARETYPE_ESDIFT_FAILSAFE'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_EPSII_PDM_1.enum_ESDI_FirmwareType()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_EPSII_PDM_1.enum_ESDI_FirmwareType.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_EPSII_PDM_1.enum_ESDI_FirmwareType.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_SGGPIO_Bitmask:
        SGGPIO_BITMASK_SGGPIOBM_DIGOUT1 = 1
        SGGPIO_BITMASK_SGGPIOBM_DIGOUT2 = 2
        SGGPIO_BITMASK_SGGPIOBM_DIGOUT3 = 4
        SGGPIO_BITMASK_SGGPIOBM_DIGOUT4 = 8
        SGGPIO_BITMASK_SGGPIOBM_DIGOUT5 = 16
        SGGPIO_BITMASK_SGGPIOBM_DIGOUT6 = 32
        SGGPIO_BITMASK_SGGPIOBM_DIGOUT7 = 64
        SGGPIO_BITMASK_SGGPIOBM_DIGOUT8 = 128
    
        ValuesDict = {
            SGGPIO_BITMASK_SGGPIOBM_DIGOUT1 : 'SGGPIO_BITMASK_SGGPIOBM_DIGOUT1', 
            SGGPIO_BITMASK_SGGPIOBM_DIGOUT2 : 'SGGPIO_BITMASK_SGGPIOBM_DIGOUT2', 
            SGGPIO_BITMASK_SGGPIOBM_DIGOUT3 : 'SGGPIO_BITMASK_SGGPIOBM_DIGOUT3', 
            SGGPIO_BITMASK_SGGPIOBM_DIGOUT4 : 'SGGPIO_BITMASK_SGGPIOBM_DIGOUT4', 
            SGGPIO_BITMASK_SGGPIOBM_DIGOUT5 : 'SGGPIO_BITMASK_SGGPIOBM_DIGOUT5', 
            SGGPIO_BITMASK_SGGPIOBM_DIGOUT6 : 'SGGPIO_BITMASK_SGGPIOBM_DIGOUT6', 
            SGGPIO_BITMASK_SGGPIOBM_DIGOUT7 : 'SGGPIO_BITMASK_SGGPIOBM_DIGOUT7', 
            SGGPIO_BITMASK_SGGPIOBM_DIGOUT8 : 'SGGPIO_BITMASK_SGGPIOBM_DIGOUT8'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_EPSII_PDM_1.enum_SGGPIO_Bitmask()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_EPSII_PDM_1.enum_SGGPIO_Bitmask.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_EPSII_PDM_1.enum_SGGPIO_Bitmask.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_SGGPIO_OnOff_mask:
        SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT_OFF = 0
        SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT1 = 1
        SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT2 = 2
        SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT3 = 4
        SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT4 = 8
        SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT5 = 16
        SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT6 = 32
        SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT7 = 64
        SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT8 = 128
    
        ValuesDict = {
            SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT_OFF : 'SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT_OFF', 
            SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT1 : 'SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT1', 
            SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT2 : 'SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT2', 
            SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT3 : 'SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT3', 
            SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT4 : 'SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT4', 
            SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT5 : 'SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT5', 
            SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT6 : 'SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT6', 
            SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT7 : 'SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT7', 
            SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT8 : 'SGGPIO_ONOFF_MASK_SGGPIOBM_DIGOUT8'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_EPSII_PDM_1.enum_SGGPIO_OnOff_mask()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_EPSII_PDM_1.enum_SGGPIO_OnOff_mask.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_EPSII_PDM_1.enum_SGGPIO_OnOff_mask.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_SGGPIO_SetError:
        SGGPIO_SETERROR_SGGPIOE_SUCCESS = 0
        SGGPIO_SETERROR_SGGPIOE_BAD_STATE = 1
        SGGPIO_SETERROR_SGGPIOE_CHIP_ERR = 2
    
        ValuesDict = {
            SGGPIO_SETERROR_SGGPIOE_SUCCESS : 'SGGPIO_SETERROR_SGGPIOE_SUCCESS', 
            SGGPIO_SETERROR_SGGPIOE_BAD_STATE : 'SGGPIO_SETERROR_SGGPIOE_BAD_STATE', 
            SGGPIO_SETERROR_SGGPIOE_CHIP_ERR : 'SGGPIO_SETERROR_SGGPIOE_CHIP_ERR'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_EPSII_PDM_1.enum_SGGPIO_SetError()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_EPSII_PDM_1.enum_SGGPIO_SetError.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_EPSII_PDM_1.enum_SGGPIO_SetError.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_SGPO_Bitmask:
        SGPO_BITMASK_SGPOBM_BBUS_RAWOUTPUTENABLE = 1
        SGPO_BITMASK_SGPOBM_12V_MASTERENABLE = 2
        SGPO_BITMASK_SGPOBM_12V_SP1_3_ENABLE = 4
        SGPO_BITMASK_SGPOBM_12V_SP1_4_ENABLE = 8
        SGPO_BITMASK_SGPOBM_12V_SP1_5_ENABLE = 16
        SGPO_BITMASK_SGPOBM_5V_CH1_MASTERENABLE = 32
        SGPO_BITMASK_SGPOBM_5V_CH1_SP2_3_ENABLE = 64
        SGPO_BITMASK_SGPOBM_5V_CH1_SP2_4_ENABLE = 128
        SGPO_BITMASK_SGPOBM_5V_CH2_MASTERENABLE = 256
        SGPO_BITMASK_SGPOBM_5V_CH2_SP1_6_ENABLE = 512
        SGPO_BITMASK_SGPOBM_5V_CH2_SP1_7_ENABLE = 1024
        SGPO_BITMASK_SGPOBM_3V3_CH1_MASTERENABLE = 2048
        SGPO_BITMASK_SGPOBM_3V3_CH1_SP2_5_ENABLE = 4096
        SGPO_BITMASK_SGPOBM_3V3_CH1_SP2_6_ENABLE = 8192
        SGPO_BITMASK_SGPOBM_3V3_CH1_SP2_7_ENABLE = 16384
        SGPO_BITMASK_SGPOBM_3V3_CH2_MASTERENABLE = 32768
    
        ValuesDict = {
            SGPO_BITMASK_SGPOBM_BBUS_RAWOUTPUTENABLE : 'SGPO_BITMASK_SGPOBM_BBUS_RAWOUTPUTENABLE', 
            SGPO_BITMASK_SGPOBM_12V_MASTERENABLE : 'SGPO_BITMASK_SGPOBM_12V_MASTERENABLE', 
            SGPO_BITMASK_SGPOBM_12V_SP1_3_ENABLE : 'SGPO_BITMASK_SGPOBM_12V_SP1_3_ENABLE', 
            SGPO_BITMASK_SGPOBM_12V_SP1_4_ENABLE : 'SGPO_BITMASK_SGPOBM_12V_SP1_4_ENABLE', 
            SGPO_BITMASK_SGPOBM_12V_SP1_5_ENABLE : 'SGPO_BITMASK_SGPOBM_12V_SP1_5_ENABLE', 
            SGPO_BITMASK_SGPOBM_5V_CH1_MASTERENABLE : 'SGPO_BITMASK_SGPOBM_5V_CH1_MASTERENABLE', 
            SGPO_BITMASK_SGPOBM_5V_CH1_SP2_3_ENABLE : 'SGPO_BITMASK_SGPOBM_5V_CH1_SP2_3_ENABLE', 
            SGPO_BITMASK_SGPOBM_5V_CH1_SP2_4_ENABLE : 'SGPO_BITMASK_SGPOBM_5V_CH1_SP2_4_ENABLE', 
            SGPO_BITMASK_SGPOBM_5V_CH2_MASTERENABLE : 'SGPO_BITMASK_SGPOBM_5V_CH2_MASTERENABLE', 
            SGPO_BITMASK_SGPOBM_5V_CH2_SP1_6_ENABLE : 'SGPO_BITMASK_SGPOBM_5V_CH2_SP1_6_ENABLE', 
            SGPO_BITMASK_SGPOBM_5V_CH2_SP1_7_ENABLE : 'SGPO_BITMASK_SGPOBM_5V_CH2_SP1_7_ENABLE', 
            SGPO_BITMASK_SGPOBM_3V3_CH1_MASTERENABLE : 'SGPO_BITMASK_SGPOBM_3V3_CH1_MASTERENABLE', 
            SGPO_BITMASK_SGPOBM_3V3_CH1_SP2_5_ENABLE : 'SGPO_BITMASK_SGPOBM_3V3_CH1_SP2_5_ENABLE', 
            SGPO_BITMASK_SGPOBM_3V3_CH1_SP2_6_ENABLE : 'SGPO_BITMASK_SGPOBM_3V3_CH1_SP2_6_ENABLE', 
            SGPO_BITMASK_SGPOBM_3V3_CH1_SP2_7_ENABLE : 'SGPO_BITMASK_SGPOBM_3V3_CH1_SP2_7_ENABLE', 
            SGPO_BITMASK_SGPOBM_3V3_CH2_MASTERENABLE : 'SGPO_BITMASK_SGPOBM_3V3_CH2_MASTERENABLE'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_EPSII_PDM_1.enum_SGPO_Bitmask()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_EPSII_PDM_1.enum_SGPO_Bitmask.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_EPSII_PDM_1.enum_SGPO_Bitmask.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 4
    
    class enum_SGPO_ON_Off_Bitmask:
        SGPO_ON_OFF_BITMASK_SGPOBM_SWITCH_OFF = 0
        SGPO_ON_OFF_BITMASK_SGPOBM_BBUS_RAWOUTPUTENABLE = 1
        SGPO_ON_OFF_BITMASK_SGPOBM_12V_MASTERENABLE = 2
        SGPO_ON_OFF_BITMASK_SGPOBM_12V_SP1_3_ENABLE = 4
        SGPO_ON_OFF_BITMASK_SGPOBM_12V_SP1_4_ENABLE = 8
        SGPO_ON_OFF_BITMASK_SGPOBM_12V_SP1_5_ENABLE = 16
        SGPO_ON_OFF_BITMASK_SGPOBM_5V_CH1_MASTERENABLE = 32
        SGPO_ON_OFF_BITMASK_SGPOBM_5V_CH1_SP2_3_ENABLE = 64
        SGPO_ON_OFF_BITMASK_SGPOBM_5V_CH1_SP2_4_ENABLE = 128
        SGPO_ON_OFF_BITMASK_SGPOBM_5V_CH2_MASTERENABLE = 256
        SGPO_ON_OFF_BITMASK_SGPOBM_5V_CH2_SP1_6_ENABLE = 512
        SGPO_ON_OFF_BITMASK_SGPOBM_5V_CH2_SP1_7_ENABLE = 1024
        SGPO_ON_OFF_BITMASK_SGPOBM_3V3_CH1_MASTERENABLE = 2048
        SGPO_ON_OFF_BITMASK_SGPOBM_3V3_CH1_SP2_5_ENABLE = 4096
        SGPO_ON_OFF_BITMASK_SGPOBM_3V3_CH1_SP2_6_ENABLE = 8192
        SGPO_ON_OFF_BITMASK_SGPOBM_3V3_CH1_SP2_7_ENABLE = 16384
        SGPO_ON_OFF_BITMASK_SGPOBM_3V3_CH2_MASTERENABLE = 32768
    
        ValuesDict = {
            SGPO_ON_OFF_BITMASK_SGPOBM_SWITCH_OFF : 'SGPO_ON_OFF_BITMASK_SGPOBM_SWITCH_OFF', 
            SGPO_ON_OFF_BITMASK_SGPOBM_BBUS_RAWOUTPUTENABLE : 'SGPO_ON_OFF_BITMASK_SGPOBM_BBUS_RAWOUTPUTENABLE', 
            SGPO_ON_OFF_BITMASK_SGPOBM_12V_MASTERENABLE : 'SGPO_ON_OFF_BITMASK_SGPOBM_12V_MASTERENABLE', 
            SGPO_ON_OFF_BITMASK_SGPOBM_12V_SP1_3_ENABLE : 'SGPO_ON_OFF_BITMASK_SGPOBM_12V_SP1_3_ENABLE', 
            SGPO_ON_OFF_BITMASK_SGPOBM_12V_SP1_4_ENABLE : 'SGPO_ON_OFF_BITMASK_SGPOBM_12V_SP1_4_ENABLE', 
            SGPO_ON_OFF_BITMASK_SGPOBM_12V_SP1_5_ENABLE : 'SGPO_ON_OFF_BITMASK_SGPOBM_12V_SP1_5_ENABLE', 
            SGPO_ON_OFF_BITMASK_SGPOBM_5V_CH1_MASTERENABLE : 'SGPO_ON_OFF_BITMASK_SGPOBM_5V_CH1_MASTERENABLE', 
            SGPO_ON_OFF_BITMASK_SGPOBM_5V_CH1_SP2_3_ENABLE : 'SGPO_ON_OFF_BITMASK_SGPOBM_5V_CH1_SP2_3_ENABLE', 
            SGPO_ON_OFF_BITMASK_SGPOBM_5V_CH1_SP2_4_ENABLE : 'SGPO_ON_OFF_BITMASK_SGPOBM_5V_CH1_SP2_4_ENABLE', 
            SGPO_ON_OFF_BITMASK_SGPOBM_5V_CH2_MASTERENABLE : 'SGPO_ON_OFF_BITMASK_SGPOBM_5V_CH2_MASTERENABLE', 
            SGPO_ON_OFF_BITMASK_SGPOBM_5V_CH2_SP1_6_ENABLE : 'SGPO_ON_OFF_BITMASK_SGPOBM_5V_CH2_SP1_6_ENABLE', 
            SGPO_ON_OFF_BITMASK_SGPOBM_5V_CH2_SP1_7_ENABLE : 'SGPO_ON_OFF_BITMASK_SGPOBM_5V_CH2_SP1_7_ENABLE', 
            SGPO_ON_OFF_BITMASK_SGPOBM_3V3_CH1_MASTERENABLE : 'SGPO_ON_OFF_BITMASK_SGPOBM_3V3_CH1_MASTERENABLE', 
            SGPO_ON_OFF_BITMASK_SGPOBM_3V3_CH1_SP2_5_ENABLE : 'SGPO_ON_OFF_BITMASK_SGPOBM_3V3_CH1_SP2_5_ENABLE', 
            SGPO_ON_OFF_BITMASK_SGPOBM_3V3_CH1_SP2_6_ENABLE : 'SGPO_ON_OFF_BITMASK_SGPOBM_3V3_CH1_SP2_6_ENABLE', 
            SGPO_ON_OFF_BITMASK_SGPOBM_3V3_CH1_SP2_7_ENABLE : 'SGPO_ON_OFF_BITMASK_SGPOBM_3V3_CH1_SP2_7_ENABLE', 
            SGPO_ON_OFF_BITMASK_SGPOBM_3V3_CH2_MASTERENABLE : 'SGPO_ON_OFF_BITMASK_SGPOBM_3V3_CH2_MASTERENABLE'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_EPSII_PDM_1.enum_SGPO_ON_Off_Bitmask()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_EPSII_PDM_1.enum_SGPO_ON_Off_Bitmask.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_EPSII_PDM_1.enum_SGPO_ON_Off_Bitmask.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 4
    
    class enum_SGPO_SetError:
        SGPO_SETERROR_SGPOSE_SUCCESS = 0
        SGPO_SETERROR_SGPOSE_BAD_STATE = 1
        SGPO_SETERROR_SGPOSE_CHIP_ERR = 2
    
        ValuesDict = {
            SGPO_SETERROR_SGPOSE_SUCCESS : 'SGPO_SETERROR_SGPOSE_SUCCESS', 
            SGPO_SETERROR_SGPOSE_BAD_STATE : 'SGPO_SETERROR_SGPOSE_BAD_STATE', 
            SGPO_SETERROR_SGPOSE_CHIP_ERR : 'SGPO_SETERROR_SGPOSE_CHIP_ERR'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_EPSII_PDM_1.enum_SGPO_SetError()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_EPSII_PDM_1.enum_SGPO_SetError.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_EPSII_PDM_1.enum_SGPO_SetError.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_SBSED_Bitmask:
        SBSED_BITMASK_SBSEDBM_DISABLED = 0
        SBSED_BITMASK_SBSEDBM_PHOENIX_MODE = 2
        SBSED_BITMASK_SBSEDBM_NORMAL_MODE = 4
        SBSED_BITMASK_SBSEDBM_PHOENIX_MODE_AND_NORMAL = 6
    
        ValuesDict = {
            SBSED_BITMASK_SBSEDBM_DISABLED : 'SBSED_BITMASK_SBSEDBM_DISABLED', 
            SBSED_BITMASK_SBSEDBM_PHOENIX_MODE : 'SBSED_BITMASK_SBSEDBM_PHOENIX_MODE', 
            SBSED_BITMASK_SBSEDBM_NORMAL_MODE : 'SBSED_BITMASK_SBSEDBM_NORMAL_MODE', 
            SBSED_BITMASK_SBSEDBM_PHOENIX_MODE_AND_NORMAL : 'SBSED_BITMASK_SBSEDBM_PHOENIX_MODE_AND_NORMAL'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_EPSII_PDM_1.enum_SBSED_Bitmask()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_EPSII_PDM_1.enum_SBSED_Bitmask.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_EPSII_PDM_1.enum_SBSED_Bitmask.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 8
    
    class enum_SBSEDE_ConOpsMode:
        SBSEDE_CONOPSMODE_SBSEDE_HELL_MODE = 1
        SBSEDE_CONOPSMODE_SBSEDE_OVH_MODE = 2
        SBSEDE_CONOPSMODE_SBSEDE_PHOENIX_MODE = 3
        SBSEDE_CONOPSMODE_SBSEDE_NORMAL_MODE = 4
    
        ValuesDict = {
            SBSEDE_CONOPSMODE_SBSEDE_HELL_MODE : 'SBSEDE_CONOPSMODE_SBSEDE_HELL_MODE', 
            SBSEDE_CONOPSMODE_SBSEDE_OVH_MODE : 'SBSEDE_CONOPSMODE_SBSEDE_OVH_MODE', 
            SBSEDE_CONOPSMODE_SBSEDE_PHOENIX_MODE : 'SBSEDE_CONOPSMODE_SBSEDE_PHOENIX_MODE', 
            SBSEDE_CONOPSMODE_SBSEDE_NORMAL_MODE : 'SBSEDE_CONOPSMODE_SBSEDE_NORMAL_MODE'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_EPSII_PDM_1.enum_SBSEDE_ConOpsMode()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_EPSII_PDM_1.enum_SBSEDE_ConOpsMode.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_EPSII_PDM_1.enum_SBSEDE_ConOpsMode.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 8
    
    class struct_SBasicSettings:
        def __init__(self, e__SBSEDE_ConOpsMode__nConOpsStartMode = 0, e__SBSED_Bitmask__nBBUS_RAWOutputEnable = 0, int32__n12V_Voltage = 0, int32__n12V_CurrentLimit = 0, e__SBSED_Bitmask__n12V_MasterEnable = 0, e__SBSED_Bitmask__n12V_SP1_3_Enable = 0, e__SBSED_Bitmask__n12V_SP1_4_Enable = 0, e__SBSED_Bitmask__n12V_SP1_5_Enable = 0, int32__n5V_Ch1_CurrentLimit = 0, e__SBSED_Bitmask__n5V_Ch1_MasterEnable = 0, e__SBSED_Bitmask__n5V_Ch1_SP2_3_Enable = 0, e__SBSED_Bitmask__n5V_Ch1_SP2_4_Enable = 0, int32__n5V_Ch2_CurrentLimit = 0, e__SBSED_Bitmask__n5V_Ch2_MasterEnable = 0, e__SBSED_Bitmask__n5V_Ch2_SP1_6_Enable = 0, e__SBSED_Bitmask__n5V_Ch2_SP1_7_Enable = 0, int32__n3V3_Ch1_CurrentLimit = 0, e__SBSED_Bitmask__n3V3_Ch1_MasterEnable = 0, e__SBSED_Bitmask__n3V3_Ch1_SP2_5_Enable = 0, e__SBSED_Bitmask__n3V3_Ch1_SP2_6_Enable = 0, e__SBSED_Bitmask__n3V3_Ch1_SP2_7_Enable = 0, int32__n3V3_Ch2_CurrentLimit = 0, e__SBSED_Bitmask__n3V3_Ch2_MasterEnable = 0, uint16__nPC104_GPIO_InversedBitmask = 0, uint16__nPC104_GPIO_NormalModeValueBitmask = 0, uint16__nPC104_GPIO_PhoenixModeValueBitmask = 0, uint16__nPC104_GPIO_OvhModeValueBitmask = 0):
            self.e__SBSEDE_ConOpsMode__nConOpsStartMode = e__SBSEDE_ConOpsMode__nConOpsStartMode
            self.e__SBSED_Bitmask__nBBUS_RAWOutputEnable = e__SBSED_Bitmask__nBBUS_RAWOutputEnable
            self.int32__n12V_Voltage = int32__n12V_Voltage
            self.int32__n12V_CurrentLimit = int32__n12V_CurrentLimit
            self.e__SBSED_Bitmask__n12V_MasterEnable = e__SBSED_Bitmask__n12V_MasterEnable
            self.e__SBSED_Bitmask__n12V_SP1_3_Enable = e__SBSED_Bitmask__n12V_SP1_3_Enable
            self.e__SBSED_Bitmask__n12V_SP1_4_Enable = e__SBSED_Bitmask__n12V_SP1_4_Enable
            self.e__SBSED_Bitmask__n12V_SP1_5_Enable = e__SBSED_Bitmask__n12V_SP1_5_Enable
            self.int32__n5V_Ch1_CurrentLimit = int32__n5V_Ch1_CurrentLimit
            self.e__SBSED_Bitmask__n5V_Ch1_MasterEnable = e__SBSED_Bitmask__n5V_Ch1_MasterEnable
            self.e__SBSED_Bitmask__n5V_Ch1_SP2_3_Enable = e__SBSED_Bitmask__n5V_Ch1_SP2_3_Enable
            self.e__SBSED_Bitmask__n5V_Ch1_SP2_4_Enable = e__SBSED_Bitmask__n5V_Ch1_SP2_4_Enable
            self.int32__n5V_Ch2_CurrentLimit = int32__n5V_Ch2_CurrentLimit
            self.e__SBSED_Bitmask__n5V_Ch2_MasterEnable = e__SBSED_Bitmask__n5V_Ch2_MasterEnable
            self.e__SBSED_Bitmask__n5V_Ch2_SP1_6_Enable = e__SBSED_Bitmask__n5V_Ch2_SP1_6_Enable
            self.e__SBSED_Bitmask__n5V_Ch2_SP1_7_Enable = e__SBSED_Bitmask__n5V_Ch2_SP1_7_Enable
            self.int32__n3V3_Ch1_CurrentLimit = int32__n3V3_Ch1_CurrentLimit
            self.e__SBSED_Bitmask__n3V3_Ch1_MasterEnable = e__SBSED_Bitmask__n3V3_Ch1_MasterEnable
            self.e__SBSED_Bitmask__n3V3_Ch1_SP2_5_Enable = e__SBSED_Bitmask__n3V3_Ch1_SP2_5_Enable
            self.e__SBSED_Bitmask__n3V3_Ch1_SP2_6_Enable = e__SBSED_Bitmask__n3V3_Ch1_SP2_6_Enable
            self.e__SBSED_Bitmask__n3V3_Ch1_SP2_7_Enable = e__SBSED_Bitmask__n3V3_Ch1_SP2_7_Enable
            self.int32__n3V3_Ch2_CurrentLimit = int32__n3V3_Ch2_CurrentLimit
            self.e__SBSED_Bitmask__n3V3_Ch2_MasterEnable = e__SBSED_Bitmask__n3V3_Ch2_MasterEnable
            self.uint16__nPC104_GPIO_InversedBitmask = uint16__nPC104_GPIO_InversedBitmask
            self.uint16__nPC104_GPIO_NormalModeValueBitmask = uint16__nPC104_GPIO_NormalModeValueBitmask
            self.uint16__nPC104_GPIO_PhoenixModeValueBitmask = uint16__nPC104_GPIO_PhoenixModeValueBitmask
            self.uint16__nPC104_GPIO_OvhModeValueBitmask = uint16__nPC104_GPIO_OvhModeValueBitmask
    
        def serialize(self):
            result = bytearray()
    
            
            result += FP_API_EPSII_PDM_1.enum_SBSEDE_ConOpsMode(self.e__SBSEDE_ConOpsMode__nConOpsStartMode).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_SBSED_Bitmask(self.e__SBSED_Bitmask__nBBUS_RAWOutputEnable).serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__n12V_Voltage)
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__n12V_CurrentLimit)
            
            result += FP_API_EPSII_PDM_1.enum_SBSED_Bitmask(self.e__SBSED_Bitmask__n12V_MasterEnable).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_SBSED_Bitmask(self.e__SBSED_Bitmask__n12V_SP1_3_Enable).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_SBSED_Bitmask(self.e__SBSED_Bitmask__n12V_SP1_4_Enable).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_SBSED_Bitmask(self.e__SBSED_Bitmask__n12V_SP1_5_Enable).serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__n5V_Ch1_CurrentLimit)
            
            result += FP_API_EPSII_PDM_1.enum_SBSED_Bitmask(self.e__SBSED_Bitmask__n5V_Ch1_MasterEnable).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_SBSED_Bitmask(self.e__SBSED_Bitmask__n5V_Ch1_SP2_3_Enable).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_SBSED_Bitmask(self.e__SBSED_Bitmask__n5V_Ch1_SP2_4_Enable).serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__n5V_Ch2_CurrentLimit)
            
            result += FP_API_EPSII_PDM_1.enum_SBSED_Bitmask(self.e__SBSED_Bitmask__n5V_Ch2_MasterEnable).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_SBSED_Bitmask(self.e__SBSED_Bitmask__n5V_Ch2_SP1_6_Enable).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_SBSED_Bitmask(self.e__SBSED_Bitmask__n5V_Ch2_SP1_7_Enable).serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__n3V3_Ch1_CurrentLimit)
            
            result += FP_API_EPSII_PDM_1.enum_SBSED_Bitmask(self.e__SBSED_Bitmask__n3V3_Ch1_MasterEnable).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_SBSED_Bitmask(self.e__SBSED_Bitmask__n3V3_Ch1_SP2_5_Enable).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_SBSED_Bitmask(self.e__SBSED_Bitmask__n3V3_Ch1_SP2_6_Enable).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_SBSED_Bitmask(self.e__SBSED_Bitmask__n3V3_Ch1_SP2_7_Enable).serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__n3V3_Ch2_CurrentLimit)
            
            result += FP_API_EPSII_PDM_1.enum_SBSED_Bitmask(self.e__SBSED_Bitmask__n3V3_Ch2_MasterEnable).serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__nPC104_GPIO_InversedBitmask)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__nPC104_GPIO_NormalModeValueBitmask)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__nPC104_GPIO_PhoenixModeValueBitmask)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__nPC104_GPIO_OvhModeValueBitmask)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_EPSII_PDM_1.struct_SBasicSettings()
    
            currentPos = pos
            
            (resultInstance.e__SBSEDE_ConOpsMode__nConOpsStartMode, bytesProcessed) = FP_API_EPSII_PDM_1.enum_SBSEDE_ConOpsMode.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__SBSED_Bitmask__nBBUS_RAWOutputEnable, bytesProcessed) = FP_API_EPSII_PDM_1.enum_SBSED_Bitmask.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.int32__n12V_Voltage, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.int32__n12V_CurrentLimit, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__SBSED_Bitmask__n12V_MasterEnable, bytesProcessed) = FP_API_EPSII_PDM_1.enum_SBSED_Bitmask.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__SBSED_Bitmask__n12V_SP1_3_Enable, bytesProcessed) = FP_API_EPSII_PDM_1.enum_SBSED_Bitmask.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__SBSED_Bitmask__n12V_SP1_4_Enable, bytesProcessed) = FP_API_EPSII_PDM_1.enum_SBSED_Bitmask.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__SBSED_Bitmask__n12V_SP1_5_Enable, bytesProcessed) = FP_API_EPSII_PDM_1.enum_SBSED_Bitmask.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.int32__n5V_Ch1_CurrentLimit, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__SBSED_Bitmask__n5V_Ch1_MasterEnable, bytesProcessed) = FP_API_EPSII_PDM_1.enum_SBSED_Bitmask.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__SBSED_Bitmask__n5V_Ch1_SP2_3_Enable, bytesProcessed) = FP_API_EPSII_PDM_1.enum_SBSED_Bitmask.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__SBSED_Bitmask__n5V_Ch1_SP2_4_Enable, bytesProcessed) = FP_API_EPSII_PDM_1.enum_SBSED_Bitmask.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.int32__n5V_Ch2_CurrentLimit, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__SBSED_Bitmask__n5V_Ch2_MasterEnable, bytesProcessed) = FP_API_EPSII_PDM_1.enum_SBSED_Bitmask.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__SBSED_Bitmask__n5V_Ch2_SP1_6_Enable, bytesProcessed) = FP_API_EPSII_PDM_1.enum_SBSED_Bitmask.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__SBSED_Bitmask__n5V_Ch2_SP1_7_Enable, bytesProcessed) = FP_API_EPSII_PDM_1.enum_SBSED_Bitmask.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.int32__n3V3_Ch1_CurrentLimit, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__SBSED_Bitmask__n3V3_Ch1_MasterEnable, bytesProcessed) = FP_API_EPSII_PDM_1.enum_SBSED_Bitmask.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__SBSED_Bitmask__n3V3_Ch1_SP2_5_Enable, bytesProcessed) = FP_API_EPSII_PDM_1.enum_SBSED_Bitmask.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__SBSED_Bitmask__n3V3_Ch1_SP2_6_Enable, bytesProcessed) = FP_API_EPSII_PDM_1.enum_SBSED_Bitmask.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__SBSED_Bitmask__n3V3_Ch1_SP2_7_Enable, bytesProcessed) = FP_API_EPSII_PDM_1.enum_SBSED_Bitmask.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.int32__n3V3_Ch2_CurrentLimit, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__SBSED_Bitmask__n3V3_Ch2_MasterEnable, bytesProcessed) = FP_API_EPSII_PDM_1.enum_SBSED_Bitmask.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__nPC104_GPIO_InversedBitmask, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__nPC104_GPIO_NormalModeValueBitmask, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__nPC104_GPIO_PhoenixModeValueBitmask, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__nPC104_GPIO_OvhModeValueBitmask, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 49
    
    class enum_SBS_SetError:
        SBS_SETERROR_SBSSE_SUCCESS = 0
        SBS_SETERROR_SBSSE_BAD_PARAMS = 1
    
        ValuesDict = {
            SBS_SETERROR_SBSSE_SUCCESS : 'SBS_SETERROR_SBSSE_SUCCESS', 
            SBS_SETERROR_SBSSE_BAD_PARAMS : 'SBS_SETERROR_SBSSE_BAD_PARAMS'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_EPSII_PDM_1.enum_SBS_SetError()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_EPSII_PDM_1.enum_SBS_SetError.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_EPSII_PDM_1.enum_SBS_SetError.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_SBS_GetError:
        SBS_GETERROR_SBSGE_SUCCESS = 0
        SBS_GETERROR_SBSGE_NVM_ERR = 1
        SBS_GETERROR_SBSGE_CONFIG_NOT_SET = 2
    
        ValuesDict = {
            SBS_GETERROR_SBSGE_SUCCESS : 'SBS_GETERROR_SBSGE_SUCCESS', 
            SBS_GETERROR_SBSGE_NVM_ERR : 'SBS_GETERROR_SBSGE_NVM_ERR', 
            SBS_GETERROR_SBSGE_CONFIG_NOT_SET : 'SBS_GETERROR_SBSGE_CONFIG_NOT_SET'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_EPSII_PDM_1.enum_SBS_GetError()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_EPSII_PDM_1.enum_SBS_GetError.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_EPSII_PDM_1.enum_SBS_GetError.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class struct_SPowerDistributionInfo:
        def __init__(self, int32__In_SysBUS_Voltage = 0, s__Out_BatRAW_Output_Sense = None, s__Out_12V_Output_Sense = None, int32__Out_12V_Output_ILimit = 0, s__Out_5V_Output1_Sense = None, int32__Out_5V_Output1_ILimit = 0, s__Out_5V_Output2_Sense = None, int32__Out_5V_Output2_ILimit = 0, s__Out_3V3_Output1_Sense = None, int32__Out_3V3_Output1_ILimit = 0, s__Out_3V3_Output2_Sense = None, int32__Out_3V3_Output2_ILimit = 0):
            self.int32__In_SysBUS_Voltage = int32__In_SysBUS_Voltage
            self.s__Out_BatRAW_Output_Sense = s__Out_BatRAW_Output_Sense
            self.s__Out_12V_Output_Sense = s__Out_12V_Output_Sense
            self.int32__Out_12V_Output_ILimit = int32__Out_12V_Output_ILimit
            self.s__Out_5V_Output1_Sense = s__Out_5V_Output1_Sense
            self.int32__Out_5V_Output1_ILimit = int32__Out_5V_Output1_ILimit
            self.s__Out_5V_Output2_Sense = s__Out_5V_Output2_Sense
            self.int32__Out_5V_Output2_ILimit = int32__Out_5V_Output2_ILimit
            self.s__Out_3V3_Output1_Sense = s__Out_3V3_Output1_Sense
            self.int32__Out_3V3_Output1_ILimit = int32__Out_3V3_Output1_ILimit
            self.s__Out_3V3_Output2_Sense = s__Out_3V3_Output2_Sense
            self.int32__Out_3V3_Output2_ILimit = int32__Out_3V3_Output2_ILimit
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__In_SysBUS_Voltage)
            
            result += self.s__Out_BatRAW_Output_Sense.serialize()
            
            result += self.s__Out_12V_Output_Sense.serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__Out_12V_Output_ILimit)
            
            result += self.s__Out_5V_Output1_Sense.serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__Out_5V_Output1_ILimit)
            
            result += self.s__Out_5V_Output2_Sense.serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__Out_5V_Output2_ILimit)
            
            result += self.s__Out_3V3_Output1_Sense.serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__Out_3V3_Output1_ILimit)
            
            result += self.s__Out_3V3_Output2_Sense.serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__Out_3V3_Output2_ILimit)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_EPSII_PDM_1.struct_SPowerDistributionInfo()
    
            currentPos = pos
            
            (resultInstance.int32__In_SysBUS_Voltage, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.s__Out_BatRAW_Output_Sense, bytesProcessed) = FP_API_EPSII_PDM_1.struct_ESEPSII_UIP.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.s__Out_12V_Output_Sense, bytesProcessed) = FP_API_EPSII_PDM_1.struct_ESEPSII_UIP.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.int32__Out_12V_Output_ILimit, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.s__Out_5V_Output1_Sense, bytesProcessed) = FP_API_EPSII_PDM_1.struct_ESEPSII_UIP.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.int32__Out_5V_Output1_ILimit, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.s__Out_5V_Output2_Sense, bytesProcessed) = FP_API_EPSII_PDM_1.struct_ESEPSII_UIP.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.int32__Out_5V_Output2_ILimit, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.s__Out_3V3_Output1_Sense, bytesProcessed) = FP_API_EPSII_PDM_1.struct_ESEPSII_UIP.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.int32__Out_3V3_Output1_ILimit, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.s__Out_3V3_Output2_Sense, bytesProcessed) = FP_API_EPSII_PDM_1.struct_ESEPSII_UIP.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.int32__Out_3V3_Output2_ILimit, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 96
    
    class enum_EDHI_ChipStatus:
        EDHI_CHIPSTATUS_EDHICS_EMDCS_UNKNOWN = 0
        EDHI_CHIPSTATUS_EDHICS_EMDCS_ONLINE = 1
        EDHI_CHIPSTATUS_EDHICS_EMDCS_COM_ERR = 2
        EDHI_CHIPSTATUS_EDHICS_EMDCS_COM_TIMEOUT = 3
        EDHI_CHIPSTATUS_EDHICS_EMDCS_DRV_DISABLED = 4
    
        ValuesDict = {
            EDHI_CHIPSTATUS_EDHICS_EMDCS_UNKNOWN : 'EDHI_CHIPSTATUS_EDHICS_EMDCS_UNKNOWN', 
            EDHI_CHIPSTATUS_EDHICS_EMDCS_ONLINE : 'EDHI_CHIPSTATUS_EDHICS_EMDCS_ONLINE', 
            EDHI_CHIPSTATUS_EDHICS_EMDCS_COM_ERR : 'EDHI_CHIPSTATUS_EDHICS_EMDCS_COM_ERR', 
            EDHI_CHIPSTATUS_EDHICS_EMDCS_COM_TIMEOUT : 'EDHI_CHIPSTATUS_EDHICS_EMDCS_COM_TIMEOUT', 
            EDHI_CHIPSTATUS_EDHICS_EMDCS_DRV_DISABLED : 'EDHI_CHIPSTATUS_EDHICS_EMDCS_DRV_DISABLED'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class struct_SGetDeviceHealthInfo:
        def __init__(self, int32__ActiveCPU_RunningTime = 0, int32__ActiveCPU_Voltage = 0, int32__ActiveCPU_Temperature = 0, int32__PCB_Temperature_1 = 0, int32__PCB_Temperature_2 = 0, int32__NVM_AllocatedSize = 0, int32__NVM_UsedSize = 0, int32__Stack_AllocatedSize = 0, int32__Stack_UsedSize = 0, e__EDHI_ChipStatus__DPOT_MCP4562_LUP_3V3_1P = 0, e__EDHI_ChipStatus__DPOT_MCP4562_LUP_3V3_1R = 0, e__EDHI_ChipStatus__DPOT_MCP4562_LUP_3V3_2P = 0, e__EDHI_ChipStatus__DPOT_MCP4562_LUP_3V3_2R = 0, e__EDHI_ChipStatus__DPOT_MCP4562_LUP_5V_1P = 0, e__EDHI_ChipStatus__DPOT_MCP4562_LUP_5V_1R = 0, e__EDHI_ChipStatus__DPOT_MCP4562_LUP_5V_2P = 0, e__EDHI_ChipStatus__DPOT_MCP4562_LUP_5V_2R = 0, e__EDHI_ChipStatus__DPOT_MCP4562_LUP_12V_P = 0, e__EDHI_ChipStatus__DPOT_MCP4562_LUP_12V_R = 0, e__EDHI_ChipStatus__DPOT_MCP4562_OUTU_12V_P = 0, e__EDHI_ChipStatus__DPOT_MCP4562_OUTU_12V_R = 0, e__EDHI_ChipStatus__GPIO_PCA9538_U1001 = 0, e__EDHI_ChipStatus__GPIO_PCA9538_U1000 = 0, e__EDHI_ChipStatus__GPIO_PCA9538_U1004 = 0, e__EDHI_ChipStatus__GPIO_PCA9538_U1011 = 0, e__EDHI_ChipStatus__INA_LUP_IN_3V3_1P = 0, e__EDHI_ChipStatus__INA_LUP_IN_3V3_1R = 0, e__EDHI_ChipStatus__INA_LUP_IN_3V3_2P = 0, e__EDHI_ChipStatus__INA_LUP_IN_3V3_2R = 0, e__EDHI_ChipStatus__INA_LUP_IN_5V_1P = 0, e__EDHI_ChipStatus__INA_LUP_IN_5V_1R = 0, e__EDHI_ChipStatus__INA_LUP_IN_5V_2P = 0, e__EDHI_ChipStatus__INA_LUP_IN_5V_2R = 0, e__EDHI_ChipStatus__INA_LUP_IN_12V_P = 0, e__EDHI_ChipStatus__INA_LUP_IN_12V_R = 0, e__EDHI_ChipStatus__TMP117_U1014 = 0, e__EDHI_ChipStatus__TMP117_U1031 = 0):
            self.int32__ActiveCPU_RunningTime = int32__ActiveCPU_RunningTime
            self.int32__ActiveCPU_Voltage = int32__ActiveCPU_Voltage
            self.int32__ActiveCPU_Temperature = int32__ActiveCPU_Temperature
            self.int32__PCB_Temperature_1 = int32__PCB_Temperature_1
            self.int32__PCB_Temperature_2 = int32__PCB_Temperature_2
            self.int32__NVM_AllocatedSize = int32__NVM_AllocatedSize
            self.int32__NVM_UsedSize = int32__NVM_UsedSize
            self.int32__Stack_AllocatedSize = int32__Stack_AllocatedSize
            self.int32__Stack_UsedSize = int32__Stack_UsedSize
            self.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_3V3_1P = e__EDHI_ChipStatus__DPOT_MCP4562_LUP_3V3_1P
            self.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_3V3_1R = e__EDHI_ChipStatus__DPOT_MCP4562_LUP_3V3_1R
            self.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_3V3_2P = e__EDHI_ChipStatus__DPOT_MCP4562_LUP_3V3_2P
            self.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_3V3_2R = e__EDHI_ChipStatus__DPOT_MCP4562_LUP_3V3_2R
            self.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_5V_1P = e__EDHI_ChipStatus__DPOT_MCP4562_LUP_5V_1P
            self.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_5V_1R = e__EDHI_ChipStatus__DPOT_MCP4562_LUP_5V_1R
            self.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_5V_2P = e__EDHI_ChipStatus__DPOT_MCP4562_LUP_5V_2P
            self.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_5V_2R = e__EDHI_ChipStatus__DPOT_MCP4562_LUP_5V_2R
            self.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_12V_P = e__EDHI_ChipStatus__DPOT_MCP4562_LUP_12V_P
            self.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_12V_R = e__EDHI_ChipStatus__DPOT_MCP4562_LUP_12V_R
            self.e__EDHI_ChipStatus__DPOT_MCP4562_OUTU_12V_P = e__EDHI_ChipStatus__DPOT_MCP4562_OUTU_12V_P
            self.e__EDHI_ChipStatus__DPOT_MCP4562_OUTU_12V_R = e__EDHI_ChipStatus__DPOT_MCP4562_OUTU_12V_R
            self.e__EDHI_ChipStatus__GPIO_PCA9538_U1001 = e__EDHI_ChipStatus__GPIO_PCA9538_U1001
            self.e__EDHI_ChipStatus__GPIO_PCA9538_U1000 = e__EDHI_ChipStatus__GPIO_PCA9538_U1000
            self.e__EDHI_ChipStatus__GPIO_PCA9538_U1004 = e__EDHI_ChipStatus__GPIO_PCA9538_U1004
            self.e__EDHI_ChipStatus__GPIO_PCA9538_U1011 = e__EDHI_ChipStatus__GPIO_PCA9538_U1011
            self.e__EDHI_ChipStatus__INA_LUP_IN_3V3_1P = e__EDHI_ChipStatus__INA_LUP_IN_3V3_1P
            self.e__EDHI_ChipStatus__INA_LUP_IN_3V3_1R = e__EDHI_ChipStatus__INA_LUP_IN_3V3_1R
            self.e__EDHI_ChipStatus__INA_LUP_IN_3V3_2P = e__EDHI_ChipStatus__INA_LUP_IN_3V3_2P
            self.e__EDHI_ChipStatus__INA_LUP_IN_3V3_2R = e__EDHI_ChipStatus__INA_LUP_IN_3V3_2R
            self.e__EDHI_ChipStatus__INA_LUP_IN_5V_1P = e__EDHI_ChipStatus__INA_LUP_IN_5V_1P
            self.e__EDHI_ChipStatus__INA_LUP_IN_5V_1R = e__EDHI_ChipStatus__INA_LUP_IN_5V_1R
            self.e__EDHI_ChipStatus__INA_LUP_IN_5V_2P = e__EDHI_ChipStatus__INA_LUP_IN_5V_2P
            self.e__EDHI_ChipStatus__INA_LUP_IN_5V_2R = e__EDHI_ChipStatus__INA_LUP_IN_5V_2R
            self.e__EDHI_ChipStatus__INA_LUP_IN_12V_P = e__EDHI_ChipStatus__INA_LUP_IN_12V_P
            self.e__EDHI_ChipStatus__INA_LUP_IN_12V_R = e__EDHI_ChipStatus__INA_LUP_IN_12V_R
            self.e__EDHI_ChipStatus__TMP117_U1014 = e__EDHI_ChipStatus__TMP117_U1014
            self.e__EDHI_ChipStatus__TMP117_U1031 = e__EDHI_ChipStatus__TMP117_U1031
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__ActiveCPU_RunningTime)
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__ActiveCPU_Voltage)
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__ActiveCPU_Temperature)
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__PCB_Temperature_1)
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__PCB_Temperature_2)
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__NVM_AllocatedSize)
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__NVM_UsedSize)
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__Stack_AllocatedSize)
            
            result += SerDesHelpers.serdesType_basic.serialize("int32", self.int32__Stack_UsedSize)
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_3V3_1P).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_3V3_1R).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_3V3_2P).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_3V3_2R).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_5V_1P).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_5V_1R).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_5V_2P).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_5V_2R).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_12V_P).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_12V_R).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__DPOT_MCP4562_OUTU_12V_P).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__DPOT_MCP4562_OUTU_12V_R).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__GPIO_PCA9538_U1001).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__GPIO_PCA9538_U1000).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__GPIO_PCA9538_U1004).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__GPIO_PCA9538_U1011).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__INA_LUP_IN_3V3_1P).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__INA_LUP_IN_3V3_1R).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__INA_LUP_IN_3V3_2P).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__INA_LUP_IN_3V3_2R).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__INA_LUP_IN_5V_1P).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__INA_LUP_IN_5V_1R).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__INA_LUP_IN_5V_2P).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__INA_LUP_IN_5V_2R).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__INA_LUP_IN_12V_P).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__INA_LUP_IN_12V_R).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__TMP117_U1014).serialize()
            
            result += FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus(self.e__EDHI_ChipStatus__TMP117_U1031).serialize()
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_EPSII_PDM_1.struct_SGetDeviceHealthInfo()
    
            currentPos = pos
            
            (resultInstance.int32__ActiveCPU_RunningTime, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.int32__ActiveCPU_Voltage, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.int32__ActiveCPU_Temperature, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.int32__PCB_Temperature_1, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.int32__PCB_Temperature_2, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.int32__NVM_AllocatedSize, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.int32__NVM_UsedSize, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.int32__Stack_AllocatedSize, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.int32__Stack_UsedSize, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_3V3_1P, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_3V3_1R, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_3V3_2P, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_3V3_2R, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_5V_1P, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_5V_1R, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_5V_2P, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_5V_2R, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_12V_P, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__DPOT_MCP4562_LUP_12V_R, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__DPOT_MCP4562_OUTU_12V_P, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__DPOT_MCP4562_OUTU_12V_R, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__GPIO_PCA9538_U1001, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__GPIO_PCA9538_U1000, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__GPIO_PCA9538_U1004, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__GPIO_PCA9538_U1011, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__INA_LUP_IN_3V3_1P, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__INA_LUP_IN_3V3_1R, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__INA_LUP_IN_3V3_2P, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__INA_LUP_IN_3V3_2R, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__INA_LUP_IN_5V_1P, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__INA_LUP_IN_5V_1R, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__INA_LUP_IN_5V_2P, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__INA_LUP_IN_5V_2R, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__INA_LUP_IN_12V_P, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__INA_LUP_IN_12V_R, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__TMP117_U1014, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__EDHI_ChipStatus__TMP117_U1031, bytesProcessed) = FP_API_EPSII_PDM_1.enum_EDHI_ChipStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 64
    
    class struct_SResetBootLdrErrCounters:
        def __init__(self, uint16__c_app_restart_errosrs = 0, uint8__g_pAppCyclesErrors = 0, uint8__reserved = 0, uint16__g_pIntegrityCheckStates = 0):
            self.uint16__c_app_restart_errosrs = uint16__c_app_restart_errosrs
            self.uint8__g_pAppCyclesErrors = uint8__g_pAppCyclesErrors
            self.uint8__reserved = uint8__reserved
            self.uint16__g_pIntegrityCheckStates = uint16__g_pIntegrityCheckStates
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__c_app_restart_errosrs)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__g_pAppCyclesErrors)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__reserved)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__g_pIntegrityCheckStates)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_EPSII_PDM_1.struct_SResetBootLdrErrCounters()
    
            currentPos = pos
            
            (resultInstance.uint16__c_app_restart_errosrs, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__g_pAppCyclesErrors, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__reserved, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__g_pIntegrityCheckStates, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 6
    
    class struct_SMSP_Exception:
        def __init__(self, uint16__m_nFileID = 0, uint16__m_nLineNum = 0):
            self.uint16__m_nFileID = uint16__m_nFileID
            self.uint16__m_nLineNum = uint16__m_nLineNum
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__m_nFileID)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__m_nLineNum)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_EPSII_PDM_1.struct_SMSP_Exception()
    
            currentPos = pos
            
            (resultInstance.uint16__m_nFileID, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__m_nLineNum, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 4
    

    ############################################################################################################
    """
    Request function for FIDL method: GetDeviceInfo
        - function ID: 00000001
        - description: Get basic device information: device type, serial number, current operational mode, software version, etc.
    """
    def req_GetDeviceInfo(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000001
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000001, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: GetDeviceInfo
        - function ID: 00000001
        - description: Get basic device information: device type, serial number, current operational mode, software version, etc.
    """
    def resp_GetDeviceInfo(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000001):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
        responseInstance["uint16__ModuleTypeID"] = field
        currentPos += bytesProcessed
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
        responseInstance["uint8__string__ModuleTypeSize"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = SerDesHelpers.serdesType_string.deserialize(data, currentPos, 20)
        responseInstance["string__ModuleType"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
        responseInstance["uint16__ModuleHWVersion"] = field
        currentPos += bytesProcessed
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
        responseInstance["uint8__string__DeviceSerialNumberSize"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = SerDesHelpers.serdesType_string.deserialize(data, currentPos, 30)
        responseInstance["string__DeviceSerialNumber"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_EPSII_PDM_1.enum_ESDI_FirmwareType.deserialize(data, currentPos)
        responseInstance["e__ESDI_FirmwareType__FWTypeID"] = field
        currentPos += bytesProcessed
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
        responseInstance["uint8__string__FWTypeSize"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = SerDesHelpers.serdesType_string.deserialize(data, currentPos, 20)
        responseInstance["string__FWType"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
        responseInstance["uint16__FWVersionMaj"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
        responseInstance["uint16__FWVersionMin"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: GetPowerDistributionInfo
        - function ID: 00000002
        - description: Get current U/I/P and current (I) limit for all output channels
    """
    def req_GetPowerDistributionInfo(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
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
    Response function for FIDL method: GetPowerDistributionInfo
        - function ID: 00000002
        - description: Get current U/I/P and current (I) limit for all output channels
    """
    def resp_GetPowerDistributionInfo(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000002):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_EPSII_PDM_1.struct_SPowerDistributionInfo.deserialize(data, currentPos)
        responseInstance["s__PowerDistributionInfo"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: GetDeviceHealthInfo
        - function ID: 00000003
        - description: Get information about all chip statuses (driver state) and CPU temperature, voltage and running time
    """
    def req_GetDeviceHealthInfo(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000003
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000003, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: GetDeviceHealthInfo
        - function ID: 00000003
        - description: Get information about all chip statuses (driver state) and CPU temperature, voltage and running time
    """
    def resp_GetDeviceHealthInfo(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000003):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_EPSII_PDM_1.struct_SGetDeviceHealthInfo.deserialize(data, currentPos)
        responseInstance["s__GetDeviceHealthInfo"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: SetPC104GPIO
        - function ID: 00000004
        - description: Set PC104GPIO outputs with mask. Refer to the description for ConOps operation
    """
    def req_SetPC104GPIO(self, e__SGGPIO_Bitmask__FilterMask, e__SGGPIO_OnOff_mask__ValuesMaskReq):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000004
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_EPSII_PDM_1.enum_SGGPIO_Bitmask(e__SGGPIO_Bitmask__FilterMask).serialize()
        requestBytes += FP_API_EPSII_PDM_1.enum_SGGPIO_OnOff_mask(e__SGGPIO_OnOff_mask__ValuesMaskReq).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000004, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: SetPC104GPIO
        - function ID: 00000004
        - description: Set PC104GPIO outputs with mask. Refer to the description for ConOps operation
    """
    def resp_SetPC104GPIO(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000004):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_EPSII_PDM_1.enum_SGGPIO_SetError.deserialize(data, currentPos)
        responseInstance["e__SGGPIO_SetError__Err"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: GetPC104GPIO
        - function ID: 00000005
        - description: Get current GPIO outputs. The value returned may be different from the last SetPC104GPIO call.
    """
    def req_GetPC104GPIO(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000005
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000005, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: GetPC104GPIO
        - function ID: 00000005
        - description: Get current GPIO outputs. The value returned may be different from the last SetPC104GPIO call.
    """
    def resp_GetPC104GPIO(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000005):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
        responseInstance["uint8__CurrentValues"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: GetRAWSensors
        - function ID: 00000006
        - description: Get RAW sensor values by ID. Up to 50 (out of 53) different sensor values may be got.
    """
    def req_GetRAWSensors(self, uint32__PktIDReq, a__e__ESEPSII_PDM_SensorIDs__50__SensorsIDs):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000006
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint32", uint32__PktIDReq)
        actualLen = len(a__e__ESEPSII_PDM_SensorIDs__50__SensorsIDs)
    
        if (actualLen > 50):
            raise Exception("The maximum expected size for array argument a__e__ESEPSII_PDM_SensorIDs__50__SensorsIDs is 50 bytes but " + str(actualLen) + " bytes were provided.")
        requestBytes += SerDesHelpers.serdesType_customTypeArray.serialize(a__e__ESEPSII_PDM_SensorIDs__50__SensorsIDs, 50)
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000006, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: GetRAWSensors
        - function ID: 00000006
        - description: Get RAW sensor values by ID. Up to 50 (out of 53) different sensor values may be got.
    """
    def resp_GetRAWSensors(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000006):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
        responseInstance["uint32__PktID"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = SerDesHelpers.serdesType_basicArray.deserialize("int32", data, currentPos, 50)
        responseInstance["a__int32__50__SensorValues"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: SetPowerOutputs
        - function ID: 00000007
        - description: Switches on/off the different power output channels of the device. Refer to the description for ConOps operation.
    """
    def req_SetPowerOutputs(self, e__SGPO_Bitmask__FilterMask, e__SGPO_ON_Off_Bitmask__ValuesMask):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000007
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_EPSII_PDM_1.enum_SGPO_Bitmask(e__SGPO_Bitmask__FilterMask).serialize()
        requestBytes += FP_API_EPSII_PDM_1.enum_SGPO_ON_Off_Bitmask(e__SGPO_ON_Off_Bitmask__ValuesMask).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000007, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: SetPowerOutputs
        - function ID: 00000007
        - description: Switches on/off the different power output channels of the device. Refer to the description for ConOps operation.
    """
    def resp_SetPowerOutputs(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000007):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_EPSII_PDM_1.enum_SGPO_SetError.deserialize(data, currentPos)
        responseInstance["e__SGPO_SetError__Err"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: GetPowerOutputs
        - function ID: 00000008
        - description: Get currently enabled power channels. The value returned may be different from the last SetPowerOutputs call.
    """
    def req_GetPowerOutputs(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
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
    Response function for FIDL method: GetPowerOutputs
        - function ID: 00000008
        - description: Get currently enabled power channels. The value returned may be different from the last SetPowerOutputs call.
    """
    def resp_GetPowerOutputs(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000008):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
        responseInstance["uint32__ValuesMask"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: SetBasicSettings
        - function ID: 00000009
        - description: The main and only device operation configuration.
    """
    def req_SetBasicSettings(self, s__BasicSettings):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000009
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__BasicSettings.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000009, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: SetBasicSettings
        - function ID: 00000009
        - description: The main and only device operation configuration.
    """
    def resp_SetBasicSettings(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000009):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_EPSII_PDM_1.enum_SBS_SetError.deserialize(data, currentPos)
        responseInstance["e__SBS_SetError__Err"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: GetBasicSettings
        - function ID: 0000000A
        - description: Read default settings
    """
    def req_GetBasicSettings(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000000A
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000000A, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: GetBasicSettings
        - function ID: 0000000A
        - description: Read default settings
    """
    def resp_GetBasicSettings(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000A):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_EPSII_PDM_1.enum_SBS_GetError.deserialize(data, currentPos)
        responseInstance["e__SBS_GetError__Err"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_EPSII_PDM_1.struct_SBasicSettings.deserialize(data, currentPos)
        responseInstance["s__BasicSettings"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: GetFailSafeExceptions
        - function ID: 0000000B
        - description: Get last 16 ASSERT fails
    """
    def req_GetFailSafeExceptions(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000000B
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000000B, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: GetFailSafeExceptions
        - function ID: 0000000B
        - description: Get last 16 ASSERT fails
    """
    def resp_GetFailSafeExceptions(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000B):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_customTypeArray.deserialize(FP_API_EPSII_PDM_1.struct_SMSP_Exception, data, currentPos, 16)
        responseInstance["a__s__16__exceptions"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: GetFailSafeErrCounters
        - function ID: 0000000C
        - description: Counters for different diagnostic parameters
    """
    def req_GetFailSafeErrCounters(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000000C
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000000C, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: GetFailSafeErrCounters
        - function ID: 0000000C
        - description: Counters for different diagnostic parameters
    """
    def resp_GetFailSafeErrCounters(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000C):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basicArray.deserialize("uint16", data, currentPos, 123)
        responseInstance["a__uint16__123__errorCounters"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: GetMainAppExceptions
        - function ID: 0000000D
        - description: Get last 16 ASSERT fails
    """
    def req_GetMainAppExceptions(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000000D
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000000D, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: GetMainAppExceptions
        - function ID: 0000000D
        - description: Get last 16 ASSERT fails
    """
    def resp_GetMainAppExceptions(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000D):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_customTypeArray.deserialize(FP_API_EPSII_PDM_1.struct_SMSP_Exception, data, currentPos, 16)
        responseInstance["a__s__16__exceptions"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: GetMainAppErrCounters
        - function ID: 0000000E
        - description: Counters for different diagnostic parameters
    """
    def req_GetMainAppErrCounters(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000000E
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000000E, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: GetMainAppErrCounters
        - function ID: 0000000E
        - description: Counters for different diagnostic parameters
    """
    def resp_GetMainAppErrCounters(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000E):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basicArray.deserialize("uint16", data, currentPos, 123)
        responseInstance["a__uint16__123__errorCounters"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: OnESCP_ResetMainAppErrCounters
        - function ID: 0000000F
        - description: Clear all error counters in the Main application
    """
    def req_OnESCP_ResetMainAppErrCounters(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000000F
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000000F, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: OnESCP_ResetMainAppErrCounters
        - function ID: 0000000F
        - description: Clear all error counters in the Main application
    """
    def resp_OnESCP_ResetMainAppErrCounters(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000F):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
        responseInstance["bool__result"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: OnESCP_ResetMainAppExceptions
        - function ID: 00000010
        - description: Clear all excetipons in the Main application
    """
    def req_OnESCP_ResetMainAppExceptions(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000010
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000010, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: OnESCP_ResetMainAppExceptions
        - function ID: 00000010
        - description: Clear all excetipons in the Main application
    """
    def resp_OnESCP_ResetMainAppExceptions(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000010):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
        responseInstance["bool__result"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: OnESCP_ResetFailAppErrCounters
        - function ID: 00000011
        - description: Clear all error counters in the Fail safe application
    """
    def req_OnESCP_ResetFailAppErrCounters(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000011
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000011, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: OnESCP_ResetFailAppErrCounters
        - function ID: 00000011
        - description: Clear all error counters in the Fail safe application
    """
    def resp_OnESCP_ResetFailAppErrCounters(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000011):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
        responseInstance["bool__result"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: OnESCP_ResetFailAppExceptions
        - function ID: 00000012
        - description: Clear all exceptions in the Fail safe application
    """
    def req_OnESCP_ResetFailAppExceptions(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000012
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000012, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: OnESCP_ResetFailAppExceptions
        - function ID: 00000012
        - description: Clear all exceptions in the Fail safe application
    """
    def resp_OnESCP_ResetFailAppExceptions(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000012):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
        responseInstance["bool__result"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: GetBulkTelemetry
        - function ID: 00000013
        - description: Clear all exceptions in the Fail safe application
    """
    def req_GetBulkTelemetry(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000013
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000013, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: GetBulkTelemetry
        - function ID: 00000013
        - description: Clear all exceptions in the Fail safe application
    """
    def resp_GetBulkTelemetry(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000013):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
        responseInstance["uint8__conOpsMode"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
        responseInstance["uint8__GPIOStates"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
        responseInstance["uint32__powerOutputsStates"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_EPSII_PDM_1.struct_SPowerDistributionInfo.deserialize(data, currentPos)
        responseInstance["s__PowerDistributionInfo"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_EPSII_PDM_1.struct_SGetDeviceHealthInfo.deserialize(data, currentPos)
        responseInstance["s__GetDeviceHealthInfo"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_EPSII_PDM_1.struct_SResetBootLdrErrCounters.deserialize(data, currentPos)
        responseInstance["s__ResetBootLdrErrCounters"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ResetDevice
        - function ID: 00000020
        - description: Reset device in same mode (main/failsafe) as it is at the time command is received.
    """
    def req_ResetDevice(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000020
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000020, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ResetDevice
        - function ID: 00000020
        - description: Reset device in same mode (main/failsafe) as it is at the time command is received.
    """
    def resp_ResetDevice(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000020):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
        responseInstance["bool__result"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ForceInstallMainApp
        - function ID: 00000021
        - description: Restart and install main application. This command may be initiated to switch from failsafe application operation to main.
    """
    def req_ForceInstallMainApp(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000021
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000021, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ForceInstallMainApp
        - function ID: 00000021
        - description: Restart and install main application. This command may be initiated to switch from failsafe application operation to main.
    """
    def resp_ForceInstallMainApp(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000021):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
        responseInstance["bool__result"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ForceInstallFailSafeApp
        - function ID: 00000022
        - description: Restart and install failsafe application.
    """
    def req_ForceInstallFailSafeApp(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000022
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000022, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ForceInstallFailSafeApp
        - function ID: 00000022
        - description: Restart and install failsafe application.
    """
    def resp_ForceInstallFailSafeApp(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000022):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
        responseInstance["bool__result"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: GetBootLoaderErrCounters
        - function ID: 00000023
        - description: Get the values of the error counters of the bootloader about the App fails to run
    """
    def req_GetBootLoaderErrCounters(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000023
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000023, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: GetBootLoaderErrCounters
        - function ID: 00000023
        - description: Get the values of the error counters of the bootloader about the App fails to run
    """
    def resp_GetBootLoaderErrCounters(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000023):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_EPSII_PDM_1.struct_SResetBootLdrErrCounters.deserialize(data, currentPos)
        responseInstance["s__ResetBootLdrErrCounters"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ResetBootLdrErrCounters
        - function ID: 00000024
        - description: Clear the values of the error counters of the bootloader about the App fails to run
    """
    def req_ResetBootLdrErrCounters(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_EPSII_PDM_1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000024
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000024, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ResetBootLdrErrCounters
        - function ID: 00000024
        - description: Clear the values of the error counters of the bootloader about the App fails to run
    """
    def resp_ResetBootLdrErrCounters(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000024):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_EPSII_PDM_1.struct_SResetBootLdrErrCounters.deserialize(data, currentPos)
        responseInstance["s__ResetBootLdrErrCounters"] = field
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

            if fpHeaderInstance.u16ProtoId != self.const_EPSII_PDM_1_PROTOCOL_ID:
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

