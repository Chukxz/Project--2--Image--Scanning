import sqlite3,loctuple, perbackendconfig,os,math, numpy as np,time
from PIL import Image

#Configure file location for my system, modify it on yours
perbackendconfig.configure()
class EmptyString(UserWarning):...

parentdir = os.getcwd()

def expr(x,y,sigma,scale):
    # start = time.time()
    # Mean (mu) = 0, so it is not included in the variables,
    # but Standard deviation (sigma) is included

    base_expr = 1/(2*(math.pow(sigma,2))*math.pi)

    power_expr_x = math.pow(x,2)/math.pow(sigma,2)
    expr_x = math.pow(math.e,-power_expr_x)

    power_expr_y = math.pow(y,2)/math.pow(sigma,2)
    expr_y = math.pow(math.e,-power_expr_y)

    final_expr = scale * base_expr * expr_x * expr_y
    # end = time.time() - start
    # print(f'Time taken: {end} seconds')
    return final_expr

def kernel(kernel_size,sigma = 1, scale = 1):
    if kernel_size >= 0:
        if kernel_size %2 == 1:
            val = (kernel_size-1)/2
            row = []
            for i in range(kernel_size):
                column = []
                for j in range(kernel_size):
                    column.append(expr(i-val,j-val,sigma,scale))
                row.append(column)
            return row
        
def pixel_neighbourhood(x,y,width,height,gray,kernel_size=3,sigma=1,scale=1):
    values = kernel(kernel_size,sigma,scale)
    if kernel_size >= 0:
        if kernel_size %2 == 1:
            val = (kernel_size-1)/2
            row = []
            for j in range(kernel_size):
                val_y = j - val
                coord_y = val_y + y
                if coord_y>=0 or coord_y<height:
                    column = []
                    for i in range(kernel_size):
                        val_x = i - val
                        coord_x = val_x + x
                        if coord_x>=0 or coord_x<width:
                            column.append(gray*values[int(val_x)][int(val_y)])
                row.append(column)
            pixel_value = round(np.sum(row))
            return (int(pixel_value))

def createBlur():
    try:
        start = time.time()
        file = str(input('Input file: '))
        if file == '':
            raise EmptyString
        ext = str(input('Input file extension: '))
        if ext == '':
            raise EmptyString
        print(f'Time of input: {time.time()-start} seconds')
        start = time.time()
        grayScaleImgFile = file+' Grayscale.'+ext
        img_folder_path = os.path.join(parentdir,'Resources','Generated_Images',file)
        img_file_path = os.path.join(parentdir,'Resources','Generated_Images',file,grayScaleImgFile)
        g_blur_image = f"{file} G_Blur."+ext
        g_blur_image_loc = os.path.join(img_folder_path,g_blur_image)
        img = Image.open(img_file_path)

        filedb = os.path.join(img_folder_path,f' {file} Pixel.db')

        print("Opening image pixel database and getting database data...")

        conn = sqlite3.connect(filedb)
        cursor = conn.cursor()

        pixel_data = []
        
        for j in range (1):
            # print("Querying grayscale image data in image_row_{}...".format(i+1))
            name = "image_row_"+str(j+1)
            queryGrayScale = f"SELECT value_Gray FROM {name}"
            index = 0
            width = img.size[0]
            height = img.size[1]            
            # for row in cursor.execute(queryGrayScale):
            #     print(f'Creating pixel {index,j} for blurred Image')
            #     modrow = loctuple.tupletolist(row)
            #     p_value = pixel_neighbourhood(index,j,width,height,int(modrow[1]))
            #     index +=1
            #     pixel_value = (p_value,p_value,p_value)
            #     pixel_data.append(pixel_value)   
        
        conn.commit()
        cursor.close()
        conn.close()


        print(f'Saving{g_blur_image} in {g_blur_image_loc}')    
        #Create an new image with the desired dimensions
        image = Image.new('RGB',(img.size[0],img.size[1]))

        #Set the pixel values for the image
        image.putdata(pixel_data)

        #Save the image file
        image.save(g_blur_image_loc)

        print(f'Time taken: {time.time()-start} seconds')
    except EmptyString:
        print('Do not use empty strings')
    except BaseException as base_err:
        print(base_err)

createBlur()


# try:
#     start = time.time()
#     values = kernel(3,0.2)
#     print(values)
#     print(np.sum(values))
#     print(round(np.sum(values)))
# except NameError:
#     print('Only integers are allowed')
# finally:
#     print(f"Time taken : {time.time()-start}")

