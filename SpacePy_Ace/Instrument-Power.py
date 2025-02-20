"""
Created on Feb 20 2025

@author: Ace Stratton

This is intended to quickly power on and off our instruments
"""


#import sys

from PDMInterface import PDMSetPower



def InstrumentPower(Inst, Mode):
    #Inst must be set to "M" = meddea or "S" = SHARP
    #Mode 1=On 0=Off

    if Inst == "M":
        if Inst == '1':

            PDMSetPower(12, 'Power1', 'ON')

            

