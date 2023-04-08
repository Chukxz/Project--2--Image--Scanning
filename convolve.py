import imagetodatabase as imgdb,imagetograyscale as imggray,os,perbackendconfig as  perbconf,re

perbconf.configure()

def decide():
    input = str(input("Enter input (-h for more)"))


def help(input):
        if(input=="-h"):
            print("-")
            print("-h: basic help")
            print("-s: get image size")
            print("-g: apply")


def generate():
    supported_image_formats = ['jpg','webp','png']
    success = True

def todb(success):


def togray(supported_image_formats):
    print("Note supported grayscale image extensions are {}".format(supported_image_formats))

    

def run():
    try:
        inputimg = str(input("Enter image file to create pixel database for and process to grayscale (don't enter extension): "))
        ext = str(input('Enter the image file extenstion (.extension name eg. jpg for jpg image files): '))
        outputext = str(input("Input list of extensions for output files (eg. for jpg and png input 'jpg & png'): "))

        info = []

    except FileNotFoundError:
        success = False
        print("Please enter a file that exists")

    if(not(os.access(inputimg+"."+ext,0))):
        success = False

        info.append("File not found please check file extension and try again")
        print(info[0])

    if(success):
        if(not(os.access(inputimg+" Pixel.db",0))):
            dbsuccess = True
            imgdb.createTables(inputimg,ext)
        else:
            dbsuccess = False
            print(inputimg+" Pixel.db already exists")


        res = re.split(r'[\s][\&][\s)]',outputext)

        #verify that grayscale file format is supported
        def verify(verify,verifyier):
            sucList = []
            if len(verify)<=len(verifyier):
                for i in range(len(verify)):
                    if (verify[i] in verifyier):
                        sucList.append(True)
                    else:
                        sucList.append(False)

                if(all(sucList)):
                    return True
                else:
                    return False
                    
        verified = verify(supported_image_formats,res)

        if(verified):
            successList = []
            for i in range(len(res)):
                successList.append(res[i])
                if(not(os.access(inputimg+" Grayscale."+res[i],0))):
                    successList[i] = True
                    imggray.createGrayScaleFile(inputimg,ext,res[i])
                else:
                    successList[i] = False
                    print(inputimg+" Grayscale."+res[i]+" already exits")

        
        if(any(res)or dbsuccess):
            print("\n")
            print("Original image file: {}".format(inputimg+"."+ext))

        if(dbsuccess):
            print("Created database file for image: ".format(inputimg+" Pixel.db"))
            
        if(verified):
            for i in range(len(res)):
                if(successList[i]):
                    print("Created {} grayscale image file: ".format(res[i],inputimg+" Grayscale."+res[i]))
        else:
            print("One or more grayscale image extension(s) not supported, supported values are {}, check extension(s) and try again".format(supported_image_formats))
run()

