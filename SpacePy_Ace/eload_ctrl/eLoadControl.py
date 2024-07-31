''' Chroma Systems Solutions, Inc. 2023

    Class to instantiate a Chroma_62000D object to remote control using the
    PyVISA module library through the "Class_PyVISA.py" custom Python class file.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.'''

from Class_Chroma_62000D import *

def eLoad(state):
	''' ########## BEGIN SETTINGS TO CONFIGURE ########## '''
	import numpy as np 
	import os
	import pathlib
	''' TEST CONTROL SETTINGS '''

	ResourceName = "USB0::0x0A69::0x0880::630031500518::INSTR" # VISA Resource Name string to communicate with the tester (e.g. "GPIB0::12::INSTR")
	ResourceName2 = "USB0::0x0A69::0x0880::630031500381::INSTR"
	BaudRate = 9600
	StopBits = 10 # 10 = 1; 15 = 1.5; 20 = 2

	LogLevel = 0 # (0 = No logging; 1: Create log text file only; 2: Create log text file and display logs in console)
	DCSupply = Chroma_62000D(LogLevel) # Instantiate the tester as an object
	DCSupply2 = Chroma_62000D(LogLevel) #5V line
	if not DCSupply.SetBaudRate(BaudRate): # Set the Baud Rate value
		return
	if not DCSupply2.SetBaudRate(BaudRate): # Set the Baud Rate value
		return
	if not DCSupply.SetStopBits(StopBits):
		return
	if not DCSupply2.SetStopBits(StopBits):
		return
	if DCSupply.Connect(ResourceName) == False:
		DCSupply.Log ("Could not connect properly to Chroma 62000D") # Could not connect properly...
		return
	if DCSupply2.Connect(ResourceName2) == False:
		DCSupply2.Log ("Could not connect properly to Chroma 62000D") # Could not connect properly...
		return

	DCSupply.ClearStatus() # Clear the error queue and other status registers
	DCSupply.GetAllSystemErrors() # Check if there are any System Errors reported (it shouldn't be since the ClearStatus function was used above)

	DCSupply2.ClearStatus() # Clear the error queue and other status registers
	DCSupply2.GetAllSystemErrors() # Check if there are any System Errors reported (it shouldn't be since the ClearStatus function was used above)

    # ******** IMPORTANT NOTE: ********
    # TO AVOID TURNING ON THE LOAD STATE WHEN THE CODE IS EXECUTED
    # PLEASE CONFIGURE THE DC LOAD AND MAKE SURE IS SAFE TO
    # INPUT POWER BEFORE ENABLING THE FOLLOWING FUNCTIONS TO
    # ENABLE THE DC SUPPLY STATE.
    # MORE FUNCTIONS WOULD BE REQUIRED TO BE INCLUDED IN THE SOURCE
    # CODE FOR THE Chroma_62000d_Class.py file TO CONFIGURE THE DC
    # OUTPUT SETTINGS.

	''' Charge / Discharge Routine 
	1- Discharge the battery at 5 A constant  until voltage drops to 24.2 V
	2- Once V = 24.2, start charging the battery at 28.8V @ 45 A
    3- Once V= 28.8 and I= 4A, start discharging fase again at 5 A constant
    4- Repeat cycle'''

	#print("------------------------------ Starting 'Charge and Discharge Routine' ------------------------------ ")
	#print("------------------------------ Press Ctrl + C to stop the execution of the Python example ------------------------------ ")

    

	DCSupply.SendCommand("SYSTEM:MODE LOAD") #12V
	DCSupply2.SendCommand("SYSTEM:MODE LOAD") #5V

	vCurr = 0.952 #12V
	VCurr2 = 0.771 #5V
    
	try:


		DCSupply.SendCommand("CURR:STAT:L1 " + str(vCurr))
		DCSupply2.SendCommand("CURR:STAT:L1 " + str(VCurr2))
						
		if state == 'on':
			DCSupply2.SendCommand("LOAD ON")
			DCSupply.SendCommand("LOAD ON")
			print("------------------------------ Loads On ------------------------------ ")
		
		elif state == 'off':
			DCSupply2.SendCommand("LOAD OFF")
			DCSupply.SendCommand("LOAD OFF")
			print("------------------------------ Loads Off ------------------------------ ")
		else:
			print('invalid input')


		DCSupply.SendCommand("CONFigure:OUTPut OFF")
	except Exception as Ex: 
		print("An Exception occurred: " + str(Ex))

# Execute the main application

