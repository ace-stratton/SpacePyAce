# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 2024

@author: Ace Stratton

This file will handle all BP Interactions
"""

import sys
sys.path.insert(0, 'C:/Users/user/Desktop/SpacePy_Ace/fidl')
from EPSII_BP_1ClientApp import FP_API_EPSII_BP_1
import Interface

api = FP_API_EPSII_BP_1
moduleMac = 102

def getDeviceInfo():
    payloadBytes = api.req_GetDeviceInfo()
    out1 = Interface.getReturn(payloadBytes, moduleMac, api)
    results = vars(out1["s__GetDeviceInfo"])
    print(results)
    
    return(results)