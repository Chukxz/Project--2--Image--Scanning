if __name__ != "__main__":

    import os,shutil,perbackendconfig as  perbconf

    perbconf.configure()

    parentdir = os.getcwd()
    intermediate_dir =  os.path.join(parentdir,'Resources','Generated_Images')

    def createchildfolder(dir_name):
        try:
            new_dir = os.path.join(intermediate_dir,dir_name)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
                if dir_name == '':
                    print(f'Created Generated_Images in {parentdir}\\Resources')
                else:
                    print(f'Created {dir_name} in {new_dir}')
            else:
                print(f'{new_dir} already exists')
        except OSError as error:
            print(error)

    def deletechildfolder(dir_name):
        try:
            new_dir = os.path.join(intermediate_dir,dir_name)
            if os.path.exists(new_dir):
                shutil.rmtree(new_dir)
                if dir_name == '':
                    print(f'Deleted Generated_Images in {parentdir}\\Resources')
                else:
                    print(f'Deleted {dir_name} in {new_dir}')
            else:
                print(f'{new_dir} does not exist')
        except OSError as error:
            print(error)

    def createchildfile(file_name,ext,dir_name=''):
        new_file = file_name+"."+ext
        if dir_name != '':
            createchildfolder(dir_name)
            dir_path = os.path.join(parentdir,'Resources','Generated_Images',dir_name,new_file)
        else:
            dir_path = os.path.join(parentdir,'Resources','Generated_Images',new_file)
        
        try:
            if not os.path.exists(dir_path):
                with open(dir_path,'w'):...
                print(f'Created {new_file} in {dir_path}')
            else:
                print(f'{dir_path} already exits')
        except Exception as e:
            print(f"An error occurred: {e}")

    def deletechildfile(file_name,ext,dir_name=''):
        delete_file = file_name+"."+ext
        if dir_name !='':
            dir_path = os.path.join(parentdir,'Resources','Generated_Images',dir_name,delete_file)
        else:
            dir_path = os.path.join(parentdir,'Resources','Generated_Images',delete_file)    
        try:
            if os.path.exists(dir_path):
                os.remove(dir_path)
                print(f"Deleted {delete_file} in {dir_path}")
            else:
                print(f'{dir_path} does not exist')
        except Exception as e:
            print(f"An error occured {e}")
                
    def copyimagefile(file_name,ext):
        full_file_name = file_name+"."+ext
        src_file_path = os.path.join(parentdir,'Resources','Images',full_file_name)
        dest_folder_path = os.path.join(parentdir,'Resources','Generated_Images',file_name)
        dest_file_path = os.path.join(dest_folder_path,full_file_name)

        try:
            if os.path.exists(src_file_path):
                if not os.path.exists(dest_folder_path):
                    createchildfolder(file_name)
                if not os.path.exists(dest_file_path):
                    shutil.copy(src_file_path,dest_file_path)
                    print(f'{full_file_name} copied successfully from {src_file_path} to {dest_file_path}')
                else:
                    print(f'{dest_file_path} already exists')               
            else:
                print(f'{src_file_path} does not exist')           
        except OSError as error:
            print(error)

    def listcontents(dir_path):
        try:
            contents = os.listdir(os.path.join(intermediate_dir,dir_path))
        except OSError as error:
            print(error)
            contents = None
        finally:
            return contents