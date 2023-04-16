import imagetodatabase as imgdb,imagetograyscale as imggray,perbackendconfig as  perbconf,re,localfileoperations as lfo,os,time,imagetogaussianblur as imggblur
from PIL import Image

perbconf.configure()

#Create error classes inheriting from the built in UserWarning class
class NoresmatchWarning(UserWarning): ...
class ExcessiveresfindallWarning(UserWarning): ...
class NotinvallistWarning(UserWarning): ...
class NoresValue(UserWarning): ...
class ExitProgram(UserWarning): ...
class NotexactlyvallistWarning(UserWarning): ...
class EmptyString(UserWarning): ...
class ExtensionNotSupported(UserWarning):...

parentdir = os.getcwd()

perbconf.configure()

lfo.deletechildfolder('aurora')

#get input
def myinput():
    input_str = str(input("Enter input ('-h' for help or 'exit' to exit program): "))
    return input_str

#check validity of input and generate errors as neccessary
class MatchIt:
    def __init__(self,input,vallist=['h','s','d','g','w','b','e','c','m']):
        self.input = input
        self.res = ''

        if self.input == 'exit':
            raise ExitProgram

        resmatch = re.match(r'-',self.input)
        if resmatch == None:
            raise NoresmatchWarning
        
        resfindall = re.findall(r"-",self.input)
        if resfindall.count("-")>1:
            raise ExcessiveresfindallWarning
        
        self.res = re.sub("-",'',self.input)
        if self.res == '':
            raise NoresValue
        else:
            if self.input[1] not in vallist:
                raise NotinvallistWarning
            else:
                ret = None
                res = re.match(r'(\w\s*)\Z',self.res)
                for i in  range(len(vallist)):
                    if res:
                        val = self.res[0]                            
                        if val == vallist[i]:
                            ret = i
                if ret == None:
                    raise NotexactlyvallistWarning


    def res_value(self):
        return self.res  

#work on errors generated in validating input if any and display the error cause and suggestions for troubleshooting
def check(value,vallist=['h','s','d','g','w','b','e','c']):
    localvalue = re.match('(-|\s)*\w',value)
    if localvalue != None:
        premodlocalvalue = re.split('',str(localvalue.group()))
        modlen = len(premodlocalvalue)
        modlocalvalue = premodlocalvalue[modlen-2].lower()
        for i in vallist:
            if modlocalvalue == i:
                return i            
    else:
        return None

#handle input and all associated errors, error causes and suggestion for trouble shooting if any and return final input value for further processing
def handleinput(value):
        try:
            MatchIt(value).res_value()
            return value[1]
        except NoresmatchWarning:
            res = check(value)
            if(res!=None):
                print(f'Command not found : {value}\n Did you mean -{res} ?'.format())
            else:
                print(f'Invalid input\nCommand not found : {value}')
        except ExcessiveresfindallWarning:
            res = check(value)
            if(res!=None):
                print(f'Command not found : {value}\n Did you mean -{res} ?')
            else:
                print(f'Invalid input\nCommand not found : {value}')           
        except NoresValue:
            print(f'Invalid input\nCommand not found : {value}')
        except NotinvallistWarning:
            res = check(value)
            if(res!=None):
                print(f'Command not found : {value}\n Did you mean -{res} ?')
            else:
                print(f'Invalid input\nCommand not found : {value}')
        except NotexactlyvallistWarning:
                res = check(value)
                print(f'Command not found : {value}\n Did you mean -{res} ?')
        except ExitProgram:
            raise ExitProgram
        except :
            return None

#main helper function: display help information
def  help():
    start = time.time()
    print("   -h  basic help\n\
             -s  get image size\n\
             -d  generate database file\n\
             -g  generate grayscale in specified formats\n\
             -w  generate gaussian blur without grayscale\n\
             -b  generate gaussian blur with grayscale (recommended if file is to be used for further image processing)\n\
             -e  generate sobel edge detection image\n\
             -c  generate canny edge image\n\
             -u  use GUI interface\n\
             -m modify supported image extensions list e.g to add 'jiff' and , input 'add jiff', to remove 'jiff', input 'remove jiff'\n\
             to add or remove multiple extensions e.g two extensions 'jiff' and 'gif', input 'add jiff gif' or input 'remove jiff gif' respecively.\n\
             Note: default image extensions are .jpg, .webp and .png and they cannot be modified by adding or removing e.g 'add jpg' or 'remove jpg'\
             will not work.")
    print(f"Total time taken: {time.time() - start} seconds")


def setImgFilePath(parentdir,inputimg,ext):
    inputimg_file = inputimg + '.' + ext
    img_file_path =os.path.join(parentdir,'Resources','Generated_Images',inputimg,inputimg_file)
    return img_file_path

def setImgFolderPath(parentdir,inputimg):
    img_folder_path = os.path.join(parentdir,'Resources','Generated_Images',inputimg)
    return img_folder_path
    
def getImageSize():
    try:
        inputimg = str(input("Enter image file (don't enter extension): "))
        if inputimg == '':
            raise EmptyString
        ext = str(input('Enter the image file extension (.extension name eg. jpg for jpg image files): '))
        if ext == '':
            raise EmptyString
        start = time.time()
        #Copy image to appropiate folder
        lfo.copyimagefile(inputimg,ext)
        #Set image path
        img_path = setImgFilePath(parentdir,inputimg,ext)
        # Open image file
        img = Image.open(img_path)
        # Get the size of the image
        width,height = img.size
        print(f'Image size {width} x {height}')
    except EmptyString:
        print ('Do not use empty strings in input')
    finally:
        print(f"Total time taken: {time.time() - start} seconds")


def genDatabaseFile():
    try:
        inputimg = str(input("Enter image file (don't enter extension): "))
        if inputimg == '':
            raise EmptyString
        ext = str(input('Enter the image file extension (.extension name eg. jpg for jpg image files): '))
        if ext == '':
            raise EmptyString
        start = time.time()
        #Copy image to appropiate folder
        lfo.copyimagefile(inputimg,ext)
        #Set Image folder path
        img_folder_path = setImgFolderPath(parentdir,inputimg)
        #Set image path
        img_file_path = setImgFilePath(parentdir,inputimg,ext)
        #Create database file
        imgdb.createTables(img_folder_path,img_file_path,inputimg)
    except EmptyString:
        print ('Do not use empty strings in input')
    except BaseException as base_err:
        print(base_err)
    finally:
        print(f"Total time taken: {time.time() - start} seconds")


def createSpImgExtFile():
    #Image extensions path
    sp_img_ext_name = "Supported Image Extensions"
    sp_img_ext_loc = os.path.join(parentdir, f'{sp_img_ext_name}.txt')
    default = ['jpg','png','webp']

    if not os.path.exists(sp_img_ext_loc):
        try:
            with open(sp_img_ext_loc,'w') as extF:
                for i in default:
                    extF.write(f'{i}\n')
        except BaseException as base_err:
            print(base_err)

  
def editSpImgExtFile(input_command):
    start = time.time()
    createSpImgExtFile()
    default = ['jpg','png','webp']
    sp_img_ext_name = 'Supported Image Extensions.txt'
    sp_img_ext_loc = os.path.join(parentdir,sp_img_ext_name)
    generated_commands =  re.split(' ',input_command)

    store = []
    deletes = []

    if generated_commands[0] == 'delete' or generated_commands[0] == 'add':
        try:
            with open(sp_img_ext_loc,'r') as extF:
                num = extF.readlines()
                for i in num:
                    val = re.sub('\n','',i)
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

        except BaseException as err:
            print(err)
    print(f"Total time taken: {time.time() - start} seconds")

def getSpImgExt():
    sp_img_ext_name = 'Supported Image Extensions.txt'
    sp_img_ext_loc = os.path.join(parentdir,sp_img_ext_name)
    store = []
    try:
        with open(sp_img_ext_loc,'r') as extF:
            num = extF.readlines()
            for i in num:
                val = re.sub('\n','',i)
                store.append(val)
            return store
    except BaseException as err:
        print(err)

def verify(initial_verify_list,verifyier_list):
    sucList = []
    #Convert to set to remove repeating values
    verify_set = set(initial_verify_list)
    #convert back to list for further computing
    verify_list = [value for value in verify_set]

    if len(verify_list)<=len(verifyier_list):
        for i in range(len(verify_list)):
            if (verify_list[i] in verifyier_list):
                sucList.append(True)
            else:
                sucList.append(False)

        if(all(sucList)):
            return True
        else:
            return False
    else:
        return False

def genGrayScaleFiles():
    try:
        inputimg = str(input("Enter image file (don't enter extension): "))
        if inputimg == '':
            raise EmptyString
        ext = str(input('Enter the image file extension (.extension name eg. jpg for jpg image files): '))
        if ext == '':
            raise EmptyString
        print(f'Supported input list of extensions are {getSpImgExt()}')
        gray_scale_files = str(input("Input choice of extensions for output files (eg. for jpg and png input 'jpg & png'): "))
        if gray_scale_files == '':
            raise EmptyString
        start = time.time()
        #Copy image to appropiate folder
        lfo.copyimagefile(inputimg,ext)
        #Set Image folder path
        img_folder_path = setImgFolderPath(parentdir,inputimg)
        #Set image path
        img_file_path = setImgFilePath(parentdir,inputimg,ext)  
        #Create database file
        imgdb.createTables(img_folder_path,img_file_path,inputimg)
        verify_list = re.split(r'[\s][\&][\s)]',gray_scale_files)
        #Verify that grayscale file format is supported
        verified = getSpImgExt()
        #Create grayscale image files
        for i in range(len(verify_list)):
            if (verify_list[i] in verified):
                imggray.createGrayScaleFile(img_folder_path,img_file_path,verify_list[i],inputimg)
            else:
                raise ExtensionNotSupported
    except EmptyString:
        print ('Do not use empty strings in input')
    except ExtensionNotSupported:
        print(f'{verify_list[i]} grayscale image extension not supported, supported values are {getSpImgExt()}, check extensions and try again')
    except BaseException as base_err:
        print(base_err)
    finally:
        print(f"Total time taken: {time.time() - start} seconds")

def genGaussianBlurFile():
    try:
        inputimg = str(input('Input file: '))
        if inputimg == '':
            raise EmptyString
        ext = str(input('Input file extension: '))
        if ext == '':
            raise EmptyString
        start = time.time()
        #Copy image to appropiate folder
        lfo.copyimagefile(inputimg,ext)
        #Set Image folder path
        img_folder_path = setImgFolderPath(parentdir,inputimg)
        #Set image path
        img_file_path = setImgFilePath(parentdir,inputimg,ext)  
        #Create database
        imgdb.createTables(img_folder_path,img_file_path,inputimg)
        #Verify that grayscale file format is supported
        verified = getSpImgExt()
        #Create grayscale image files
        if (ext in verified):
            imggray.createGrayScaleFile(img_folder_path,img_file_path,ext,inputimg)
        else:
            raise ExtensionNotSupported
        imggblur.createBlur(inputimg,ext,img_folder_path)
    except EmptyString:
        print ('Do not use empty strings in input')
    except ExtensionNotSupported:
        print(f'{ext} grayscale image extension not supported, supported values are {getSpImgExt()}, check extensions and try again')
    except BaseException as base_err:
        print(base_err)
    finally:
        print(f"Total time taken: {time.time() - start} seconds")


#combine all main helper functions to form a coherent output
def organize():
    start = time.time()
    try:
        common = handleinput(myinput())
        if common == "h":
            print('>>')
            help()
        elif common == 's':
            getImageSize()
        elif common == 'd':
            genDatabaseFile()
        elif common == 'g':
            genGrayScaleFiles()
        elif common == 'b':
            genGaussianBlurFile()
        elif common == 'm':
            editSpImgExtFile(str(input('Input Command : ')))
        print(f"Total time spent in cycle: {time.time() - start} seconds")
        organize()
    except ExitProgram:
        print("Program exited")
        print(f"Total time spent in cycle: {time.time() - start} seconds")
organize()