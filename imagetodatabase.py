if __name__ != "__main__":
    import sqlite3,loctuple, perbackendconfig
    from PIL import Image

    #Configure file location for my system, modify it on yours
    perbackendconfig.configure()

    def createTables(inputimage,ext):
        print("Opening image and getting image data...")
        # Open image file
        file = inputimage+"."+ext
        img = Image.open(file)

        # Get the size of the image
        width,height = img.size
        print("Image size {} x {}".format(width,height))

        # Get the pixels
        pixels = img.load()

        print(width*height)

        print("Generating database...")

        # Connect to a database and create a connection object
        filedb = inputimage+" Pixel.db"

        conn = sqlite3.connect(filedb)

        # Create a cursor object
        cursor = conn.cursor()
        
        for hg in range(img.size[1]):
            print("creating image_row_{}...".format(hg+1))
            #Create Image row tables
            name = "image_row_"+str(hg+1)
            queryChild = f"CREATE TABLE {name}(id INTEGER PRIMARY KEY)"
            cursor.execute(queryChild)

            #ADD data_value column to table
            queryDataHeaderR = f"ALTER TABLE {name} ADD value_R"
            queryDataHeaderG = f"ALTER TABLE {name} ADD value_G"
            queryDataHeaderB = f"ALTER TABLE {name} ADD value_B"
            queryDataHeaderGray = f"ALTER TABLE {name} ADD value_Gray"

            cursor.execute(queryDataHeaderR)
            cursor.execute(queryDataHeaderG)
            cursor.execute(queryDataHeaderB)
            cursor.execute(queryDataHeaderGray)

            for wd in range(img.size[0]):
                #Insert the values to the data_value column
                value = str(pixels[wd,hg])
                modValue = loctuple.tupletolist(value)

                r = int(modValue[1])
                g = int(modValue[3])
                b = int(modValue[5])

                #Create rudimentary grayscale value
                gray = int((r+g+b)/3)
                
                queryData = f"INSERT INTO {name}(value_R,value_G,value_B,value_Gray) VALUES ({r},{g},{b},{gray})"
                cursor.execute(queryData)

        #Commit the changes to the database
        conn.commit()

        #Close the cursor and connection objects
        cursor.close()
        conn.close()

        print("Database generation completed")
