if __name__ != "__main__":
    from perbackendconfig import configure
    from PIL import Image, ImageFilter
    from os import path

    #Configure img_name location for my system, modify it on yours
    configure()

    def detectEdges(ext,img_folder_path,img_file_path,img_name):
            edge_image = f"{img_name} Egde_lines."+ext
            edge_image_loc = path.join(img_folder_path,edge_image)
            if not path.exists(edge_image_loc):
                img = Image.open(img_file_path)
                edge = img.filter(ImageFilter.FIND_EDGES)
                edge.save(edge_image_loc)  
                print(f"{edge_image} saved")    
            else:
                print(f'{edge_image} already exists in {img_folder_path}')
