#import os
# print(os.name," ",os.curdir," ",os.pardir," ",os.sep," ",os.linesep)


# arr1 = np.random.random(100000) #100k random values
# arr2 = np.random.random(100000) #100k random values

# arr1 = [1,2,3]
# arr2 = [4,5,6]

# #Faster in operation
# res1 = sg.fftconvolve(arr1,arr2)
# print("Done",res1,type(res1))


# # Slower in operation
# res2 = np.convolve(arr1,arr2)
# print("final",res2,type(res2))


#Convert to greyscale 
#Use gaussian blur
#Use Sobel edge detector in x and y direction
#Also get gradient and orientation
#Use canny edge

# #Define the pizel data
# pixel_data = [(255,0,0),(0,255,0),(0,0,255)]

# #Create an new image with the desired dimensions
# image = Image.new('RGB',(3,1))

# #Set the pixel values for the image
# image.putdata(pixel_data)

# #Save the image file
# image.save('test1.png')

# o = Image.open('test1.png')
# p = o.load()

# for i in range(o.size[0]):
#     for j in range(o.size[1]):
#         print(p[i,j])



# #get the column names from the Pixels table in the ImagePixelValue database
# table_name = 'Pixels'

# columns = []
# for row in conn.execute(f"PRAGMA table_info('{table_name}')"):
#     columns.append(row[1])

# new_values = ['hey','hi','there'] #Values to set

# i = 0
# for column in columns:
#     cursor.execute(f"UPDATE {table_name} SET {column} = ? WHERE id = ?",(new_values[i],1)) #Set
#     i+1



#Insert into database
# cursor.execute('''
#     INSERT INTO Pixels (name,email)
#     VALUES (?,?)
# ''',('John Doe','johndoe@example.com')
# )



# # Join tables
# def join(index):
#     name = "image_row_"+str(index)
#     nameId = name+'.id'
#     nameR = name+'.value_R'
#     nameG = name+'.value_G'
#     nameB = name+'.value_B'
#     queryJoin = f"""SELECT {nameId}, {nameR}, {nameG}, {nameB}
#     FROM Pixels
#     JOIN {name} ON Pixels.id = {nameId}"""
#     cursor.execute(queryJoin)
#     rows = cursor.fetchall()

#     for row in rows:
#         print(row[1],row[2],row[3])

# import re
# gray_scale_files = str(input("Input list of extensions for output files (eg. for jpg and png input 'jpg & png', do not repeat extensions!): "))

# supported_image_formats = ['jpg','webp','png']
# verify_list = re.split(r'[\s][\&][\s)]',gray_scale_files)

# print(verify_list)

import os,sqlite3,re
parentdir = os.getcwd()

def createSpImgExtFile():
    #Image extensions path
    sp_img_ext_name = 'Supported Image Extensions'
    sp_img_ext_loc = os.path.join(parentdir,sp_img_ext_name+'.db')
    default = ['jpg','png','webp']
    column_name = 'Extension List'
    if not os.path.exists(sp_img_ext_loc):
        # Connect to a database and create a connection object
        conn = sqlite3.connect(sp_img_ext_loc)
        # Create a cursor object
        cursor = conn.cursor()
        print("Generating database with default values")         
        create_table = f"CREATE TABLE {sp_img_ext_name}({column_name} TEXT)"
        cursor.execute(create_table)

        for i in default:
            queryI = f'INSERT  INTO {sp_img_ext_name} ({column_name})) VALUES ({i})'

        #Commit the changes to the database
        conn.commit()
        #Close the cursor and connection objects
        cursor.close()
        conn.close()

createSpImgExtFile()

def editSpImgExtFile(input_command):
    # createSpImgExtFile()
    sp_img_ext_name = 'Supported Image Extensions'
    sp_img_ext_loc = os.path.join(parentdir,sp_img_ext_name+'.db')
    generated_commands =  re.split(' ',input_command)

    print(generated_commands)


    if generated_commands[0] == 'remove' or generated_commands[0] == 'add': ...
    #         command = generated_commands[0]
    #         value = generated_commands[]
    #         # Connect to a database and create a connection object
    #         conn = sqlite3.connect(sp_img_ext_loc)
    #         # Create a cursor object
            
    #         cursor = conn.cursor()
    #         query = f'DELETE '

# editSpImgExtFile(str(input('Input Command : ')))
