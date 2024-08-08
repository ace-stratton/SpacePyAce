# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 01:09:32 2024

@author: user
"""

import sys
sys.path.insert(0,'C:/Users/user/Desktop/SpacePy_Ace/Performance Check')
import OBC
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

#assert out1 == currentTime

out2 = OBC.getDate()
print(out2)

Day = currentTime.day
Month = currentTime.month
Year = currentTime.year
checkDate = [Day, Month, Year]

assert out2 == checkDate
