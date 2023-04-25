if __name__ != "__main__":
    import sqlite3,loctuple, perbackendconfig,os
    from PIL import Image

    #Configure file location for my system, modify it on yours
    perbackendconfig.configure()

    def createGrayScaleFile(image_folder_path,image_file_path,gray_scale_ext,img_name):
        grayscaleimage = f"{img_name} Grayscale."+gray_scale_ext
        grayscaleimageloc = os.path.join(image_folder_path,grayscaleimage)
        if not os.path.exists(grayscaleimageloc):
            print("Opening image and getting image data...")
            # Open image file
            img = Image.open(image_file_path)
            # Get the size of the image
            width,height = img.size
            print(f'Image size {width} x {height}')

            pixel_data = []

            filedb = os.path.join(image_folder_path,f'{img_name} Pixel.db')

            print("Opening image pixel database and getting database data...")

            conn = sqlite3.connect(filedb)
            cursor = conn.cursor()

            print("Generating grayscale image data...")
                    
            pixel_data = []

            for i in range (img.size[1]):
                # print(f'Querying grayscale image data in image_row_{i+1}...')   
                name = "image_row_"+str(i+1)

                queryGrayScale = f"SELECT value_Gray FROM {name}"

                for row in cursor.execute(queryGrayScale):
                    gray = loctuple.tupletolist(row)[0]
                    pixel_value = (gray,gray,gray)
                    pixel_data.append(pixel_value)    


            conn.commit()
            cursor.close()
            conn.close()

            print("Creating grayscale image with previously generated grayscale image data")

            #Create an new image with the desired dimensions
            image = Image.new('RGB',(img.size[0],img.size[1]))

            #Set the pixel values for the image
            image.putdata(pixel_data)   

            #Save the image file
            image.save(grayscaleimageloc)

            print("Grayscale image generation completed")
        else:
            print(f'{grayscaleimageloc} already exists in {image_folder_path}')