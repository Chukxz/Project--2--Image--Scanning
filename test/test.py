import ctypes,subprocess,os
from ctypes import *


def show():

    with subprocess.Popen("sh test.sh", stdout = subprocess.PIPE, shell=True,encoding='utf-8') as proc:
        print(proc.stdout.read())
        

    test = ctypes.CDLL(r'./test.so')
    my_func = test.runsqlite3
    my_func.argtypes = [ctypes.c_int,ctypes.c_int]

    x = ctypes.c_int(488)
    y = ctypes.c_int(232)

    my_func(x,y)

show()

# with subprocess.Popen("sh runtest.sh", stdout = subprocess.PIPE, shell=True,encoding='utf-8') as proc:
#     print(proc.stdout.read())




