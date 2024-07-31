
# python wrapper for package gitlab.endurosatlab.com/ground_station/go-comms/internal/event_notifier within overall package pygs
# This is what you import to use the package.
# File is generated by gopy. Do not edit.
# gopy.exe build -build-tags=dbg_log with_wire_only -no-make -output=art\spacepy-windows-amd64 .\pygs ..\pkg\gs ..\pkg\consts ..\pkg\misc ..\internal\event_notifier

# the following is required to enable dlopen to open the _go.so file
import os,sys,inspect,collections
try:
	import collections.abc as _collections_abc
except ImportError:
	_collections_abc = collections

cwd = os.getcwd()
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(currentdir)
from . import _pygs
from . import go

os.chdir(cwd)

# to use this code in your end-user python file, import it as follows:
# from pygs import event_notifier
# and then refer to everything using event_notifier. prefix
# packages imported by this package listed below:




# ---- Types ---


#---- Enums from Go (collections of consts with same type) ---
from enum import Enum

class EventNotifierId(Enum):
	"""
	An enumeration of all defined event notifier ids.
	
	"""
	EventNotifierId_TPSyncSent = 1
	EventNotifierId_TPSyncRecv = 2
	EventNotifierId_TPStatusSent = 3
	EventNotifierId_TPStatusRecv = 4
	EventNotifierId_TPDataSent = 5
	EventNotifierId_TPDataRecv = 6
	EventNotifierId_TPErr = 7
	EventNotifierId_DataTick = 100

EventNotifierId_TPSyncSent = 1
EventNotifierId_TPSyncRecv = 2
EventNotifierId_TPStatusSent = 3
EventNotifierId_TPStatusRecv = 4
EventNotifierId_TPDataSent = 5
EventNotifierId_TPDataRecv = 6
EventNotifierId_TPErr = 7
EventNotifierId_DataTick = 100



#---- Constants from Go: Python can only ask that you please don't change these! ---
EventNotifierId_AirHSResp = 700
EventNotifierId_AirInitHS = 600
EventNotifierId_CPErr = 200
EventNotifierId_FWUpdErr = 300
EventNotifierId_MacGWErr = 400
EventNotifierId_UhfGWErr = 500


# ---- Global Variables: can only use functions to access ---


# ---- Interfaces ---


# ---- Structs ---

# Python type for struct event_notifier.EventNotifier
class EventNotifier(go.GoClass):
	"""An event notifier, fired on specific hard-wired events and can hold data. It can be subscribed to by observers.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_pygs.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_pygs.IncRef(self.handle)
		else:
			self.handle = _pygs.event_notifier_EventNotifier_CTor()
			_pygs.IncRef(self.handle)
	def __del__(self):
		_pygs.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'event_notifier.EventNotifier{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'event_notifier.EventNotifier ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	def Subscribe(self, o, goRun=False):
		"""Subscribe(object o) 
		
		Subscribe to this event notifier.
		"""
		_pygs.event_notifier_EventNotifier_Subscribe(self.handle, o.handle, goRun)
	def Unsubscribe(self, o, goRun=False):
		"""Unsubscribe(object o) 
		
		Unsubscribe from this event notifier.
		"""
		_pygs.event_notifier_EventNotifier_Unsubscribe(self.handle, o.handle, goRun)
	def Notify(self, goRun=False):
		"""Notify() 
		
		Notify all observers of this event.
		"""
		_pygs.event_notifier_EventNotifier_Notify(self.handle, goRun)
	def NotifyWithData(self, data, dataInfo, goRun=False):
		"""NotifyWithData([]int data, str dataInfo) 
		
		Notify all observers of this event, with data.
		"""
		_pygs.event_notifier_EventNotifier_NotifyWithData(self.handle, data.handle, dataInfo, goRun)

# Python type for struct event_notifier.FuncEventObserver
class FuncEventObserver(go.GoClass):
	"""A simple implementation of an observer, which calls fun.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_pygs.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_pygs.IncRef(self.handle)
		else:
			self.handle = _pygs.event_notifier_FuncEventObserver_CTor()
			_pygs.IncRef(self.handle)
	def __del__(self):
		_pygs.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'event_notifier.FuncEventObserver{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'event_notifier.FuncEventObserver ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	def OnNotify(self, goRun=False):
		"""OnNotify() 
		
		Called when the event notifier is notified.
		"""
		_pygs.event_notifier_FuncEventObserver_OnNotify(self.handle, goRun)


# ---- Slices ---


# ---- Maps ---


# ---- Constructors ---
def Get(id):
	"""Get(int id) object
	
	Get a pointer to a singleton EventNotifier per given id.
	"""
	return EventNotifier(handle=_pygs.event_notifier_Get(id))
def NewFuncEventObserver(fun, notifier):
	"""NewFuncEventObserver(callable fun, object notifier) object
	
	Constructor for FuncEventObserver.
	fun will be called upon notify. During its execution, the communication thread will be blocked, so Fun should not be blocking.
	fun will receive the data associated with the event notifier.
	"""
	return FuncEventObserver(handle=_pygs.event_notifier_NewFuncEventObserver(fun, notifier.handle))


# ---- Functions ---


