        if(not(os.access(inputimg+" Pixel.db",0))):
            dbsuccess = True
            imgdb.createTables(inputimg,ext)
        else:
            dbsuccess = False
            print(inputimg+" Pixel.db already exists")

        
        res = re.split(r'[\s][\&][\s)]',outputext)
        print(len(res),res[0])
        # successList = []
        # for i in range(len(res)):   
        #     if(not(os.access(inputimg+" Grayscale."+res[i-1],0))):
        #         successList[i] = True
        #         imggray.createGrayScaleFile(inputimg,ext,outputext)
        #     else:
        #         successList[i] = False
        #         print(inputimg+" Grayscale.jpg already exits")

        # print(successList)
        
        # if(success):
        #     print("\n\n\n")
        #     print("Original image file: {}\nCreated database file for image: ".format(inputimg+"."+ext,inputimg+" Pixel.db\n"))
            
        # for i in range(len(res)):
        #     if(successList[i-1]):
        #         print("Created {} grayscale image file: ".format({res[i-1]},inputimg+" Grayscale."+{res[i-1]}))