"""
Module for testing the  generic class ErrorDisplay to see if the intance can handle errors of a given intance. It displays error messages and hold a status of generic instance error status. Depending on if the instance is working properly or not. The meaning of this class to be imported at any instance to handle malfunctions and errors.
"""
__author__ = "Mats Larse"
__copyright__ = "Mats Larsen 2014"
__credits__ = ["Mats Larsen"]
__license__ = "GPLv3"
__maintainer__ = "Mats Larsen"
__email__ = "larsen.mats.87@gmail.com"
__status__ = "Development"

#--------------------------------------------------------------------
#Import
#--------------------------------------------------------------------
from error_display import ErrorDisplay as ED 
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

class TestErrorDisplay(object):
    def __init__(self,name,log_level):
        self._name = name # Name of the Instance
        self._log_level = log_level # The information level

    def testInit(self):
        e1 = ED('e1')#self._log_level)
log_level = 2
print('start here')
ted = TestErrorDisplay(name='TestingOfErrorDisplay',log_level=log_level)
ted.testInit()
        
