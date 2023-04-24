import ctypes, subprocess,os,perbackendconfig as pb
from _ctypes import*

pb.configure()

def create_database(image_pixel_width,image_pixel_height):

    with subprocess.Popen("sh database.sh",stdout=subprocess.PIPE,shell=True,encoding="utf-8") as file:
        print(file.stdout.read())
    
    database = ctypes.CDLL(r"database.exe")
    initiate_database = database.createDatabase
    initiate_database.argtypes = [ctypes.c_int,ctypes.c_int]

    width = ctypes.c_int(image_pixel_width)
    height = ctypes.c_int(image_pixel_height)

    os.chdir("Resources/Generated_Images/Colored_Wolf")

    print(os.getcwd())

    initiate_database(width,height)

    # os.chdir("../../../")

    print(os.getcwd())

create_database(480,480)