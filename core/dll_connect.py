from ctypes import *
from win32api import LoadLibraryEx

from typing import Final

LOAD_WITH_ALTERED_SEARCH_PATH: Final[int] = 8
arraySize: Final[int] = 256
charset: Final[str] = 'utf-8'

dllName = r'../dll_lib.so'
dllHandle = LoadLibraryEx(dllName, 0, LOAD_WITH_ALTERED_SEARCH_PATH)
dllLib = WinDLL(dllName, handle = dllHandle)

class _COMPONENT(Structure):

    _fields_ = [('ID',              c_uint),
                ('TYPE',            c_char_p),
                ('NAME',            c_char_p),
                ('COUNT',           c_uint)]

class _PROJECT(Structure):

    _fields_ = [('ID',              c_uint),
                ('NAME',            c_char_p),
                ('PROCESSOR',       _COMPONENT),
                ('VIDEOCARD',       _COMPONENT),
                ('RAM',             _COMPONENT),
                ('RAM_COUNT',       c_uint),
                ('STORAGE_DEVICE', _COMPONENT),
                ('PRICE',           c_float)]

class _PRODUCT(Structure):

    _fields_ = [('ID',              c_uint),
                ('PROJECT',         _PROJECT),
                ('COUNT',           c_uint)]

class DATA(Structure):

    _fields_ = [('COMPONENTS',      _COMPONENT * arraySize),
                ('PROJECTS',        _PROJECT * arraySize),
                ('PRODUCTS',        _PRODUCT * arraySize)]

dllLib.GET_COMPONENT.argtypes = [
                                    c_uint,
                                    c_char_p,
                                    c_char_p,
                                    c_uint]
dllLib.GET_COMPONENT.restype = _COMPONENT

GET_COMPONENT = dllLib.GET_COMPONENT

dllLib.GET_PROJECT.argtypes = [
                                    c_uint,
                                    c_char_p,
                                    _COMPONENT,
                                    _COMPONENT,
                                    _COMPONENT,
                                    c_uint,
                                    _COMPONENT,
                                    c_float]
dllLib.GET_PROJECT.restype = _PROJECT

GET_PROJECT = dllLib.GET_PROJECT

dllLib.GET_PRODUCT.argtypes = [
                                    c_uint,
                                    _PROJECT,
                                    c_uint]
dllLib.GET_PRODUCT.restype = _PRODUCT

GET_PRODUCT = dllLib.GET_PRODUCT

dllLib.GET_DATA.argtypes = [
                                    _COMPONENT * arraySize,
                                    _PROJECT * arraySize,
                                    _PRODUCT * arraySize]
dllLib.GET_DATA.restype = DATA

GET_DATA = dllLib.GET_DATA