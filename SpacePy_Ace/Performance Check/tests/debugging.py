# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 01:09:32 2024

@author: user
"""

import sys
sys.path.insert(0,'C:/Users/user/Desktop/SpacePy_Ace/Performance Check')
import OBC, PDM
from datetime import datetime


out = OBC.getVersion()

assert out != [99,99,99]


out1 = OBC.getTime()
currentTime = datetime.now()

Hour = currentTime.hour
Min = currentTime.minute
Sec = currentTime.second

checkTime = [Hour, Min, Sec]
print(checkTime)
print(out1)

#assert out1 == checkTime

out2 = OBC.getDate()
print(out2)

Day = currentTime.day
Month = currentTime.month
Year = currentTime.year
checkDate = [Day, Month, Year]

assert out2 == checkDate


out3 = PDM.getPDMHealthInfo('else')
out4 = vars(out3['e__EDHI_ChipStatus__DPOT_MCP4562_LUP_3V3_1R'])
out5 = out4['value']

print(out3)

