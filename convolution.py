import imagetodatabase as imgdb,imagetograyscale as imggray,perbackendconfig as  perbconf,re,localfileoperations as lfo,os,sqlite3
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

parentdir = os.getcwd()

#get input
def myinput():
    input_str = str(input("Enter input ('-h' for help or 'exit' to exit program): "))
    return input_str

#check validity of input and generate errors as neccessary
class MatchIt:
    def __init__(self,input,vallist=['h','s','d','g','w','b','e','c']):
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
                print("Command not found : {}\n Did you mean -{} ?".format(value,res))
            else:
                print("Invalid input\nCommand not found : {}".format(value))
        except ExcessiveresfindallWarning:
            res = check(value)
            if(res!=None):
                print("Command not found : {}\n Did you mean -{} ?".format(value,res))
            else:
                print("Invalid input\nCommand not found : {}".format(value))           
        except NoresValue:
            print("Invalid input\nCommand not found : {}".format(value))
        except NotinvallistWarning:
            res = check(value)
            if(res!=None):
                print("Command not found : {}\n Did you mean -{} ?".format(value,res))
            else:
                print("Invalid input\nCommand not found : {}".format(value))
        except NotexactlyvallistWarning:
                res = check(value)
                print("Command not found : {}\n Did you mean -{} ?".format(value,res))
        except ExitProgram:
            raise ExitProgram
        except :
            return None

#main helper function: display help information
def help():
    print("   -h  basic help\n   -s  get image size\n   -d  generate database file\n   -g  generate grayscale in specified formats\n   -w  generate gaussian blur without grayscale\n   -b  generate gaussian blur with grayscale (recommended if file is to be used for further image processing)\n   -e  generate sobel edge detection image\n   -c  generate canny edge image\n   -u  use GUI interface\n   Note: image output formats are in .jpg, .webp and .png")

def setImgFilePath(parentdir,inputimg,ext):
    inputimg_file = inputimg + '.' + ext
    img_file_path =os.path.join(parentdir,'Resources','Generated_Images',inputimg,inputimg_file)
    return img_file_path

def setImgFolderPath(parentdir,inputimg):
    img_folder_path = os.path.join(parentdir,'Resources','Generated_Images',inputimg)
    return img_folder_path

def createSpImgExtFile():
    #Image extensions path
    sp_img_ext_name = 'Supported Image Extensions'
    sp_img_ext_loc = os.path.join(parentdir,sp_img_ext_name+'.db')
    default = ['jpg','png','webp']
    if not os.path.exists(sp_img_ext_loc):
        conn = sqlite3.connect(sp_img_ext_loc)
        cursor = conn.cursor()          
        query = f"CREATE TABLE {sp_img_ext_name}(id INTEGER PRIMARY KEY)"
        cursor.execute(query)
        #Commit the changes to the database
        conn.commit()
        #Close the cursor and connection objects
        cursor.close()
        conn.close()


def editSpImgExtFile(input_command):
    createSpImgExtFile()
    generated_commands =  re.split(' ',input_command)

    if generated_commands[0] == 'remove':...






    
def getImageSize():
    try:
        inputimg = str(input("Enter image file (don't enter extension): "))
        if inputimg == '':
            raise EmptyString
        ext = str(input('Enter the image file extension (.extension name eg. jpg for jpg image files): '))
        if ext == '':
            raise EmptyString
            #copy image to appropiate folder
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


def genDatabaseFile():
    try:
        inputimg = str(input("Enter image file (don't enter extension): "))
        if inputimg == '':
            raise EmptyString
        ext = str(input('Enter the image file extension (.extension name eg. jpg for jpg image files): '))
        if ext == '':
            raise EmptyString 
        #copy image to appropiate folder
        lfo.copyimagefile(inputimg,ext)
        #Set Image folder path
        img_folder_path = setImgFolderPath(parentdir,inputimg)
        #Set image path
        img_file_path = setImgFilePath(parentdir,inputimg,ext)
        #Create database
        imgdb.createTables(img_folder_path,img_file_path,inputimg)
    except EmptyString:
        print ('Do not use empty strings in input') 

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
        gray_scale_files = str(input("Input list of extensions for output files (eg. for jpg and png input 'jpg & png'): "))
        if gray_scale_files == '':
            raise EmptyString
        #copy image to appropiate folder
        lfo.copyimagefile(inputimg,ext)
        #Set Image folder path
        img_folder_path = setImgFolderPath(parentdir,inputimg)
        #Set image path
        img_file_path = setImgFilePath(parentdir,inputimg,ext)  
        #Create database
        imgdb.createTables(img_folder_path,img_file_path,inputimg)
        verify_list = re.split(r'[\s][\&][\s)]',gray_scale_files)
        #verify that grayscale file format is supported
        verified = verify(supported_image_extensions,verify_list)
        #Create grayscale files
        if(verified):
            for i in range(len(verify_list)):
                imggray.createGrayScaleFile(img_folder_path,img_file_path,verify_list[i],inputimg)
        else:
            print(f'One or more grayscale image extension(s) not supported, supported values are {supported_image_extensions}, check extension(s) and try again')

    except EmptyString:
        print ('Do not use empty strings in input')    

#combine all main helper functions to form a coherent output
def organize():
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

            organize()
        except ExitProgram:
            print("Program exited")

organize()