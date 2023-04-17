# import re,perbackendconfig as pb,os,time,localfileoperations as lfo
# from PIL import Image

# class EmptyString(UserWarning):...

# pb.configure()

# parentdir = os.getcwd()

# def setImgFilePath(parentdir,inputimg,ext):
#     inputimg_file = inputimg + '.' + ext
#     img_file_path =os.path.join(parentdir,'Resources','Generated_Images',inputimg,inputimg_file)
#     return img_file_path

# def setImgFolderPath(parentdir,inputimg):
#     img_folder_path = os.path.join(parentdir,'Resources','Generated_Images',inputimg)
#     return img_folder_path

# def getImageSize():
#     try:
#         inputimg = str(input("Enter image file (don't enter extension): "))
#         if inputimg == '':
#             raise EmptyString
#         ext = str(input('Enter the image file extension (.extension name eg. jpg for jpg image files): '))
#         if ext == '':
#             raise EmptyString
#         start = time.time()
#         #Copy image to appropiate folder
#         lfo.copyimagefile(inputimg,ext)
#         #Set image path
#         img_path = setImgFilePath(parentdir,inputimg,ext)
#         # Open image file
#         img = Image.open(img_path)
#         print(img_path)
#         # Get the size of the image
#         width,height = img.size
#         print(f'Image size {width} x {height}')
#     except EmptyString:
#         print ('Do not use empty strings in input')
#     finally:
#         print(f"Total time taken: {time.time() - start} seconds")


# getImageSize()
import os,perbackendconfig as pb,ctypes
from ctypes import util
from ctypes import *

pb.configure()

parentdir = os.getcwd()

if not os.path.exists("./try.sh") or not os.path.exists("./myfunc.so"):
    import subprocess
    #This is our shell command

    # p = subprocess.Popen("sh try.sh", stdout = subprocess.PIPE, shell=True)

    # print(p.communicate())

    with subprocess.Popen("sh try.sh", stdout = subprocess.PIPE, shell=True) as proc:
        print(proc.stdout.read())

so_path = os.path.join(parentdir,"myfunc.so") 

example2 = CDLL('./myfunc.so')

print(type(example2))

print(util.find_library('myfunc.so'))
