if __name__ != "__main__":
    import sqlite3,loctuple, perbackendconfig,os
    from PIL import Image

    #Configure file location for my system, modify it on yours
    perbackendconfig.configure()

    def createTables(image_folder_path,image_file_path,img_name):
        filedb = os.path.join(image_folder_path,f' {img_name} Pixel.db')

        if not os.path.exists(filedb):
            print("Opening image and getting image data...")
            # Open image file
            img = Image.open(image_file_path)
            # Get the pixels
            pixels = img.load()

            print("Generating database...")

            # Connect to a database and create a connection object
            conn = sqlite3.connect(filedb)

            # Create a cursor object
            cursor = conn.cursor()
            
            for hg in range(img.size[1]):
                print(f'Creating image_row_{hg+1}...')
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
                    value = pixels[wd,hg]
                    modValue = loctuple.tupletolist(value)

                    r = modValue[0]
                    g = modValue[1]
                    b = modValue[2]

                    #Create rudimentary grayscale value
                    gray = round((r+g+b)/3)
                    
                    queryData = f"INSERT INTO {name}(value_R,value_G,value_B,value_Gray) VALUES ({r},{g},{b},{gray})"
                    cursor.execute(queryData)

            #Commit the changes to the database
            conn.commit()

            #Close the cursor and connection objects
            cursor.close()
            conn.close()

            print("Database generation completed")
        else:
            print(f'{filedb} already exists in {image_folder_path}')