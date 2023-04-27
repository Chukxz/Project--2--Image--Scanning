if __name__ != "__main__":

    from PIL import Image
    from os import path, makedirs, remove, listdir
    import shutil,perbackendconfig as  perbconf

    perbconf.configure()

    intermediate_dir =  path.join('Resources','Generated_Images')

    def createchildfolder(dir_name):
        try:
            new_dir = path.join(intermediate_dir,dir_name)
            if not path.exists(new_dir):
                makedirs(new_dir)
                if dir_name == '':
                    print(f'Created Generated_Images in Resources')
                else:
                    print(f'Created {dir_name} in {new_dir}')
            else:
                print(f'{new_dir} already exists')
        except OSError as error:
            print(error)

    def deletechildfolder(dir_name):
        try:
            delete_dir = path.join(intermediate_dir,dir_name)
            if path.exists(delete_dir):
                shutil.rmtree(delete_dir)
                if dir_name == '':
                    print(f'Deleted Generated_Images in Resources')
                else:
                    print(f'Deleted {dir_name} in {delete_dir}')
            else:
                print(f'{delete_dir} does not exist')
        except OSError as error:
            print(error)

    def createchildfile(file_name,ext,dir_name=''):
        new_file = file_name+"."+ext
        if dir_name != '':
            createchildfolder(dir_name)
            dir_path = path.join('Resources','Generated_Images',dir_name,new_file)
        else:
            dir_path = path.join('Resources','Generated_Images',new_file)
        
        try:
            if not path.exists(dir_path):
                with open(dir_path,'w'):...
                print(f'Created {new_file} in {dir_path}')
            else:
                print(f'{dir_path} already exits')
        except Exception as e:
            print(f"An error occurred: {e}")

    def deletechildfile(file_name,ext,dir_name=''):
        delete_file = file_name+"."+ext
        if dir_name !='':
            dir_path = path.join('Resources','Generated_Images',dir_name,delete_file)
        else:
            dir_path = path.join('Resources','Generated_Images',delete_file)    
        try:
            if path.exists(dir_path):
                remove(dir_path)
                print(f"Deleted {delete_file} in {dir_path}")
            else:
                print(f'{dir_path} does not exist')
        except Exception as e:
            print(f"An error occured {e}")
                
    def copyimagefile(file_name,ext):
        full_file_name = file_name+"."+ext
        resized_img_file_name = file_name+"R."+ext
        src_file_path = path.join('Resources','Images',full_file_name)
        resized_img_path = path.join('Resources','Images',resized_img_file_name)
        dest_folder_path = path.join('Resources','Generated_Images',file_name)
        dest_file_path = path.join(dest_folder_path,full_file_name)

        try:
            if path.exists(src_file_path):
                if not path.exists(dest_folder_path):
                    createchildfolder(file_name)
                if not path.exists(dest_file_path):
                    #Resize Image to 400 X 400 pixels to reduce space
                    img = Image.open(src_file_path)
                    width, height = img.size

                    conversion_factor = max(width,height)/480
                    with open("conv_factor.txt","w") as conv_f:
                        conv_f.write(str(conversion_factor))

                    new_width = int(width/conversion_factor)
                    new_height = int(height/conversion_factor)

                    resized_img = img.resize([new_width,new_height])
                    resized_img.save(resized_img_path)

                    shutil.copy(resized_img_path,dest_file_path)
                    remove(resized_img_path)
                    print(f'{full_file_name} copied successfully from {src_file_path} to {dest_file_path}')
                else:
                    print(f'{dest_file_path} already exists')               
            else:
                print(f'{src_file_path} does not exist')           
        except OSError as error:
            print(error)

    def listcontents(dir_path):
        try:
            contents = listdir(path.join(intermediate_dir,dir_path))
        except OSError as error:
            print(error)
            contents = None
        finally:
            return contents