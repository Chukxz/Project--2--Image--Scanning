
import time,localfileoperations as lfo,os
from PIL import Image

def setImgFilePath(inputimg,ext):
    inputimg_file = inputimg + '.' + ext
    img_file_path =os.path.join('Resources','Generated_Images',inputimg,inputimg_file)
    return img_file_path

def setImgFolderPath(inputimg):
    img_folder_path = os.path.join('Resources','Generated_Images',inputimg)
    return img_folder_path


def package():
    inputimg = str(input("Enter image file (don't enter extension): "))
    ext = str(input('Enter the image file extension (.extension name eg. jpg for jpg image files): '))
    start = time.time()
    #Copy image to appropiate folder
    lfo.copyimagefile(inputimg,ext)
    #Set Image folder path
    img_folder_path = setImgFolderPath(inputimg)
    #Set image path
    img_path = setImgFilePath(inputimg,ext)
    # Open image file
    img = Image.open(img_path)
    # Get the size of the image
    width,height = img.size
    pixels = img.load()
    print(f'Image size {width} x {height}')
    return f"{width} {height}"


print(package())



