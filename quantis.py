# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 00:36:13 2016

Wrapper for Quantis.h generated with ctypesgen.py

@author: Gabriel Guerrer
"""

import numpy as np
import sys, time
import platform
from ctypes import *

# DETECT OS

def is_windows_os():
    return 'Windows' in platform.system()
    
if is_windows_os():
    lib_str = 'Quantis.dll'
else:
    lib_str = 'libQuantis.so'
lib = cdll.LoadLibrary(lib_str)

# GENERIC

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P"):
        return type
    else:
        return c_void_p

#def POINTER(obj):
#    p = POINTER(obj)
#
#    # Convert None to a real NULL pointer to work around bugs
#    # in how ctypes handles None on 64-bit platforms
#    if not isinstance(p.from_param, classmethod):
#        def from_param(cls, x):
#            if x is None:
#                return cls()
#            else:
#                return x
#        p.from_param = classmethod(from_param)
#
#    return p


# DEVICE TYPE
QUANTIS_DEVICE_PCI = 1 
QUANTIS_DEVICE_USB = 2 

QuantisDeviceType = c_int

# ERRORS
QUANTIS_SUCCESS = 0 
QUANTIS_ERROR_NO_DRIVER = (-1) 
QUANTIS_ERROR_INVALID_DEVICE_NUMBER = (-2) 
QUANTIS_ERROR_INVALID_READ_SIZE = (-3) 
QUANTIS_ERROR_INVALID_PARAMETER = (-4)
QUANTIS_ERROR_NO_MEMORY = (-5)
QUANTIS_ERROR_NO_MODULE = (-6)
QUANTIS_ERROR_IO = (-7) 
QUANTIS_ERROR_NO_DEVICE = (-8) 
QUANTIS_ERROR_OPERATION_NOT_SUPPORTED = (-9)
QUANTIS_ERROR_OTHER = (-99) 

QuantisError = c_int

QUANTIS_MAX_READ_SIZE = ((16 * 1024) * 1024)

# STRUCTS
class QuantisOperations(Structure):
    pass

class QuantisDeviceHandle(Structure):
    pass

QuantisOperations._fields_ = [
    ('BoardReset', CFUNCTYPE(UNCHECKED(c_int), POINTER(QuantisDeviceHandle))),
    ('Close', CFUNCTYPE(UNCHECKED(None), POINTER(QuantisDeviceHandle))),
    ('Count', CFUNCTYPE(UNCHECKED(c_int), )),
    ('GetBoardVersion', CFUNCTYPE(UNCHECKED(c_int), POINTER(QuantisDeviceHandle))),
    ('GetDriverVersion', CFUNCTYPE(UNCHECKED(c_float), )),
    ('GetManufacturer', CFUNCTYPE(UNCHECKED(String), POINTER(QuantisDeviceHandle))),
    ('GetModulesMask', CFUNCTYPE(UNCHECKED(c_int), POINTER(QuantisDeviceHandle))),
    ('GetModulesDataRate', CFUNCTYPE(UNCHECKED(c_int), POINTER(QuantisDeviceHandle))),
    ('GetModulesPower', CFUNCTYPE(UNCHECKED(c_int), POINTER(QuantisDeviceHandle))),
    ('GetModulesStatus', CFUNCTYPE(UNCHECKED(c_int), POINTER(QuantisDeviceHandle))),
    ('GetSerialNumber', CFUNCTYPE(UNCHECKED(String), POINTER(QuantisDeviceHandle))),
    ('ModulesDisable', CFUNCTYPE(UNCHECKED(c_int), POINTER(QuantisDeviceHandle), c_int)),
    ('ModulesEnable', CFUNCTYPE(UNCHECKED(c_int), POINTER(QuantisDeviceHandle), c_int)),
    ('Open', CFUNCTYPE(UNCHECKED(c_int), POINTER(QuantisDeviceHandle))),
    ('Read', CFUNCTYPE(UNCHECKED(c_int), POINTER(QuantisDeviceHandle), POINTER(None), c_size_t)),
    ('GetBusDeviceId', CFUNCTYPE(UNCHECKED(c_int), POINTER(QuantisDeviceHandle))),
    ]
    

QuantisDeviceHandle._fields_ = [
    ('deviceNumber', c_int),
    ('deviceType', c_int),
    ('ops', POINTER(QuantisOperations)),
    ('privateData', POINTER(None)),
    ]



    
# FUNCTIONS

QuantisBoardReset = lib.QuantisBoardReset
QuantisBoardReset.argtypes = [QuantisDeviceType, c_uint]
QuantisBoardReset.restype = c_int    

QuantisCount = lib.QuantisCount
QuantisCount.argtypes = [QuantisDeviceType]
QuantisCount.restype = c_int

QuantisGetBoardVersion = lib.QuantisGetBoardVersion
QuantisGetBoardVersion.argtypes = [QuantisDeviceType, c_uint]
QuantisGetBoardVersion.restype = c_int

QuantisGetDriverVersion = lib.QuantisGetDriverVersion
QuantisGetDriverVersion.argtypes = [QuantisDeviceType]
QuantisGetDriverVersion.restype = c_float

QuantisGetLibVersion = lib.QuantisGetLibVersion
QuantisGetLibVersion.argtypes = []
QuantisGetLibVersion.restype = c_float

QuantisGetManufacturer = lib.QuantisGetManufacturer
QuantisGetManufacturer.argtypes = [QuantisDeviceType, c_uint]
if sizeof(c_int) == sizeof(c_void_p):
    QuantisGetManufacturer.restype = ReturnString
else:
    QuantisGetManufacturer.restype = String
    QuantisGetManufacturer.errcheck = ReturnString
    
QuantisGetModulesCount = lib.QuantisGetModulesCount
QuantisGetModulesCount.argtypes = [QuantisDeviceType, c_uint]
QuantisGetModulesCount.restype = c_int

QuantisGetModulesDataRate = lib.QuantisGetModulesDataRate
QuantisGetModulesDataRate.argtypes = [QuantisDeviceType, c_uint]
QuantisGetModulesDataRate.restype = c_int

QuantisGetModulesMask = lib.QuantisGetModulesMask
QuantisGetModulesMask.argtypes = [QuantisDeviceType, c_uint]
QuantisGetModulesMask.restype = c_int

QuantisGetModulesPower = lib.QuantisGetModulesPower
QuantisGetModulesPower.argtypes = [QuantisDeviceType, c_uint]
QuantisGetModulesPower.restype = c_int

QuantisGetModulesStatus = lib.QuantisGetModulesStatus
QuantisGetModulesStatus.argtypes = [QuantisDeviceType, c_uint]
QuantisGetModulesStatus.restype = c_int

QuantisGetSerialNumber = lib.QuantisGetSerialNumber
QuantisGetSerialNumber.argtypes = [QuantisDeviceType, c_uint]
if sizeof(c_int) == sizeof(c_void_p):
    QuantisGetSerialNumber.restype = ReturnString
else:
    QuantisGetSerialNumber.restype = String
    QuantisGetSerialNumber.errcheck = ReturnString

QuantisModulesDisable = lib.QuantisModulesDisable
QuantisModulesDisable.argtypes = [QuantisDeviceType, c_uint, c_int]
QuantisModulesDisable.restype = c_int

QuantisModulesEnable = lib.QuantisModulesEnable
QuantisModulesEnable.argtypes = [QuantisDeviceType, c_uint, c_int]
QuantisModulesEnable.restype = c_int

QuantisModulesReset = lib.QuantisModulesReset
QuantisModulesReset.argtypes = [QuantisDeviceType, c_uint, c_int]
QuantisModulesReset.restype = c_int

QuantisOpen = lib.QuantisOpen
QuantisOpen.argtypes = [QuantisDeviceType, c_uint, POINTER(POINTER(QuantisDeviceHandle))]
QuantisOpen.restype = c_int

QuantisClose = lib.QuantisClose
QuantisClose.argtypes = [POINTER(QuantisDeviceHandle)]
QuantisClose.restype = None

QuantisReadHandled = lib.QuantisReadHandled
QuantisReadHandled.argtypes = [POINTER(QuantisDeviceHandle), POINTER(None), c_size_t]
QuantisReadHandled.restype = c_int

QuantisRead = lib.QuantisRead
QuantisRead.argtypes = [QuantisDeviceType, c_uint, POINTER(None), c_size_t]
QuantisRead.restype = c_int

QuantisReadDouble_01 = lib.QuantisReadDouble_01
QuantisReadDouble_01.argtypes = [QuantisDeviceType, c_uint, POINTER(c_double)]
QuantisReadDouble_01.restype = c_int

QuantisReadFloat_01 = lib.QuantisReadFloat_01
QuantisReadFloat_01.argtypes = [QuantisDeviceType, c_uint, POINTER(c_float)]
QuantisReadFloat_01.restype = c_int

QuantisReadInt = lib.QuantisReadInt
QuantisReadInt.argtypes = [QuantisDeviceType, c_uint, POINTER(c_int)]
QuantisReadInt.restype = c_int

QuantisReadShort = lib.QuantisReadShort
QuantisReadShort.argtypes = [QuantisDeviceType, c_uint, POINTER(c_short)]
QuantisReadShort.restype = c_int

QuantisReadScaledDouble = lib.QuantisReadScaledDouble
QuantisReadScaledDouble.argtypes = [QuantisDeviceType, c_uint, POINTER(c_double), c_double, c_double]
QuantisReadScaledDouble.restype = c_int

QuantisReadScaledFloat = lib.QuantisReadScaledFloat
QuantisReadScaledFloat.argtypes = [QuantisDeviceType, c_uint, POINTER(c_float), c_float, c_float]
QuantisReadScaledFloat.restype = c_int

QuantisReadScaledInt = lib.QuantisReadScaledInt
QuantisReadScaledInt.argtypes = [QuantisDeviceType, c_uint, POINTER(c_int), c_int, c_int]
QuantisReadScaledInt.restype = c_int

QuantisReadScaledShort = lib.QuantisReadScaledShort
QuantisReadScaledShort.argtypes = [QuantisDeviceType, c_uint, POINTER(c_short), c_short, c_short]
QuantisReadScaledShort.restype = c_int

QuantisStrError = lib.QuantisStrError
QuantisStrError.argtypes = [QuantisError]
if sizeof(c_int) == sizeof(c_void_p):
    QuantisStrError.restype = ReturnString
else:
    QuantisStrError.restype = String
    QuantisStrError.errcheck = ReturnString     


class QUANTIS():
    
    def __init__(self, dev_type=QUANTIS_DEVICE_USB, dev_number=0):
        
        self.dev_type = dev_type
        self.dev_n = dev_number
        self.qdh = pointer(QuantisDeviceHandle())
        self.is_open = False
        
        if not QuantisCount(dev_type):
            print 'Quantis Error - please connect device'
            raise RuntimeError
            
        self.start()

    def __del__(self):
        self.close()
            
    def start(self):
        QuantisBoardReset(self.dev_type, self.dev_n)
        #time.sleep(.1)
        QuantisOpen(self.dev_type, self.dev_n, byref(self.qdh))
#        print res
#        if not res:
#            print 'Quantis Error starting device'
#            raise RuntimeError
#        else:
        #sn = QuantisGetSerialNumber(self.dev_type, self.dev_n)
        print 'Quantis - opening device'
        
        self.is_open = True
        
    def close(self):
        if self.is_open:
            QuantisClose(self.qdh)
            self.is_open = False
        
    def read(self, nbytes):
        if not self.is_open:
            print 'Quantis Error - please start device before reading'
            raise RuntimeError            
            
        raw_data=(c_ubyte * nbytes )()
        nread = QuantisReadHandled(self.qdh, raw_data, nbytes)
        if nread != nbytes:
            print 'Quantis Error - nbyes read is different from asked'
            raise ValueError
        array_data = np.array(raw_data)
        del raw_data
        return array_data
        
    def get_bits(self, nbits):
        nbytes = int(np.ceil(float(nbits)/8))
        int_data = self.read(nbytes)
        bit_data = int_data[:, np.newaxis] >> np.arange(8)[::-1] & 1
        bit_data = np.concatenate(bit_data)
        del int_data
        return bit_data[:nbits]
        
    def time_read(self, nbytes=10):
        t0 = time.time()
        self.read(nbytes)
        t1 = time.time()
        print t1-t0
        
    def test(self):
        pass
    
    def plot(self):
        pass
