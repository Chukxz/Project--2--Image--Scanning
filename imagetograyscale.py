if __name__ != "__main__":
    import sqlite3,loctuple, perbackendconfig
    from PIL import Image

    #Configure file location for my system, modify it on yours
    perbackendconfig.configure()

    def createGrayScaleFile(inputimage,ext,outputext):
        print("Opening image and getting image data...")
        # Open image file
        file = inputimage+"."+ext
        img = Image.open(file)

        # Get the size of the image
        width,height = img.size
        print("Image size {} x {}".format(width,height))

        pixel_data = []

        filedb = inputimage+" Pixel.db"

        print("Opening image pixel database and getting database data...")

        conn = sqlite3.connect(filedb)
        cursor = conn.cursor()

        print("Generating grayscale image data...")
                
        pixel_data = []

        for i in range (height):
            print("Query grayscale image data in image_row_{}...".format(i+1))
            name = "image_row_"+str(i+1)

            queryGrayScale = f"SELECT value_Gray FROM {name}"
            cursor.execute(queryGrayScale)

            rows = cursor.fetchall()
            for row in rows:
                modrow = loctuple.tupletolist(row)
                pixel_value = (int(modrow[1]),int(modrow[1]),int(modrow[1]))
                pixel_data.append(pixel_value)     


        conn.commit()
        cursor.close()
        conn.close()

        print("Creating grayscale image with previously generated grayscale image data")

        #Create an new image with the desired dimensions
        image = Image.new('RGB',(width,height))

        #Set the pixel values for the image
        image.putdata(pixel_data)

        #Save the image file
        grayscaleimage = inputimage+" Grayscale."+outputext
        image.save(grayscaleimage)

        print("Grayscale image generation completed")