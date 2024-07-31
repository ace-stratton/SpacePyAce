# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 10:03:42 2024

@author: Ace
"""

from module_ace import ace_test

import time, sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, 'C:/Users/user/Desktop/SpacePy_Ace/eload_ctrl')
from eLoadControl import eLoad

t = []
bV = []
bI = []
ConOpsMode = 4
BattV = 17000

eLoad('on')
#while ConOpsMode == 4:
for i in range(3):
	
	# Battery 
	BattInfo = ace_test("GetBatteryInfo", "FP_API_EPSII_BP_1")
	ConOpsMode = BattInfo['uint8__nConOpsMode']
	
	if ConOpsMode == 1:
		break
	
	BattV = BattInfo['int64__BattVoltage']
	BattI = BattInfo['int64__BattCurrent']
	
	bV.append(BattV)
	bI.append(BattI)
	
	print(ConOpsMode, BattV, BattI)
	
	# Time
	TimeOut = ace_test("UpTime", "FP_API_OBC")
	upTime = TimeOut["uint32__uptime"]
	timeSeconds = upTime
	t.append(timeSeconds)
	
	time.sleep(60)
	
print('Done')
eLoad('off')

saveArray = np.array([t, bV, bI])
fileName = 'BatteryDrainCurve_Eclipse_NoSPInput.csv'
np.savetxt(fileName, saveArray, delimiter=',') 

# plotting 

fig, ax1 = plt.subplots()
color = 'tab:blue'
ax1.set_xlabel('time (s)')
ax1.set_title('Battery Drain Curve Eclipse Mode')
ax1.set_ylabel('Voltage (mV)', color=color)
ax1.plot(t,bV)
ax1.tick_params(axis = 'y', labelcolor=color)


ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Current (mA)', color=color)
ax2.plot(t, bI, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()
fig.savefig('BatteryDrainCurvePerc_Eclipse_NoSPInput.png', dpi=300)


#plotting depth of discharge versus voltage and current

# Calculating Depth Of Discharge
tHours = (saveArray[0, :])/60/60 #seconds to hours
tHours = tHours-(tHours[1])
Volts = (saveArray[1, :])*(10**-3) #Volts
Amps = abs((saveArray[2, :])*(10**-3)) #Amps
WhFull = 84 #Wh

Wh = tHours*Volts*Amps
leng = len(Amps)

DrainPerc =(1-((WhFull-Wh)/WhFull))*100

fig2, ax3 = plt.subplots()

color = 'tab:blue'
ax3.set_xlabel('Drainage Percent')
ax3.set_title('Battery Drain Curve Idle Mode')
ax3.set_ylabel('Voltage (mV)', color=color)
ax3.plot(DrainPerc[2:-2],bV[2:-2])
ax3.tick_params(axis = 'y', labelcolor=color)

ax4 = ax3.twinx()
color = 'tab:red'
ax4.set_ylabel('Current (mA)', color=color)
ax4.plot(DrainPerc[2:-2], bI[2:-2], color=color)
ax4.tick_params(axis='y', labelcolor=color)

fig2.tight_layout()
plt.show()
fig2.savefig('BatteryDrainCurvePerc_SciMode_NoSPInput.png', dpi=300)
