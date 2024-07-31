'''
    =============================================================================
    Chroma Systems Solutions, Inc. 2023

    Class to instantiate a Chroma_62000D object to remote control using the
    PyVISA module library through the "Class_PyVISA.py" custom Python class file.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    =============================================================================
'''

from Class_PyVISA import *

class Chroma_62000D(Chroma_PyVISA):
    __ObjectDescription = "Chroma 62000D"

    # Generic Private attributes (do not change)
    __Manufacturer = "Chroma" # Manufacturer supported
    __Identificator = ["63003-150-40","62120D-100","62180D-100","62060D-600","62120D-600","62180D-600","62180D-1200","62120D-1200","62180D-1800"] # Model numbers supported
    __ObjectDescription = "Chroma 62000D Programmable Bidirectional DC Power Supply"
    __PerformFinalizing = False

    
    # Constructor
    def __init__(self, LogLevel=1):
        try:
            super().__init__(LogLevel, "Chroma_62000D")
            self.Log(self.__ObjectDescription + " object instantiated successfully.")
            pass
        except Exception as Ex:
            self.Log("An Exception occurred while trying to instantiate the " + self.__ObjectDescription + " object: " + str(Ex))
            return

    # Destructor
    def __del__(self):
        try:
            super().__del__()
            return
        except Exception as Ex:
            self.Log("An Exception occurred while trying to destroy the " + self.__ObjectDescription + " object: " + str(Ex))
            return

    # Connect
    def Connect(self, Param1, Param2 = None):
        try:
            if super().Connect(Param1, Param2):
                if (self.__Manufacturer.upper() in self.Manufacturer.upper() and self.ModelNumber.upper() in self.__Identificator):
                    self.Log("Connected to " + self.Manufacturer + " " + self.ModelNumber + " [S/N: " + self.SerialNumber + "]")
                    if self.__Initializing():
                        return True
                    else:
                        self.Disconnect()
                        return False
                else:
                    self.Log("The instrument identified as " + self.Manufacturer + " " + self.ModelNumber + " is not supported by this application.")
                    self.Disconnect()
                    return False
            else:
                self.Log("Could not connect successfully. For more information, refer to the Log created if this function is enabled.")
                return False
        #except ValueError:
        #   self.Log("A Value Error occurred while trying to connect to the " + self.__ObjectDescription)
        #  return False
        except Exception as Ex:
            self.Log("An Exception occurred while trying to connect to the " + self.__ObjectDescription + ": " + str(Ex))
            return False

    # Disconnect
    def Disconnect(self):
        self.__Finalizing()
        return super().Disconnect()


    ''' ############ PRIVATE FUNCTIONS ############ '''
    ''' ############ PRIVATE GENERIC FUNCTIONS ############ '''



    ''' ############ PRIVATE CHROMA 62000D FUNCTIONS ############ '''

    # Private function to perform all tasks required after connecting
    def __Initializing(self):
        try:
            # Program the tasks to be performed at Initialization
            self.Log ("Initializing...")
            self.ClearStatus()
            self.GetAllSystemErrors()

            InstrumentModelNumber = self.ModelNumber
            self.Log ("Initializing routine performed successfully.")
            self.__PerformFinalizing = True
            return True
        except Exception as Ex:
            self.Log("An Exception occurred while trying to perform the Initializing tasks: " + str(Ex))
            return False

    # Private function to perform all tasks required before disconnecting
    def __Finalizing(self):
        try:
            # Program all tasks to be performed at Finalization
            if self.__PerformFinalizing == False: # If there is a different instrument connected, we do not execute the code from here
                return True
            self.Log ("Finalizing...")
            self.GetAllSystemErrors() # Clear the error queue

            self.Log ("Finalizing routine performed successfully.")
            return True
        except Exception as Ex:
            self.Log ("An exception occurred while trying to perform the Finalizing tasks: " + str(Ex))
            return False

    

    ''' ############ PUBLIC FUNCTIONS ############ '''
    ''' ############ PUBLIC GENERIC FUNCTIONS ############ '''


    ''' ############ PUBLIC CHROMA 62000D FUNCTIONS ############ '''

    # Save the working memory to a specific memory location number

    # Start OUTPUT
    def Output_Start(self):
        try:
            if self.GetAllSystemErrors() > 0:
                self.Log ("Did not start the test due to several System Errors reported.")
                return False
            self.SendCommand("CONF:OUTP ON")
            return True
        except Exception as Ex:
            self.Log ("An exception occurred while trying to start the test: " + str(Ex))
            return False

    # Stop OUTPUT
    def Output_Stop(self):
        try:
            self.SendCommand("CONF:OUTP OFF")
            Status = self.SendCommand ("CONF:OUTP?")
            Counter = 1
            while (Status != "OFF"):
                self.Log ("Retrying #" + str(Counter) + " to stop the test...")
                self.SendCommand("CONF:OUTP OFF")
                sleep(0.05)
                Status = self.SendCommand ("CONF:OUTP?")
                Counter = Counter + 1

            self.Log ("Test stopped using STOP command")

            if self.GetAllSystemErrors() > 0:
                self.Log ("Error(s) reported while trying to stop the test.")
                return False

            return True
        except Exception as Ex:
            self.Log ("An exception occurred while trying to stop the test: " + str(Ex))
            return False
    
    # Clear 
    def Clear_Programs(self):
        try:
            Counter = 1
            while (Counter < 11):
                self.Log ("Clearing Program #" + str(Counter))
                self.SendCommand("PROG:SEL " + str(Counter))
                sleep(0.05)
                self.SendCommand ("PROG:CLEAR")
                Counter = Counter + 1

            self.Log ("Programs cleareds")

            if self.GetAllSystemErrors() > 0:
                self.Log ("Error(s) reported while trying to clear the programs.")
                return False

            return True
        except Exception as Ex:
            self.Log ("An exception occurred while trying to clear the programs: " + str(Ex))
            return False


    # Configure Sequence.
    def Configure_Seq(self, Type, Voltage, VSlew, SCurrent, CSlew, LCurrent, Time ):
        try:
            self.Log ("Configuring Sequence.")
            self.SendCommand("PROGRAM:SEQ " + str(Type) + "," + str(Voltage) + "," + str(VSlew) + "," + str(SCurrent) + "," + str(CSlew) + "," + str(LCurrent) + "," + str(Time))
            return True
        except Exception as Ex:
            self.Log ("An exception occurred while trying to configure a sequence: " + str(Ex))
            return False

    # RUN Program
    def RUN_Program(self):
        try:
            if self.GetAllSystemErrors() > 0:
                self.Log ("Did not start the program due to several System Errors reported.")
                return False
            self.SendCommand("PROG:RUN ON")
            return True
        except Exception as Ex:
            self.Log ("An exception occurred while trying to start the test: " + str(Ex))
            return False

    # Monitor the Program
    def Prog_Monitor(self):
        try:
            Status = self.SendCommand ("PROG:RUN?")
            while (Status != "OFF"):
                self.Log ("Program is running...")
                sleep(0.5)
                Status = self.SendCommand ("PROG:RUN?")
                self.SendCommand ("FETCH:VOLT?")
                self.SendCommand ("FETCH:CURR?")


            self.Log ("Program stopped.")
            return True
        except Exception as Ex:
            self.Log ("An exception occurred while trying to start the Program: " + str(Ex))
            return False
