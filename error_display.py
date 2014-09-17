#--------------------------------------------------------------------
#Administration Details
#--------------------------------------------------------------------
__author__ = "Mats Larsen"
__copyright__ = "Mats Larsen 2014"
__credits__ = ["Mats Larsen"]
__license__ = "GPLv3"
__maintainer__ = "Mats Larsen"
__email__ = "larsen.mats.87@gmail.com"
__status__ = "Development"
__description__ = "Module for generic class to handle errors of a given intance. It displays error messages and hold a status of generic instance error status. Depending on if the instance is working properly or not. The meaning of this class to be imported at any instance to handle malfunctions and errors."
__file__ = "error_display.py"
__class__ ="ErrorDisplay"
#--------------------------------------------------------------------
#Version
#--------------------------------------------------------------------
__version_stage__ = "Pre_alpha"
__version_number__ = "0.1"
__version_risk__ = "This current version is in Pre-alpha version, which meaning that the program can crash or perform other unrespected behavoiurs."
__version_modification__ = "The development project has just been created."
__version_next_update__ = "Implementation of Error warnings and exceptions."  
#--------------------------------------------------------------------
#Import
#--------------------------------------------------------------------
from msg import DisplayMsg as DM # Import library for standard display messages. 
import traceback
#--------------------------------------------------------------------
#CONSTANTS
#--------------------------------------------------------------------
LOG_LEVEL = 2 # Information level
LOG_ALWAYS = 3 # Always log data
FILE = "error_display" # Name of the file
CLASS = 'ErrorDisplay' # Name of the class.
""" Error Priorities """
PRIORITIES = ['HIGH_PRIORITY','MEDIUM_PRIORITY','LOW_PRIORITY']
""" Error Types """
ERRORTYPING = ['Error_Typing']
""" Error Messages """
WORKING = ' is working without any problems and warings!!'
#--------------------------------------------------------------------
#METHODS
#--------------------------------------------------------------------
def log(msg, log_level=LOG_LEVEL):
    """
    Print a message, and track, where the log is invoked
    Input:
    -msg: message to be printed, ''
    -log_level: informationlevel, i
    """
    global LOG_LEVEL
    if log_level <= LOG_LEVEL:
        print(str(log_level) + ' : ' + FILE + '.py::' + traceback.extract_stack()[-2][2] + ' : ' + msg)

class ErrorDisplay(object):
    """
    Class for handling errors of a given instance.
    """    
    class ErrorEXC(Exception):
        """Exception class."""
        def __init__(self,name,e_type,priority,msg,callback):
            """
            Constructor of the suberror, where it casting all arguments.
            """
            self.__dm = DM('Error Msg',2) # Create message display
            if type(name) == str: # Name has to be a string
                self._name = name # Name of the sub error.
            else:
                print(self.__dm.getMsg(6),ERRORTYPING[0],PRIORITIES[0],self.__dm.getMsg(5))

            if e_type in ERRORTYPING: # Type has to be defined
                self._e_type = e_type
            else:
                print(self.__dm.getMsg(7),ERRORTYPING[0],PRIORITIES[0],self.__dm.getMsg(8))

            if priority in PRIORITIES: # Priority has to be defined
                self._priority = priority
            else:
                print( self.__dm.getMsg(7),ERRORTYPING[0],PRIORITIES[0],self.__dm.getMsg(8))
            
            if type(msg) == str: # Msg has to be a string.
                self._msg = msg
            else:
                print(self.__dm.getMsg(6),ERRORTYPING[0],PRIORITIES[0],self.__dm.getMsg(5))
            self._callback = callback
            Exception.__init__(self, 'Name of Error : ' + self._name + '. Error Type : ' + self._e_type + '. Error Priority : ' + self._priority + '. Error Message : ' + self._msg + '. Error in method : ' + self._callback) # Cast a exception.
                        
        def getName(self):
            """
            Returns the Name of the instance.
            """
            return self._name

        def setName(self,name):
            """
            Set a new name of the instance.
            """
            self._name = name
        name = property(getName,setName,doc='Name property')

        def __repr__(self):
            """
            Print the reprentation of the instance.
            """
            return self._msg
    







class ErrorWAR(object):
        """Warning class."""
        def __init__(self,name,e_type,priority,msg,callback):
            """
            Constructor of the suberror, where it casting all arguments.
            """
            self.__dm = DM('Error Warning Msg',2) # Create message display
            if type(name) == str: # Name has to be a string
                self._name = name # Name of the sub error.
            else:
                print(self.__dm.getMsg(6),ERRORTYPING[0],PRIORITIES[0],self.__dm.getMsg(5))

            if e_type in ERRORTYPING: # Type has to be defined
                self._e_type = e_type
            else:
                print(self.__dm.getMsg(7),ERRORTYPING[0],PRIORITIES[0],self.__dm.getMsg(8))

            if priority in PRIORITIES: # Priority has to be defined
                self._priority = priority
            else:
                print( self.__dm.getMsg(7),ERRORTYPING[0],PRIORITIES[0],self.__dm.getMsg(8))
            
            if type(msg) == str: # Msg has to be a string.
                self._msg = msg
            else:
                print(self.__dm.getMsg(6),ERRORTYPING[0],PRIORITIES[0],self.__dm.getMsg(5))
            self._callback = callback
            print(self, 'Name of Error : ' + self._name + '. Error Type : ' + self._e_type + '. Error Priority : ' + self._priority + '. Error Message : ' + self._msg + '. Error in method : ' + self._callback) # Print the warning.
                        
        def getName(self):
            """
            Returns the Name of the instance.
            """
            return self._name

        def setName(self,name):
            """
            Set a new name of the instance.
            """
            self._name = name
        name = property(getName,setName,doc='Name property')

        def __repr__(self):
            """
            Print the reprentation of the instance.
            """
            return self._msg
    
    def __init__(self,name=None,log_level=None):
        """
        Constuctor for the ErrorDisplay, to list and handle all errors.
        """
        self.__dm = DM('Display Messages for ErrorDisplay',2) 
        if type(name) == str: # Name has to be a string
            self._name = name # Name of the sub error.
        elif name == None:
            raise self.ErrorEXC(self.__dm.getMsg(10),ERRORTYPING[0],PRIORITIES[0],self.__dm.getMsg(11),traceback.extract_stack()[-2][2])
        
        else:
            raise self.ErrorEXC(self.__dm.getMsg(6),ERRORTYPING[0],PRIORITIES[0],self.__dm.getMsg(5),traceback.extract_stack()[-2][2])
        
        if type(log_level) == int:
            self._log_level = log_level
        elif log_level == None:
            raise self.ErrorEXC(self.__dm.getMsg(10),ERRORTYPING[0],PRIORITIES[0],self.__dm.getMsg(11),traceback.extract_stack()[-2][2])    
        else:
            raise self.ErrorEXC(name=self.__dm.getMsg(7),e_type=ERRORTYPING[0],priority=PRIORITIES[0],msg=self.__dm.getMsg(9),callback=traceback.extract_stack()[-2][2])

        self.__war = [] # List containing error warnings.
        self.__exc = [] # List containing error exceptions.

    def createErrorWar(self,name,e_type,priority,msg,callback):
        """
        Create a warning, which is stored in a list.
        """
        if name
        self.__war.append(self.ErrorWAR(name=name,e_type=e_type,priority=priority,msg=msg,callback=callback))
        
