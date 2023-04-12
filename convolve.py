import imagetodatabase as imgdb,imagetograyscale as imggray,os,perbackendconfig as  perbconf,re,localfileoperations

perbconf.configure()


# def decide():
#     takeinput = True
#     while takeinput:
#         input = str(input("Enter input (-h for more)"))


   

def run():
    try:
        inputimg = str(input("Enter image file to create pixel database for and process to grayscale (don't enter extension): "))
        ext = str(input('Enter the image file extenstion (.extension name eg. jpg for jpg image files): '))
        outputext = str(input("Input list of extensions for output files (eg. for jpg and png input 'jpg & png'): "))

    except FileNotFoundError:
        success = False
        print("Please enter a file that exists")


    supported_image_formats = ['jpg','webp','png']
    print(f'Note supported grayscale image extensions are {supported_image_formats}')

    if(not(os.access(inputimg+"."+ext,0))):
        success = False

    if(success):
        if(not(os.access(inputimg+" Pixel.db",0))):
            dbsuccess = True
            imgdb.createTables(inputimg,ext)
        else:
            dbsuccess = False

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
            print(f'Original image file: {inputimg+"."+ext}')

        if(dbsuccess):
            print(f'Created database file for image: {inputimg+" Pixel.db"}')
            
        if(verified):
            for i in range(len(res)):
                if(successList[i]):
                    print(f'Created {res[i],inputimg+" Grayscale."+res[i]} grayscale image file: ')
        else:
            print(f'One or more grayscale image extension(s) not supported, supported values are {supported_image_formats}, check extension(s) and try again')

run()

