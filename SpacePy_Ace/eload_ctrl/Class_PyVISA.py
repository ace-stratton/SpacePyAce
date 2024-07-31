'''
    =============================================================================
    Chroma Systems Solutions, Inc. 2023
    Class to instantiate the PyVISA class to control a Chroma Instrument over
    a supported communication interface by VISA using SCPI Commands (ASCII
    characters).

    NOTES:
    * Install the Python "PyVISA" module to work with this class.
      The command "pip install pyvisa" (without quotes) can be used to install
      this module in Windows command prompt or in console used.
    * Python v3.8 was used to develop and maintain this source code.
    * NI-VISA or a compatible VISA architecture may be required to be installed
      to establish communication properly. As an option, PyVISA-py backend can
      be used instead of the NI-VISA backend.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

    Copyright © 2001-2021 Python Software Foundation; All Rights Reserved
    =============================================================================
'''

import pyvisa as visa # PyVISA module
from datetime import datetime
from time import sleep # Library to use the sleep (delay) function
import re # Module for REGular EXpressions
from decimal import Decimal

class Chroma_PyVISA():
    # Private PyVISA / Connection attributes
    __Backend = "" # Set "@py" to use PyVISA-py as backend
    __ResourceManager = visa.ResourceManager(__Backend) # Instantiate the Resource Manager object
    __Instrument = object() # _Instrument will be the object to write and read commands
    __ResourceName = "" # String of the Resource name that is required to communicate with the instrument
    __WriteTermChar = '\n' # Termination character accepted by most of the Chroma instruments that use SCPI Commands
    __ReadTermChar = '\n' # Termination character to read from responses
    __BytesReadBuffer = 4096 # Number of bytes for reading from the buffer
    __Timeout = 5000 # Timeout is in milliseconds
    __WriteDelay = 0.05 # This delay will prevent writing several commands in a short time that may cause an overflow in the buffer
    __Connected = False # Boolean attribute to check if there is connection with the instrument
    __CommunicationInterface = "PyVISA"
    # Settings for serial communication
    __BaudRate = 9600 # Baud Rate configured by default: 9600
    __DataBits = 8
    __StopBits = 10 # Set to 1
    __Parity = 0 # None
    __BaudRatesValid = [4800, 9600, 19200, 38400, 57600, 115200] # List of valid Baud Rates
    __StopBitsValid = [10,15,20] # (10 = 1; 15 = 1.5; 20 = 2)
    __ParityValuesValidTuple = [(0,"NONE"),(1,"ODD"),(2,"EVEN"),(3,"MARK"),(4,"SPACE")]

    # Private Log Data attributes
    __LogLevel = 1 # Log data function (0 = Disabled; 1 = Log Data in text file only; 2 = Log Data in text file and to be printed in console)
    __LogFileCreated = False # To know if the Log Data file was created successfully
    __LogFile = None # Log Data file object to be instantiated
    __LogTerminationCharacters = False

    # Private Instrument's generic attributes
    __Manufacturer = "N/A"
    __ModelNumber = "N/A"
    __SerialNumber = "N/A"
    __FirmwareVersion = "N/A"

    __NaN = -99999.1234 # Constant value to identify when a measuremnet or value is not valid
    _ErrorString = "<ERROR>"
    __TimeoutMaxRetries = 3

    ''' >>>>> PROPERTIES (GETTERS) <<<<< '''
    @property
    def IsConnected(self): return self.__Connected
    @property
    def LogLevel(self): return self.__LogLevel
    @property
    def ResourceName(self): return self.__ResourceName
    @property
    def WriteTerminationCharacter(self): return self.__WriteTermChar
    @property
    def ReadTerminationCharacter(self): return self.__ReadTermChar
    @property
    def TimeoutRetries(self): return self.__TimeoutMaxRetries
    @property
    def Manufacturer(self): return self.__Manufacturer
    @property
    def ModelNumber(self): return self.__ModelNumber
    @property
    def SerialNumber(self): return self.__SerialNumber
    @property
    def FirmwareVersions(self): return self.__FirmwareVersion
    @property
    def BaudRate(self): return self.__BaudRate
    @property
    def Parity(self): return self.__Parity
    @property
    def DataBits(self): return self.__DataBits


    ''' >>>>> SETTERS <<<<< '''
    @TimeoutRetries.setter
    def TimeoutRetries(self, Value):
        Description = "Maximum Timeout Retries"
        try:
            if not IsInt(Value):
                self.Log ("Could not set the " + str(Description) + ": the ")
                return False
            self.__TimeoutMaxRetries = int(Value)
            self.Log (str(Description) + " set to " + str(Value) + " successfully.")
            return True
        except Exception as Ex:
            self.Log ("An exception occurred while trying to set the " + str(Description) + ": " + str(Ex))
            return False

    # Constructor (Set the parameter to true to enable data logging, which will create a plain text file)
    def __init__(self, LogLevel=0, LogIdentifier=""):
        try:
            LogRegExPattern = "^\w+$"
            self.__LogLevel = LogLevel
            self.Connected = False
            if LogLevel > 0:
                if bool(re.search(LogRegExPattern,LogIdentifier)) == False:
                    LogIdentifier = ""

                if LogIdentifier != "":
                    LogIdentifier = LogIdentifier + "_"

                self.__LogFile = open("Log_" + LogIdentifier + datetime.now().strftime('%Y%m%d_%H%M%S') + ".txt", "w+") # E.g. "Log_20200228_145304.txt"
                self.__LogFileCreated = True
                self.Log ("Chroma PyVISA object instantiated successfully.")
            pass
        except Exception as Ex:
            print("An exception occurred while trying to create the Chroma PyVISA object: " + str(Ex), True)
            input()
            return

    # Destructor (finishes writing to the log file if it's enabled)
    def __del__(self):
        try:
            if self.Connected:
                self.Disconnect() # Try to disconnect before destroying the object
            if self.__LogFileCreated == True:
                self.Log("Chroma PyVISA object destroyed successfully.")
                self.__LogFile.close()
            pass
        except Exception as Ex:
            print("An exception occurred while trying to destroy the Chroma PyVISA object: " + str(Ex))
            return

    ''' ########## PRIVATE FUNCTIONS ########## '''

    ''' ########## PRIVATE GENERIC FUNCTIONS ########## '''



    ''' ########## PRIVATE PYVISA FUNCTIONS ########## '''

    # Get the instrument's identification
    def __GetIdentification(self, LogIdentificationInformation=True):
        try:
            self.Log("Retrieving the Instrument Identification string.")
            IDNResponse = self.SendCommand("*IDN?")

            # If the response was not taken previously, try one more time
            if IDNResponse == "": IDNResponse = self.SendCommand("*IDN?")

            # Update Manufacturer, Model Number, Serial Number, and Firmware version(s)
            if IDNResponse != "" and IDNResponse.find(",") >= 0:
                IDN = list()
                IDN = IDNResponse.split(",")
                if len(IDN) >= 4:
                    self.__Manufacturer = IDN[0].strip() # Instrument Manufacturer
                    self.__ModelNumber = IDN[1].strip() # Model Number
                    self.__SerialNumber = IDN[2].strip() # Serial Number

                    # Process Firmware version(s)
                    FirmwareVer = IDN[3].strip() # Firmware version
                    if FirmwareVer.count(".") > 1: # The Firmware version is not fully released and contains more than 1 period (e.g. "3.00.8")
                        PeriodFirstPos = FirmwareVer.index(".") # Get the position of the First period and will use it as the only one
                        FirmwareVer = FirmwareVer.replace(".","") # Remove all periods since we already know the position of the first period
                        FirmwareVer = FirmwareVer[:PeriodFirstPos] + "." + FirmwareVer[PeriodFirstPos:]

                    self.__FirmwareVersion = FirmwareVer.strip() # First Firmware Version

                    if len(IDN) > 4: # More than 1 Firmware versions were reported
                        idx = 4
                        while idx < len(IDN):
                            FirmwareVer = IDN[idx].strip()
                            if FirmwareVer.count(".") > 1: # The Firmware version is not fully released and contains more than 1 period (e.g. "3.00.8")
                                PeriodFirstPos = FirmwareVer.index(".") # Get the position of the First period and will use it as the only one
                                FirmwareVer = FirmwareVer.replace(".","") # Remove all periods since we already know the position of the first period
                                FirmwareVer = FirmwareVer[:PeriodFirstPos] + "." + FirmwareVer[PeriodFirstPos:]

                            self.__FirmwareVersion = self.__FirmwareVersion + ", " + FirmwareVer
                            idx = idx + 1

                        self.__FirmwareVersion = self.__FirmwareVersion.strip()

                    # Log the identification information, but don't print it
                    if (LogIdentificationInformation):
                        self.Log("Manufacturer: " + self.__Manufacturer)
                        self.Log("Model Number: " + self.__ModelNumber)
                        self.Log("Serial Number: " + self.__SerialNumber)
                        self.Log("Firmware Version(s): " + self.__FirmwareVersion)

                    self.Log("Instrument's identification retrieved successfully.")
                else:
                    self.Log("Instrument's identification could not be retrived correctly.")
            return IDNResponse

        except Exception as Ex:
            self.Log("An exception occurred while trying to get the Instrument's identification: " + str(Ex))


    ''' ########## PUBLIC FUNCTIONS ########## '''

    ''' ########## PUBLIC GENERIC FUNCTIONS ########## '''



    ''' ########## PUBLIC PYVISA FUNCTIONS ########## '''

    # Get list of VISA resources as an array of strings (function only available for PyVISA)
    def GetVISAResourceNamesListString(self):
        try:
            ResourceNames = self.__ResourceManager.list_resources()
            ArrayResourceNames = [""] * len(ResourceNames)

            for Item in enumerate(ResourceNames):
                Index, Name = Item
                ArrayResourceNames[Index] = Name

            return ArrayResourceNames
        except Exception as Ex:
            self.Log("An Exception occurred while trying to get the list of VISA Resource names: " + str(Ex))
            return [""]

    # *************** COMMUNICATION FUNCTIONS ***************

    # Function to connect to the Chroma instrument
    def Connect(self, ResourceName=None, ParamNotUsed=None):
        try:
            if ResourceName == None or ResourceName == "":
                RNTuple = self.GetVISAResourceNameSelectedByUser()
                if RNTuple[0]:
                    ResourceName = RNTuple[1]
                else:
                    self.Log("The Resource Name given is empty.")
                    raise ConnectionError("The Resource Name given is empty.")
                    #return False

            if not isinstance(ResourceName, str):
                self.Log("The Resource Name given is not a String.")
                return False
            ResourceName = ResourceName.strip().replace("\n","").replace("\r","") # Remove termination characters

            # Configure the PyVISA Resource Name, termination characters, timeout value, etc.
            self.__ResourceName = ResourceName
            self.__Instrument = self.__ResourceManager.open_resource(self.__ResourceName)
            self.__Instrument.write_termination = self.__WriteTermChar
            self.__Instrument.read_termination = self.__ReadTermChar
            self.__Instrument.timeout = self.__Timeout
            # Serial communication settings
            self.__Instrument.baud_rate = self.__BaudRate # Set the Baud Rate configured
            self.__Instrument.stop_bits = self.__StopBits
            self.__Instrument.parity = self.__Parity

            self.Log("PyVISA Resource Name opened successfully [" + self.__ResourceName + "].")
            self.__Connected = True

            self.__GetIdentification() # Load the Instrument identification (Manufacturer, Model number, serial number, FW versions)
            return True
        except ConnectionError:
            self.Log("An exception occurred while trying to open the connection [" + self.__ResourceName + "].")# + str(Ex))
            self.__Connected = False
            raise
            #input() # Show the message and wait for the user to press a key to continue


    # Close the connection opened
    def Disconnect(self):
        try:
            if self.__Connected:
                self.__Instrument.close()
                self.__Connected = False
                self.Log("PyVISA Resource Name disconnected properly [" + self.__ResourceName + "].")
            else:
                self.Log ("PyVISA Resource Name is already disconnected [" + self.__ResourceName + "].")
            return True
        except Exception as Ex:
            self.Log("An error occurred while trying to close the PyVISA connection: " + str(Ex))
            input()
            return False

    # Set the timeout to be used in seconds (use before connecting)
    def SetTimeout(self, Timeout):
        try:
            MinValue = 0
            MaxValue = 100
            if Timeout < MinValue or Timeout > MaxValue:
                self.Log ("The value for Timeout is out of the valid range [" + str(MinValue) + " - " + MaxValue + "].")
                return False

            self.__Timeout = int(Timeout) * 1000
            return True
        except ValueError:
            # The value passed as argument is not an integer number, throw a ValueError exception:
            self.Log("The Timeout value given is not a valid number.")
            return False
        except Exception as Ex:
            self.Log ("An exception occurred while trying to set the Timeout value: " + str(Ex))
            return False

    def SetWriteTerminationCharacter(self, TerminationCharacter):
        try:
            if TerminationCharacter != "":
                self.__WriteTermChar = TerminationCharacter
                self.Log ("Write Termination Character set to: " + self.__CheckTerminationCharacter(TerminationCharacter))
                return True
            else:
                self.__WriteTermChar = ""
                self.Log ("The Write Termination Character was disabled.")
                return True
        except Exception as Ex:
            self.Log ("An Exception occurred while trying to set the Write Termination Character: " + str(Ex))
            return False

    def SetReadTerminationCharacter(self, TerminationCharacter):
        try:
            if TerminationCharacter != "":
                self.__ReadTermChar = TerminationCharacter
                self.Log ("Read Termination Character set to: " + self.__CheckTerminationCharacter(TerminationCharacter))
                return True
            else:
                self.__WriteTermChar = ""
                self.Log ("The Read Termination Character was disabled.")
                return True
        except Exception as Ex:
            self.Log ("An Exception occurred while trying to set the Read Termination Character: " + str(Ex))
            return False

    def SetBaudRate(self, BaudRate):
        try:
            if not self._IsInt(BaudRate):
                self.Log ("Could not set the Baud Rate value: the value given is not an Integer value.")
                return False

            if not BaudRate in self.__BaudRatesValid:
                self.Log ("Could not set the Baud Rate value: the Baud Rate value given is not supported.")
                return False

            self.__BaudRate = int(BaudRate)
            self.Log ("Baud Rate value set to [" + str(BaudRate) + "] successfully.")
            return True
        except Exception as Ex:
            self.Log ("An exception occurred while trying to set the Baud Rate value: " + str(Ex))
            return False

    def SetStopBits(self, StopBits):
        try:
            if not self._IsInt(StopBits):
                self.Log ("Could not set the Stop Bits value: the value given is not an Integer value.")
                return False

            if not StopBits in self.__StopBitsValid:
                self.Log ("Could not set the Stop Bits value: the value given is not a valid value.")
                self.Log ("Stop Bits valid values:")
                for idx in range (0, len(self.__StopBitsValid)):
                    self.Log (str(self.__StopBitsValid[idx]))
                return False

            self.__StopBits = StopBits
            self.Log ("Stop Bits value set to [" + str(self.__StopBits) + "] successfully.")
            return True
        except Exception as Ex:
            self.Log ("An exception occurred while trying to set the Stop Bits: " + str(Ex))
            return False

    def __CheckTerminationCharacter(self, TerminationCharacter):
        try:
            if TerminationCharacter == "\n":
                TerminationCharacter = "Line Feed"
            elif TerminationCharacter == "\r":
                TerminationCharacter = "Carrier Return"
            elif TerminationCharacter == "\r\n":
                TerminationCharacter = "CRLF"
            else:
                TerminationCharacter = TerminationCharacter

            return TerminationCharacter
        except Exception as Ex:
            self.Log ("An Exception occurred while trying to determine the Termination Character: " + str(Ex))
            return ""

    # Communication Interface
    def GetCommunicationInterface(self):
        return self.__CommunicationInterface


    # ************ WRITE AND QUERY SCPI COMMANDS (ASCII) GENERIC FUNCTIONS ************

    # Write
    def Write(self, Command, Encoding = None, LogCommand = True):
        try:
            Command = Command.strip() # Remove any termination characters or unnecessary spaces
            if Command == "":
                self.Log("Could not write data to the instrument, the command given is empty.")
                return False
            if self.__Connected == False:
                self.Log("Could not write data to the instrument, the connection is not open.")
                return False

            self.__Instrument.write(Command, None, Encoding) # the PyVISA should write the command including the termination character configured
            if LogCommand == True:
                self.Log("<W>: [" + Command + "]")

            sleep(self.__WriteDelay) # Wait a delay to keep communication stable (in case a continuous loop is used to write commands)
            return True
        except Exception as Ex:
            self.Log("An exception occurred while trying to write the [" + Command + "] Command to PyVISA Resource Name: " + str(Ex))
            return False

    # Read (Encoding argument can be used to give a specific Encoding to read)
    def Read(self, Encoding = None):
        try:
            # From PyVISA can read data using a specific encoding
            if Encoding == "":
                Response = self.__Instrument.read()
            else:
                Response = self.__Instrument.read(encoding=Encoding)

            # NOTE: the "PyVISA.read()" function may not return the termination character appended to the response.
            # In order to get the termination characters included in the responses, additional configuration may be required
            if self.__LogTerminationCharacters:
                Response = Response.replace('\n','\LF').replace('\r','\CR').strip() # Clean the response from instrument (remove the termination character and trim spaces)
            else:
                Response = Response.replace("\n","").replace("\r","").strip()

            if Response != "":
                self.Log("<R>: [" + Response + "]")
                Response = Response.replace("\LF","").replace("\CR","").strip()
                return Response
            else:
                self.Log("Could not read data or it is unavailable.")
                return ""
        except Exception as Ex:
            self.Log("An exception occurred while trying to read data from Resource Name [" + self.__ResourceName + "]: " + str(Ex))
            return ""


    # Send Command and if it includes the "?" character, a response will try to be read
    def SendCommand(self, Command, WriteEncoding = None, ReadEncoding = None, ForceQuery=False, LogCommand = True, DoNotQuery=False):
        try:
            if not self.IsConnected:
                return ""
            Command = Command.strip()
            Success = False
            Response = ""
            Counter = 0
            while (Success == False and Counter < self.__TimeoutMaxRetries):
                if self.Write(Command, WriteEncoding, LogCommand) == True:
                    if ('?' in Command or ForceQuery) and DoNotQuery == False:
                        Response = self.Read(ReadEncoding)
                        if Response != "": Success = True
                    else:
                        Success = True
                if not Success:
                    Counter = Counter + 1

            if Success == False:
                self.Log ("Could not send a Command properly after [" + str(Counter) + "] tries.")

            return Response
        except Exception as Ex:
            self.Log("An exception occurred while trying to send a command to the Instrument over PyVISA: " + str(Ex))
            return ""

    # Query Binary Data
    def QueryBinaryValues(self, Command, LogData=False):
        try:
            if (Command != ""):
                BinData = None
                self.__Instrument.query_binary_values(Command, BinData)
                if LogData:
                    self.Log(BinData)
                return BinData
            else:
                return ""
        except Exception as Ex:
            self.Log("An exception occurred while trying to query binary values: " + str(Ex))
            return ""


    # Check Decimal Places
    def GetDecimalPlaces(self, Value):
        try:
            float(Value)
            D = Decimal(str(Value))
            Exp = D.as_tuple().exponent

            Exp = abs(Exp)

            return True, Exp
        except Exception as Ex:
            self.Log ("An Exception occurred while trying to get the Decimal places for a number: " + str(Ex))
            return False, -1

    # Returns an Integer number by querying a SCPI command
    def _GetIntNumber(self, SCPICommand):
        try:
            if (SCPICommand.strip() != ""):
                Response = self.SendCommand(SCPICommand)
                if (Response != ""):
                    if self._IsInt(Response):
                        return int(Response)
                    else:
                        self.Log ("Could not get an Integer number: the value gotten is not an Integer number.")
                        return int(self.__NaN)
                else:
                    return float(self.__NaN)
            else:
                self.Log ("Could not get an Integer number:  The SCPI command given is empty.")
                return self.__NaN
        except ValueError:
            self.Log("A Value Error occurred while trying to get an Integer number.")
            return int(self.__NaN)
        except Exception as Ex:
            self.Log("An Exception occurred while trying to get an Integer number: " + str(Ex))
            return int(self.__NaN)

    # Return a Float Number by querying a SCPI command
    def _GetFloatNumber(self, SCPICommand):
        try:
            if (SCPICommand.strip() != ""):
                Response = self.SendCommand(SCPICommand)
                if (Response != ""):
                    if self._IsFloat(Response):
                        return float(Response)
                    else:
                        self.Log ("Could not get a Float number: the value gotten is not a Float number.")
                        return float(self.__NaN)
                else:
                    return float(self.__NaN)
            else:
                self.Log ("Could not get a float number:  The SCPI command given is empty.")
                return self.__NaN
        except ValueError:
            self.Log("A Value Error occurred while trying to get a float number.")
            return float(self.__NaN)
        except Exception as Ex:
            self.Log("An Exception occurred while trying to get a float number: " + str(Ex))
            return float(self.__NaN)

    # Return multiple float numbers in an array
    def _GetMultipleFloatNumbers(self, SCPICommand, SeparatorCharacter):
        ArrayDefault = [self.__NaN] * 10 # If there is no response, the default array is returned with 10 NaN values
        try:
            if (SeparatorCharacter == ""):
                self.Log("Could not get multiple float numbers: the Separator character is empty.")
                return ArrayDefault
            if (SCPICommand.strip() != ""):
                Response = self.SendCommand(SCPICommand)
                if (Response != ""):
                    if (SeparatorCharacter in Response):
                        TempArray = Response.split(SeparatorCharacter)

                        ArrayMeasurements = [self.__NaN] * len(TempArray)

                        for Idx, Item in enumerate(TempArray):
                            ArrayMeasurements[Idx] = float(Item)
                        return ArrayMeasurements
                else:
                    return ArrayDefault
            else:
                self.Log ("Could not get multiple float numbers: the SCPI command given is empty.")
                return ArrayDefault
        except ValueError:
            self.Log("A Value Error occurred while trying to get multiple float numbers.")
            return ArrayDefault
        except Exception as Ex:
            self.Log("An Exception occurred while trying to get multiple float numbers: " + str(Ex))
            return ArrayDefault

    def _IsFloat(self, Value):
        try:
            float(Value)
            return True
        except Exception as Ex:
            return False

    def _IsInt(self, Value):
        try:
            int(Value)
            return True
        except Exception as Ex:
            return False

    def _IsLong(self, Value):
        try:
            long(Value)
            return True
        except Exception as Ex:
            return False


    # *************** LOG DATA FUNCTIONS ***************

    # Get the date time in the format established in parameter
    def GetDateTime(self, StrFormat='%Y/%m/%d %H:%M:%S'):
        return datetime.now().strftime(StrFormat)

    # Function to print a text message in the console and also to include it in the Log plain text file.
    def Log(self, Message, ForcePrintMessage=False, IncludeDateTime=True):
        try:
            # Log data function (0 = Disabled; 1 = Log Data in text file; 2 = Log Data in text file and print it)
            if self.__LogLevel >= 1:
                if IncludeDateTime:
                    Message = self.GetDateTime() + ": " + Message.strip()
                else:
                    Message = Message.strip()
                if (ForcePrintMessage or self.__LogLevel >= 2):
                    print (Message)
                if self.__LogFileCreated == True:
                    self.__LogFile.write(Message + "\n")
            return
        except Exception as Ex:
            print ("An Exception occurred while trying to log data: " + str(Ex))
            return

    # *************** GET SETTING FUNCTIONS ***************

    def GetConnectionState(self):
        return self.__Connected

    def GetCommunicationInterface(self):
        return self.__CommunicationInterface

    def GetTimeout(self):
        return self.__Timeout

    def GetBaudRate(self):
        return self.__BaudRate

    def GetStopBits(self):
        return self.__StopBits


    # *************** COMMON SCPI COMMANDS ***************


    # Clear the error queue and other status registers (refer to 69200-1 manual for more details)
    def ClearStatus(self):
        self.Log("Clearing the Status.")
        self.SendCommand("*CLS")
        return

    # Reset the instrument (use with the instruments that support the "*RST" SCPI command)
    def Reset(self, WaitTime = 5):
        self.Log("Resetting the instrument.")
        self.SendCommand("*RST")
        sleep(WaitTime) # Wait n seconds while the instrument is reset
        return


    # Get the last System Error from the Error queue (use with the instruments that support the "SYSTem:ERRor?" command)
    # Return: 0: NO ERROR; 1: ERROR is reported; -1: Exception occurred
    def GetSystemError(self):
        try:
            SysError = self.SendCommand("SYSTEM:ERROR?")
            if SysError != "":
                if SysError.upper().find("NO ERROR") > 0:
                    self.Log ("No System Error reported.")
                    return 0 # No errors to report
                else:
                    self.Log("System Error pulled from queue: " + SysError)
                    return 1, SysError
            else:
                return -1, "N/A"

        except Exception as Ex:
            self.Log("An exception occurred while trying to get the last System Error: " + str(Ex))
            return -1, "9999,EXCEPTION OCCURRED"


    # Get the last System Error from the Error queue (use with the instruments that support the "SYSTem:ERRor?" command)
    def GetAllSystemErrors(self):
        try:
            ErrorCount = 0
            RetryCounter = 0
            MaxTimeouts = 5 # will retry up to 4 consecutive times to read the buffer

            Response = self.SendCommand("SYSTEM:ERROR?").strip()

            while Response.upper().find("NO ERROR") < 0 and RetryCounter < MaxTimeouts:
                if Response != "":
                    ErrorCount = ErrorCount + 1
                    self.Log("System Error #" + str(ErrorCount) + " pulled from queue: " + Response)
                    RetryCounter = 0
                    Response = ""
                else:
                    RetryCounter = RetryCounter + 1
                    if RetryCounter < MaxTimeouts:
                        Response = self.SendCommand("SYSTEM:ERROR?")

            if RetryCounter >= MaxTimeouts:
                self.Log("Could not get a response for System Errors after " + str(MaxTimeouts) + " tries.")

            if ErrorCount > 0:
                self.Log("Number of errors pulled from queue: " + str(ErrorCount))
            return ErrorCount

        except Exception as Ex:
            self.Log("An exception occurred while trying to get all System Errors: " + str(Ex))
            return ErrorCount

    def SetAndVerifySingleValue(self, WriteCommand, QueryCommand, ValueToGet, Description = "Undefined Setting", MaxTries=3, DigitsOfPrecision=8):
        try:
            # Validation
            if Description == "": Description = "N/A"
            if (WriteCommand.strip() == ""):
                self.Log("[" + Description + "] Could not set and verify a value to the device: the Write Command is empty.")
                return False
            elif (QueryCommand.strip() == ""):
                self.Log("[" + Description + "] Could not set and verify a value to the device: the Query Command is empty.")
                return False
            if ValueToGet == None:
                self.Log ("[" + Description + "] Could not set and verify a value to the device: the value to verify is not given [None].")
                return False
            if isinstance(ValueToGet, str): ValueToGet = ValueToGet.strip().upper()

            Counter = 1
            while (Counter <= MaxTries):
                # Write the Command to set the value
                if self.Write(WriteCommand):
                    # Query the Command to verify the value set
                    Response = ""
                    Response = self.SendCommand(QueryCommand).strip()
                    TempResponse = Response.strip().upper() # If it's a string, we will compare it using upper case...

                    # There is no response
                    if TempResponse == "":
                        if Counter <= 1: self.Log("[" + Description + "] Could not read the value set [" + Description + "] time.")
                        if Counter > 1: self.Log("[" + Description + "] Could not read the value set [" + Description + "] times.")
                        Counter = Counter + 1
                        continue

                    # LIST OF MULTIPLE VALUES TO COMPARE WITH
                    if isinstance(ValueToGet, list): # LIST
                        for i in range (0, len(ValueToGet)):
                            if self._IsFloat(TempResponse) and self._IsFloat(ValueToGet[i]):
                                if DigitsOfPrecision >= 0:
                                    TempResponse = round(float(TempResponse), DigitsOfPrecision)
                                    ValueToGet = round(float(ValueToGet[i]), DigitsOfPrecision)
                                if float(TempResponse) == float(ValueToGet[i]):
                                    self.Log ("[" + Description + "] set to [" + str(float(TempResponse)) + "] successfully.")
                                    return True
                            elif self._IsInt(TempResponse) and self._IsInt(ValueToGet[i]):
                                if int(TempResponse) == int(ValueToGet[i]):
                                    self.Log ("[" + Description + "] set to [" + str(TempResponse) + "] successfully.")
                                    return True
                            elif isinstance(ValueToGet[i], str):
                                if ValueToGet[i] == str(TempResponse):
                                    self.Log("[" + Description + "] set to [" + TempResponse + "] successfully.")
                                    return True
                    else:
                        # SINGLE VALUE TO COMPARE WITH
                        if self._IsFloat(TempResponse) and self._IsFloat(ValueToGet):
                            if DigitsOfPrecision >= 0:
                                TempResponse = round(float(TempResponse), DigitsOfPrecision)
                                ValueToGet = round(float(ValueToGet), DigitsOfPrecision)
                            if float(ValueToGet) == float(TempResponse):
                                self.Log("[" + Description + "] set to [" + str(float(TempResponse)) + "] successfully.")
                                return True
                            else:
                                self.Log("[" + Description + "] Could not set the value to the device, the value to set does not match the value retrieved.")
                        elif self._IsInt(TempResponse) and self._IsInt(ValueToGet):
                            if int(ValueToGet) == int(TempResponse):
                                self.Log ("[" + Description + "] set to [" + str(TempResponse) + "] successfully.")
                                return True
                        elif isinstance(TempResponse, str): # STRING
                            if ValueToGet == TempResponse:
                                self.Log("[" + Description + "] set to [" + TempResponse + "] successfully.")
                                return True

                    Counter = Counter + 1
                    #sleep(0.5) # This is in case we are not successful in writing a command or reading a response

            self.Log ("[" + Description + "] Could not set or verify the value after " + str(Counter - 1) + " tries.")
            return False

        except ValueError:
            self.Log ("Could not set and verify a value: a Value Error occurred.")
            return False
        except Exception as Ex:
            self.Log("An Exception occurred while trying to set and verify a value: " + str(Ex))
            return False

    def ValidateNumberRange(self, ValueDescription, Number, MinValue, MaxValue, DigitsOfPrecision = 6):
        try:
            if not self._IsInt(Number) and not self._IsFloat(Number):
                self.Log ("The number to validate is not an integer nor a float number.")
                return False

            if isinstance(Number, float):
                MinValue = round(MinValue, DigitsOfPrecision)
                MaxValue = round(MaxValue, DigitsOfPrecision)

            if Number < MinValue or Number > MaxValue:
                print ("The " + ValueDescription + " [" + str(Number) + "] is out of range [" + str(MinValue) + " ~ " + str(MaxValue) + "]")
                return False
            else:
                return True
        except Exception as Ex:
            print ("An exception occurred while trying to validate a number: " + str(Ex))
            return False

    def ValidateSettingsListOfTuples(self, SettingsTuplesList, SettingsDescription = ""):
        try:
            QuantityOfSettingsRequiredPerTuple = 5 # This is the quantity of settings to expect per tuple

            # VALIDATION
            # We expect to get a list of tuples. Needs to validate there is a list
            if not isinstance(SettingsTuplesList, list):
                self.Log ("Could not validate a list of settings: the argument received is not a list (of tuples).")
                return False

            if len(SettingsTuplesList) <= 0:
                self.Log ("Could not validate a list of settings: the list received is empty.")
                return False

            for i, TempTuple in enumerate(SettingsTuplesList):
                #TempTuple = SettingsTuplesList[i]
                # Check that the elements included in the list are all tuples
                if type(TempTuple) is not tuple:
                    self.Log ("The element " + str(i + 1) + " from the list received is not a tuple.")
                    return False
                # There is a tuple, let's check it contains exactly n elements required per tuple
                if len(TempTuple) != QuantityOfSettingsRequiredPerTuple:
                    self.Log ("Could not validate a list of settings: one tuple has a different quantity of settings.")
                    return False

                Value = TempTuple[0]
                MinValue = TempTuple[1]
                MaxValue = TempTuple[2]
                Resolution = TempTuple[3]
                SettingDescription = TempTuple[4]

                # Validate the settings attached in each tuple
                # Number to be validated
                if not isinstance(SettingDescription, str): # Setting Description - String
                    self.Log ("The description of the setting is not a string value.")
                    return False
                if not self._IsInt(Value) and not self._IsFloat(Value): # Number - Int or Float
                    self.Log ("The number value to validate is not an integer nor a float number.")
                    return False
                # Minimum Value
                if not self._IsInt(MinValue) and not self._IsFloat(MinValue): # Minimum - Int or Float
                    self.Log ("The minimum value is not an integer nor a float number.")
                    return False
                # Maximum Value
                if not self._IsInt(MaxValue) and not self._IsFloat(MaxValue): # Maximum - Int or Float
                    self.Log ("The maximum value is not an integer nor a float number.")
                    return False
                # Resolution
                if not self._IsInt(Resolution): # Resolution - Int
                    self.Log ("The resolution is not an integer nor a float number.")
                    return False

                # Check the Resolution (digits of precision) of the number received against the number of digits of precision allowed
                if not isinstance(Value, int) and isinstance(Value, float):
                    DecimalTuple = self.GetDecimalPlaces(Value)
                    if DecimalTuple[0]:
                        if DecimalTuple[1] > Resolution:
                            self.Log ("The resolution of the number given for [" + SettingDescription + "] as [" + str(DecimalTuple[1]) + "] digits of resolution is higher than the resolution allowed: [" + str(Resolution) + "] digits of resolution.")
                            return False
                        else:
                            if isinstance(Value, float):
                                MinValue = round(MinValue, Resolution)
                                MaxValue = round(MaxValue, Resolution)
                    else:
                        self.Log ("Could not get the decimal places of the number value to validate.")
                        return False

                if Value < MinValue or Value > MaxValue:
                    self.Log ("The " + SettingDescription + " [" + str(Value) + "] is out of range [" + str(MinValue) + " ~ " + str(MaxValue) + "]")
                    return False


            if SettingsDescription == "" or SettingsDescription == None:
                self.Log ("Settings validated successfully.")
            else:
                self.Log (SettingsDescription + " - Settings validated successfully.")

            return True # If we reach here, then something wrong may occur... ???
        except Exception as Ex:
            self.Log ("An exception occurred while trying to validate the range for setting: " + str(Ex))
            return False

    def SetFloatSetting(self, Value, SetCommand, GetCommand, Description = "", MinValue = 0.0, MaxValue = 0.0, DigitsOfPrecision = 6):
        try:
            # Validation
            if not self._IsFloat(Value): return False
            if not self._IsFloat(MinValue): return False
            if not self._IsFloat(MaxValue): return False
            if not self._IsInt(DigitsOfPrecision): return False

            SetCommand = SetCommand.strip()
            GetCommand = GetCommand.strip()

            if SetCommand == "": return False
            if GetCommand == "": return False

            if MaxValue != 0.0 or MinValue != 0.0:
                # Check if the value is within the Min and Max Values
                if self.ValidateNumberRange(Description, Value, MinValue, MaxValue) == False:
                    return False

            if self.SetAndVerifySingleValue(SetCommand, GetCommand, Value, Description):
                return True
            else:
                return False
        except Exception as Ex:
            self.Log ("An exception occurred while trying to set a setting with float value [" + Description + "]: " + str(Ex))
            return False

    # Return a single measurement as a float number
    def _FetchSingleMeasurement(self, SCPICommand):
        try:
            if (SCPICommand.strip() != ""):
                Response = self.SendCommand(SCPICommand)
                if (Response != ""):
                    return float(Response)
                else:
                    return float(self.__NaN)
            else:
                self.Log ("The SCPI command given is empty.")
                return self.__NaN
        except ValueError:
            self.Log("A Value Error occurred while trying to fetch a measurement.")
            return float(self.__NaN)
        except Exception as Ex:
            self.Log("An Exception occurred while trying to fetch a measurement: " + str(Ex))
            return float(self.__NaN)

    def GetVISAResourceNameSelectedByUser(self):
        try:
            self.Log ("VISA Resource Names found:")
            RNList = self.GetVISAResourceNamesListString()
            if len(RNList) <= 0:
                self.Log ("No VISA Resource Names were found.")
                return False, ""

            self.Log ("0: <CANCEL OPERATION>", True, False)
            for idx, Item in enumerate(RNList):
                self.Log (str(idx + 1) + ": " + Item, True, False)

            # Variables to try at least n times for getting an appropriate VISA Resource Name
            Retry = False
            Success = False
            TryCounter = 0
            MaxRetries = 3
            while (TryCounter < MaxRetries):
                if Retry:
                    TryCounter = TryCounter + 1
                    self.Log ("Retrying #" + str(TryCounter))
                TempStr = input("Input the number of the VISA Resource Name to use for communication (enter 0 to cancel the operation): ")
                TempStr = TempStr.strip()
                if TempStr == "":
                    self.Log ("There was not a number entered. Retrying...")
                    Retry = True
                    continue

                if TempStr == "0":
                    self.Log ("Operation cancelled by user.")
                    return False, ""

                if not self._IsInt(TempStr):
                    self.Log ("The value input is not an integer number.")
                    Retry = True
                    continue
                else:
                    IntRN = int(TempStr)

                if IntRN < 1 or IntRN > len(RNList):
                    self.Log ("The integer number input is not within the VISA Resource Name options available [1 ~ " + str(len(RNList)) + "].")
                    Retry = True
                    continue

                # Here, we have a valid option after validating several options
                ResourceName = RNList[IntRN - 1]
                ResourceName = ResourceName.strip()
                if ResourceName != "":
                    self.Log ("VISA Resource Name selected: " + ResourceName)
                    return True, ResourceName
                else:
                    self.Log ("The VISA Resource Name selected is empty.")
                    return False, ""

            if Success == False:
                self.Log ("Failed to choose a VISA Resource Name by user.")
                return False, ""
        except Exception as Ex:
            self.Log ("An exception occurred while trying to get the VISA Resource Name selected by user: " + str(Ex))
            return False, ""
