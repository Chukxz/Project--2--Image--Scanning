# V 2.0, uses PIL (Python Imaging Library) and OpenCV (Open Computer Vision)

#This is the only place letter 'q' occurs in this program for now :)
from pathconfig import configure
from os import path
from re import sub,match,findall,split
from time import time
from imageedgedetection import detectEdges
from PIL import Image
from localfileoperations import copyimagefile, deletechildfolder

#Create error classes inheriting from the built in UserWarning class
class NoResMatchWarning(UserWarning): ...
class ExcessiveResFindallWarning(UserWarning): ...
class NotInVallistWarning(UserWarning): ...
class NoResValue(UserWarning): ...
class ExitProgram(UserWarning): ...
class NotExactlyVallistWarning(UserWarning): ...
class EmptyString(UserWarning): ...
class ImageExtensionNotSupported(UserWarning):...
class BrokenImageFile(UserWarning):...
class InvalidGUIExpression(UserWarning):...
class FolderNotFoundError(UserWarning):...

#Configure location for my system, modify it on yours
configure()

int_dir = path.join('Edge_Detection_V2.0','Resources','Generated_Images')

#Get input
def myinput():
    input_str = str(input("Enter input ('-h' for help or 'exit' to exit program): "))
    return input_str

#Check validity of input and generate errors as neccessary
class MatchIt:
    def __init__(self,input,vallist=['h','s','e','c','m','n','d']):
        self.input = input
        self.res = ''

        if self.input == 'exit':
            raise ExitProgram

        resmatch = match(r'-',self.input)
        if resmatch == None:
            raise NoResMatchWarning
        
        resfindall = findall(r"-",self.input)
        if resfindall.count("-")>1:
            raise ExcessiveResFindallWarning
        
        self.res = sub("-",'',self.input)
        if self.res == '':
            raise NoResValue
        else:
            if self.input[1] not in vallist:
                raise NotInVallistWarning
            else:
                ret = None
                res = match(r'(\w\s*)\Z',self.res)
                for i in  range(len(vallist)):
                    if res:
                        val = self.res[0]                            
                        if val == vallist[i]:
                            ret = i
                if ret == None:
                    raise NotExactlyVallistWarning

    def res_value(self):
        return self.res  

#Work on errors generated in validating input if any and display the error cause and suggestions for troubleshooting
def check(value,vallist=['h','s','e','c','m','n','d']):
    localvalue = match('(-|\s)*\w',value)
    if localvalue != None:
        premodlocalvalue = split('',str(localvalue.group()))
        modlen = len(premodlocalvalue)
        modlocalvalue = premodlocalvalue[modlen-2].lower()
        for i in vallist:
            if modlocalvalue == i:
                return i            
    else:
        return None

#Handle input and all associated errors, error causes and suggestion for trouble shooting if any and return final input value for further processing
def handleinput(value):
        try:
            MatchIt(value).res_value()
            return value[1]
        
        except NoResMatchWarning:
            res = check(value)
            if(res!=None):
                print(f'Command not found : {value}\n Did you mean -{res} ?'.format())
            else:
                print(f'Invalid input\nCommand not found : {value}')
        except ExcessiveResFindallWarning:
            res = check(value)
            if(res!=None):
                print(f'Command not found : {value}\n Did you mean -{res} ?')
            else:
                print(f'Invalid input\nCommand not found : {value}')           
        except NoResValue:
            print(f'Invalid input\nCommand not found : {value}')
        except NotInVallistWarning:
            res = check(value)
            if(res!=None):
                print(f'Command not found : {value}\n Did you mean -{res} ?')
            else:
                print(f'Invalid input\nCommand not found : {value}')
        except NotExactlyVallistWarning:
                res = check(value)
                print(f'Command not found : {value}\n Did you mean -{res} ?')
        except ExitProgram:
            raise ExitProgram
        except BaseException as base_err:
            print(base_err)

#Main helper function: display help information
def  help():
    start = time()
    print("\
             -h  basic help\n\
             -s  get image size\n\
             -e  generate edge detection image\n\
             -c  create a copy of the image with a different extension\n\
             -m  modify supported image extensions list e.g to add 'jiff' and , input 'add jiff', to remove 'jiff', input 'remove jiff'\n\
             -n  modify previous image extensions list e.g to add 'jiff' and , input 'add jiff', to remove 'jiff', input 'remove jiff'\n\
             to add or remove multiple extensions e.g two extensions 'jiff' and 'gif', input 'add jiff gif' or input 'remove jiff gif' respecively.\n\
             Note: default image extensions are .jpg, .webp and .png and they cannot be modified by adding or removing e.g 'add jpg' or 'remove jpg'\n\
             will not work.\n\
             -d  delete image folder")

    print(f"Total time taken: {time() - start} seconds")

def setImgFilePath(inputimg,ext):
    inputimg_file = inputimg + '.' + ext
    img_file_path = path.join(int_dir,inputimg,inputimg_file)
    return img_file_path

def setImgFolderPath(inputimg):
    img_folder_path = path.join(int_dir,inputimg)
    return img_folder_path

def createSpImgExtFile():
    #Image extensions path
    sp_img_ext_name = "Supported_Image_Extensions.txt"
    sp_img_ext_loc = path.join(int_dir,sp_img_ext_name)
    default = ['jpg','png','webp']

    if not path.exists(sp_img_ext_loc):
        try:
            with open(sp_img_ext_loc,'w') as extF:
                for i in default:
                    extF.write(f'{i}\n')
        except BaseException as base_err:
            print(base_err)
  
def editSpImgExtFile(input_command):
    start = time()
    default = ['jpg','png','webp']
    sp_img_ext_name = 'Supported_Image_Extensions.txt'
    sp_img_ext_loc = path.join(int_dir,sp_img_ext_name)
    generated_commands =  split(' ',input_command)

    if not path.exists(sp_img_ext_loc):
        createSpImgExtFile()

    store = []
    deletes = []

    if generated_commands[0] == 'delete' or generated_commands[0] == 'add':
        try:
            with open(sp_img_ext_loc,'r') as extF:
                num = extF.readlines()
                for i in num:
                    val = sub('\n','',i)
                    store.append(val)

            if generated_commands[0] == 'add':
                pre_store_set = set(store)
                for i in range(len(generated_commands)-1):
                    store.append(generated_commands[i+1])
                store_set = set(store)
                store_list = list(pre_store_set)
                val = list(store_set.difference(pre_store_set))

                for h in range(len(store_list)):
                    if store_list[h] in default:
                        print(f'Not able to add {store_list[h]} as it is a default value')
                    elif store_list[h] not in default:
                        print(f'{store_list[h]} already exists in {sp_img_ext_loc}')

                if val:
                    with open(sp_img_ext_loc,'a') as extF:
                        for k in range(len(val)):
                                extF.write(f'{val[k]}\n')
                                print(f'Added {val[k]} to {sp_img_ext_loc}')

            if generated_commands[0] == 'delete':
                for i in range(len(generated_commands)-1):
                    if generated_commands[i+1] in store:
                        if not generated_commands[i+1] in default:
                            indexVal = store.index(generated_commands[i+1])
                            deletes.append(store.pop(indexVal))
                with open(sp_img_ext_loc,'w') as extF:
                    for j in store:
                        if j != len(store)-1:
                            extF.write(f'{j}\n')
                        else:
                            extF.write(j)
                for i in deletes:
                    print(f'Deleted {i} in {sp_img_ext_loc}')
                for j in store:
                    if j in generated_commands and j in default:
                        print(f'Not able to delete {j} as it is a default value')
                for k in generated_commands:
                    if k not in deletes:
                        if k in generated_commands and not k in default and k != 'delete':
                            print(f'{k} not found in {sp_img_ext_loc}')                    

        except BaseException as base_err:
            print(base_err)
    print(f"Total time taken: {time() - start} seconds")

def getSpImgExt():
    sp_img_ext_name = 'Supported_Image_Extensions.txt'
    sp_img_ext_loc = path.join(int_dir,sp_img_ext_name) 

    if not path.exists(sp_img_ext_loc):
        createSpImgExtFile()
        
    store = []
    try:
        with open(sp_img_ext_loc,'r') as extF:
            num = extF.readlines()
            for i in num:
                val = sub('\n','',i)
                store.append(val)
            return store
    except BaseException as base_err:
        print(base_err)

def editPvImgExtFile(input_command):
    start = time()
    try:
        inputimg = str(input("Enter image file (don't enter extension): "))
        if inputimg == '':
            raise EmptyString
        
        pv_img_ext_name = 'Previous_Image_Extensions.txt'
        pv_img_ext_loc = path.join(int_dir,inputimg,pv_img_ext_name)

        if not path.exists(pv_img_ext_loc):
            with open(pv_img_ext_loc) as pv:...

        generated_commands =  split(' ',input_command)
        store = []
        deletes = []

        if generated_commands[0] == 'delete' or generated_commands[0] == 'add':
            with open(pv_img_ext_loc,'r') as extF:
                num = extF.readlines()
                for i in num:
                    val = sub('\n','',i)
                    store.append(val)

            if generated_commands[0] == 'add':
                pre_store_set = set(store)
                for i in range(len(generated_commands)-1):
                    store.append(generated_commands[i+1])
                store_set = set(store)
                store_list = list(pre_store_set)
                val = list(store_set.difference(pre_store_set))

                for h in range(len(store_list)):
                        print(f'{store_list[h]} already exists in {pv_img_ext_loc}')

                if val:
                    with open(pv_img_ext_loc,'a') as extF:
                        for k in range(len(val)):
                                extF.write(f'{val[k]}\n')
                                print(f'Added {val[k]} to {pv_img_ext_loc}')

            if generated_commands[0] == 'delete':
                for i in range(len(generated_commands)-1):
                    if generated_commands[i+1] in store:
                        indexVal = store.index(generated_commands[i+1])
                        deletes.append(store.pop(indexVal))
                with open(pv_img_ext_loc,'w') as extF:
                    for j in store:
                        if j != len(store)-1:
                            extF.write(f'{j}\n')
                        else:
                            extF.write(j)
                for i in deletes:
                    print(f'Deleted {i} in {pv_img_ext_loc}')
                for j in generated_commands:
                    if j not in deletes:
                        if j in generated_commands and j != 'delete':
                            print(f'{j} not found in {pv_img_ext_loc}') 

    except EmptyString:
        print ('Do not use empty strings in input')
    except BaseException as base_err:
        print(base_err)
    print(f"Total time taken: {time() - start} seconds")

def getPvImgExt(inputimg):
    pv_img_ext_name = 'Previous_Image_Extensions.txt'
    pv_img_ext_loc = path.join(int_dir,inputimg,pv_img_ext_name)
    store = []

    if not path.exists(pv_img_ext_loc):
        file = open(pv_img_ext_loc,'w')
        file.close()
    try:
        with open(pv_img_ext_loc,'r') as extF:
            num = extF.readlines()
            for i in num:
                val = sub('\n','',i)
                store.append(val)
        return store
    except BaseException as base_err:
        print(base_err)
    
def getImageSize():
    try:
        inputimg = str(input("Enter image file (don't enter extension): "))
        if inputimg == '':
            raise EmptyString
        ext = str(input('Enter the image file extension (extension name eg. jpg for jpg image files): '))
        if ext == '':
            raise EmptyString
        start = time()
        #Copy image to appropiate folder
        copyimagefile(inputimg,ext)
        #Set image path
        img_path = setImgFilePath(inputimg,ext)
 
        #Check if image exists
        if not path.exists(img_path):
            raise FileNotFoundError
        
        # Open image file              
        img = Image.open(img_path)
        #Verify that image is not broken
        if not img.verify() == None:
            raise BrokenImageFile
        #Reopen image file
        img = Image.open(img_path)
        # Get the size of the image
        width,height = img.size
        print(f'Image size {width} x {height}')
        print(f"Total time taken: {time() - start} seconds")
    except FileNotFoundError as err:
        print(err)
    except EmptyString:
        print ('Do not use empty strings in input')
    except BrokenImageFile:
        #Reopen image file
        img = Image.open(img_path)
        print(img.verify())
        deletechildfolder(inputimg) 
    except BaseException as base_err:
        print(base_err)   

def DeleteChildFolder():
    try:
        inputimg = str(input("Enter image file folder: "))
        if inputimg == '':
            raise EmptyString

        start = time()

        #Set image folder path
        img_folder_path = setImgFolderPath(inputimg)
 
        #Check if image exists
        if not path.exists(img_folder_path):
            raise FolderNotFoundError
        
        deletechildfolder(inputimg)
        print(f"Total time taken: {time() - start} seconds")
    except FolderNotFoundError:
        print(f"{img_folder_path} does not exist")
    except EmptyString:
        print ('Do not use empty strings in input')
    except BaseException as base_err:
        print(base_err)

def convertImg():
    try:
        inputimg = str(input("Enter image file (don't enter extension): "))
        if inputimg == '':
            raise EmptyString
        ext = str(input('Enter the image file extension (.extension name eg. jpg for jpg image files): '))
        if ext == '':
            raise EmptyString
        print(f'Supported input list of extensions are {getSpImgExt()}')
        output_ext = str(input("Input choice of extensions for output files (eg. for jpg and png input 'jpg & png'): "))
        if output_ext == '':
            raise EmptyString
        
        start = time()

        pv_img_ext_name = 'Previous_Image_Extensions.txt'
        pv_img_ext_loc = path.join(int_dir,inputimg,pv_img_ext_name)

        with open(pv_img_ext_loc,"w") as f:
            f.write(f'{ext}\n');      

        img_file = inputimg + '.' + ext
        img_folder_path = path.join('Resources','Images')
        img_file_path = path.join(img_folder_path,img_file)

        #Check if image exists
        if not path.exists(img_file_path):
            raise FileNotFoundError
        
        #Open image file                
        img = Image.open(img_file_path)
        #Verify that image is not broken 
        if not img.verify() == None:
            raise BrokenImageFile
        #Get inputted output extensions
        verify_list = split(r'[\s][\&][\s)]',output_ext)
        #Verify that image file format is supported
        verified = getSpImgExt()
        #Verify that image has not been created before with the specified image format
        confirm_ext = getPvImgExt(inputimg)
        #Create grayscale image files
        for i in range(len(verify_list)):
            if (verify_list[i] in verified):
                if verify_list[i] not in confirm_ext:
                    with open(path.join(int_dir,inputimg,'Previous_Image_Extensions.txt'),"a") as file:
                        file.write(verify_list[i]+'\n')
                    new_img = Image.open(img_file_path)
                    new_img_file_path = path.join(img_folder_path,inputimg)+"."+verify_list[i]
                    new_img.save(new_img_file_path)
                else:
                    print(f"{inputimg}.{verify_list[i]} already exists in Resources/Images")           
            else:
                raise ImageExtensionNotSupported

        print(f"Total time taken: {time() - start} seconds")
    except FileNotFoundError as err:
        print(err)
    except EmptyString:
        print ('Do not use empty strings in input')
    except ImageExtensionNotSupported:
        print(f'{verify_list[i]} image extension not supported, supported values are {getSpImgExt()}, check extensions and try again')
    except BrokenImageFile:
        #Reopen image file
        img = Image.open(img_file_path)
        print(img.verify())
        deletechildfolder(inputimg) 
        img = Image.open()
    except BaseException as base_err:
        print(base_err)

def genEdges():
    try:
        d_USE_GUI = False
        inputimg = str(input('Input file: '))
        if inputimg == '':
            raise EmptyString
        ext = str(input('Input file extension: '))
        if ext == '':
            raise EmptyString
        usegui = str(input('Use GUI ? [y/n or '']: '))
        if usegui == 'y':
            d_USE_GUI = True
        elif usegui == 'n' or usegui == '':
            d_USE_GUI = False
        else:
            raise InvalidGUIExpression
        start = time()
        #Copy image to appropiate folder
        copyimagefile(inputimg,ext)
        #Set Image folder path
        img_folder_path = setImgFolderPath(inputimg)
        #Set image path
        img_file_path = setImgFilePath(inputimg,ext)
        
        #Check if image exists
        if not path.exists(img_file_path):
            raise FileNotFoundError
        
        #Open image file             
        img = Image.open(img_file_path)
        #Verify that image is not broken
        if not path.exists(img_file_path):
            raise FileNotFoundError 
        if not img.verify() == None:
            raise BrokenImageFile
        #Verify that image file format is supported
        verified = getSpImgExt()
        #Create image with edges enhanced
        if (ext in verified):
            detectEdges(ext,img_folder_path,img_file_path,inputimg,d_USE_GUI)
        else:
            raise ImageExtensionNotSupported
        print(f"Total time taken: {time() - start} seconds")
    except FileNotFoundError as err:
        print(err)
    except EmptyString:
        print ('Do not use empty strings in input')
    except ImageExtensionNotSupported:
        print(f"{ext} image extension not supported, supported values are {getSpImgExt()}, check extensions and try again")
    except BrokenImageFile:
        #Reopen image file
        img = Image.open(img_file_path)
        print(img.verify())
        deletechildfolder(inputimg) 
        img = Image.open()
    except InvalidGUIExpression:
        print(f"{usegui} is not a valid expression")
    except BaseException as base_err:
        print(base_err)   

#Combine all main helper functions to form a coherent output
def organize():
    start = time()
    try:
        common = handleinput(myinput())
        if common == 'h':
            print('>>')
            help()
        elif common == 's':
            getImageSize()
        elif common == 'c':
            convertImg()
        elif common == 'm':
            editSpImgExtFile(str(input('Input Command : ')))
        elif common == 'n':
            editPvImgExtFile(str(input('Input Command : ')))
        elif common == 'e':
            genEdges()
        elif common == 'd':
            DeleteChildFolder()
        print(f"Total time spent in cycle: {time() - start} seconds")
        organize()
    except ExitProgram:
        print("Program exited")
        print(f"Total time spent in cycle: {time() - start} seconds")

organize()
