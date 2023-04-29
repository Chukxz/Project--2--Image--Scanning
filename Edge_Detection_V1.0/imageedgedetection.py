if __name__ != "__main__":
    from pathconfig import configure
    from PIL import Image, ImageFilter
    from matplotlib.pyplot import imshow, show
    from os import path

    #Configure location for my system, modify it on yours
    configure()

    def detectEdges(ext,img_folder_path,img_file_path,img_name,d_USE_GUI):
        grayscale_image = f"{img_name} Grayscale."+ext
        grayscale_image_loc = path.join(img_folder_path,grayscale_image)
        pre_g_blur_image = f"{img_name} Pre_G_Blur."+ext
        pre_g_blur_image_loc = path.join(img_folder_path,pre_g_blur_image)
        post_g_blur_image = f"{img_name} Post_G_Blur."+ext
        post_g_blur_image_loc = path.join(img_folder_path,post_g_blur_image) 
        edges_image = f"{img_name} Egde_lines."+ext
        edges_image_loc = path.join(img_folder_path,edges_image)

        if not path.exists(edges_image_loc):
            #Read the image
            img = Image.open(img_file_path)
            #Grayscale image
            gray = img.convert("L")
            #Gaussian blurred image
            pre_g_blur = img.filter(ImageFilter.GaussianBlur(2))
            #Gaussian blurred grayscale image
            post_g_blur = gray.filter(ImageFilter.GaussianBlur(2))
            #Detect edges
            edges = img.filter(ImageFilter.FIND_EDGES)

            if(d_USE_GUI==True):
                imshow(gray,cmap="gray")
                show()
                imshow(pre_g_blur,cmap="gray")
                show()
                imshow(post_g_blur,cmap="gray")
                show()
                imshow(edges,cmap="gray")
                show()

            gray.save(grayscale_image_loc)
            pre_g_blur.save(pre_g_blur_image_loc)
            post_g_blur.save(post_g_blur_image_loc)
            edges.save(edges_image_loc)
            print(f"{grayscale_image} saved")
            print(f"{pre_g_blur_image} saved")
            print(f"{post_g_blur_image} saved")
            print(f"{edges_image} saved")

        else:
            print(f'{edges_image} already exists in {img_folder_path}')
            