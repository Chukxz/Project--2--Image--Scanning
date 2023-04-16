if __name__ != "__main__":
    import loctuple, perbackendconfig,os,math, numpy as np
    from PIL import Image

    #Configure img_name location for my system, modify it on yours
    perbackendconfig.configure()

    def expr(x,y,sigma,scale):
        # Mean (mu) = 0, so it is not included in the variables,
        # but Standard deviation (sigma) is included

        base_expr = 1/(2*(math.pow(sigma,2))*math.pi)

        power_expr_x = math.pow(x,2)/math.pow(sigma,2)
        expr_x = math.pow(math.e,-power_expr_x)

        power_expr_y = math.pow(y,2)/math.pow(sigma,2)
        expr_y = math.pow(math.e,-power_expr_y)

        final_expr = scale * base_expr * expr_x * expr_y
        return final_expr

    def kernel(kernel_size,sigma, scale):
        if kernel_size >=0 and kernel_size%2==1:
            val = (kernel_size-1)/2
            row = []
            for i in range(kernel_size):
                column = []
                for j in range(kernel_size):
                    column.append(expr(i-val,j-val,sigma,scale))
                row.append(column)
            return row
            
def createBlur(img_name,ext,img_folder_path,kernel_size=5,sigma=4.5, scale = 100):
        grayScaleImgFile = img_name+' Grayscale.'+ext
        img_file_path = os.path.join(img_folder_path,grayScaleImgFile)
        g_blur_image = f"{img_name} G_Blur."+ext
        g_blur_image_loc = os.path.join(img_folder_path,g_blur_image)

        if not os.path.exists(g_blur_image_loc):
            print("Opening grayscale image and getting image data...")
            img = Image.open(img_file_path)
            width,height = img.size
            pixels = img.load()
            pixel_data = []        
            kernel_set = kernel(kernel_size,sigma,scale)
            val = int((kernel_size-1)/2)
            
            if kernel_size>=0 and kernel_size<=min(width,height) and kernel_size%2==1:
                for hg in range(img.size[1]):
                    print(f'Generating blurred image row {hg+1}')
                    for wd in range(img.size[0]):       
                        row = []
                        for j in range(kernel_size):
                            column = []
                            val_x = int(j-val)
                            coord_x = val_x+wd
                            if coord_x<0:
                                coord_x = 0
                            elif coord_x>=width:
                                coord_x = width-1
                            for i in range(kernel_size):
                                val_y = int(i-val)
                                coord_y = val_y+hg
                                if coord_y<0:
                                    coord_y = 0
                                elif coord_y>=height:
                                    coord_y = height-1
                                column.append(loctuple.tupletolist(pixels[coord_x,coord_y])[0]*kernel_set[i][j])
                            row.append(column)
                        result = round(np.sum(row)/(math.pow(kernel_size,2)))
                        if result>255:
                            result = 255
                        pixel_value = (result,result,result)
                        pixel_data.append(pixel_value)

            print(f'Saving {g_blur_image} in {g_blur_image_loc}')    
            #Create an new image with the desired dimensions
            image = Image.new('RGB',(img.size[0],img.size[1]))

            #Set the pixel values for the image
            image.putdata(pixel_data)

            #Save the image img_name
            image.save(g_blur_image_loc)
        else:
            print(f'{g_blur_image_loc} already exists in {img_folder_path}')