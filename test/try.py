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

#     This is our shell command

# p = subprocess.Popen("sh try.sh", stdout = subprocess.PIPE, shell=True,encoding='utf-8')

# print(p.communicate())


# my_f = my
# my_f.argtypes = [ctypes.POINTER(ctypes.c_char)]

# x = ctypes.c_char("Resources/Generated_Images/Colored_Wolf/Colored_Wolf Pixel.db")

# print(x)

# my_f(ctypes.byref(x))

# file = "Resources/Generated_Images/Pipe Puzzle/Pipe Puzzle Pixel.db";


# my_open = my.opensql
# my_open.argtypes = [ctypes.c_char]
# handle = ctypes.c_char(file)
# res = my_open(ctypes.byref(handle))



# print(util.find_library('./myfunc.c'))
# print(util.find_library('./myfunc.so'))

# import os,perbackendconfig as pb,ctypes,subprocess
# from ctypes import *
# from PIL import Image


# os.chdir("Resources/Generated_Images/Colored_Wolf")

# img = Image.open("Colored_Wolf.jpg")
# width,height = img.size

# os.chdir("../../../")

# print(os.getcwd(),width,height)

# with subprocess.Popen("sh try.sh", stdout = subprocess.PIPE, shell=True,encoding='utf-8') as proc:
#     print(proc.stdout.read())

# my_func = ctypes.CDLL(r'./myfunc.so')
# my_function = my_func.runsqlite3
# my_function.argtypes = [ctypes.c_int,ctypes.c_int]

# x = ctypes.c_int(width)
# y = ctypes.c_int(height)

# my_function(x,y)