if __name__ != "__main__":
    from pathconfig import configure
    from cv2 import imread,Canny,cvtColor,imwrite,destroyAllWindows,waitKey,COLOR_RGB2GRAY,GaussianBlur,Sobel,CV_64F
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
            canny_image = f"{img_name} Egde_lines."+ext
            canny_image_loc = path.join(img_folder_path,canny_image)

            if not path.exists(canny_image_loc):
                #Read the image
                img = imread(img_file_path)
                #Gaussian blurred original image
                pre_g_blur = GaussianBlur(img,(5,5),2)
                #Convert it to grayscale
                gray = cvtColor(img, COLOR_RGB2GRAY) 
                #Gaussian blur the grayscale image for better edge detection
                post_g_blur = GaussianBlur(gray,(5,5),2)
                #Perform sobel edge detection
                sobelx = Sobel(post_g_blur,CV_64F,1,0,5)
                sobely = Sobel(post_g_blur,CV_64F,0,1,5)
                sobelxy = Sobel(post_g_blur,CV_64F,1,1,5)
                #Perform the canny edge detector to detect
                edges = Canny(post_g_blur,threshold1=50,threshold2=150)

                if(d_USE_GUI==True):
                    imshow(gray,cmap="gray")
                    show()
                    key = waitKey(1000)
                    imshow(pre_g_blur,cmap="gray")
                    show()
                    key = waitKey(1000)
                    imshow(post_g_blur,cmap="gray")
                    show()
                    key = waitKey(1000)
                    imshow(sobelx,cmap="gray")
                    show()
                    key = waitKey(1000)
                    imshow(sobely,cmap="gray")
                    show()
                    key = waitKey(1000)
                    imshow(sobelxy,cmap="gray")
                    show()
                    key = waitKey(1000)
                    imshow(edges,cmap="gray")
                    show()
                    key = waitKey(1000)

                    if key == 27:
                        destroyAllWindows()

                imwrite(grayscale_image_loc,gray)
                imwrite(pre_g_blur_image_loc,pre_g_blur)
                imwrite(post_g_blur_image_loc,post_g_blur)
                imwrite(canny_image_loc,edges)
                print(f"{grayscale_image} saved")
                print(f"{pre_g_blur_image} saved")
                print(f"{post_g_blur_image} saved")
                print(f"{canny_image} saved")

            else:
                print(f'{canny_image} already exists in {img_folder_path}')
                