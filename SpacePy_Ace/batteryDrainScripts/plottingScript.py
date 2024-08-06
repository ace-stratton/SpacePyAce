# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 13:30:46 2024

@author: user
"""
import pandas as pd
import matplotlib.pyplot as plt


saveArray = pd.DataFrame.to_numpy(pd.read_csv('ScienceModeDrain_NoSolarInput.csv', header=None))

bV = saveArray[1,:]
bI = saveArray[2,:]

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

