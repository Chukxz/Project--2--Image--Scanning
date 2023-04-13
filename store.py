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

# import os,sqlite3,re, perbackendconfig

# perbackendconfig.configure()

# parentdir = os.getcwd()

# def createSpImgExtFile():
#     #Image extensions path
#     sp_img_ext_name = "Supported Image Extensions"
#     sp_img_ext_loc = os.path.join(parentdir, f'{sp_img_ext_name}.txt')
#     default = ['jpg','png','webp']

#     if not os.path.exists(sp_img_ext_loc):
#         try:
#             with open(sp_img_ext_loc,'w') as extF:
#                 for i in default:
#                     extF.write(f'{i}\n')
#         except BaseException as err:
#             print(err)

  
# def editSpImgExtFile(input_command):
#     createSpImgExtFile()
#     default = ['jpg','png','webp']
#     sp_img_ext_name = 'Supported Image Extensions.txt'
#     sp_img_ext_loc = os.path.join(parentdir,sp_img_ext_name)
#     generated_commands =  re.split(' ',input_command)

#     store = []
#     deletes = []

#     if generated_commands[0] == 'delete' or generated_commands[0] == 'add':
#         try:
#             with open(sp_img_ext_loc,'r') as extF:
#                 num = extF.readlines()
#                 for i in num:
#                     val = re.sub('\n','',i)
#                     store.append(val)

#             if generated_commands[0] == 'add':
#                 pre_store_set = set(store)
#                 for i in range(len(generated_commands)-1):
#                     store.append(generated_commands[i+1])
#                 store_set = set(store)
#                 store_list = list(pre_store_set)
#                 val = list(store_set.difference(pre_store_set))

#                 for h in range(len(store_list)):
#                     if store_list[h] in default:
#                         print(f'Not able to add {store_list[h]} as it is a default value')
#                     elif store_list[h] not in default:
#                         print(f'{store_list[h]} already exists in {sp_img_ext_loc}')

#                 if val:
#                     with open(sp_img_ext_loc,'a') as extF:
#                         for k in range(len(val)):
#                                 extF.write(f'{val[k]}\n')
#                                 print(f'Added {val[k]} to {sp_img_ext_loc}')

#             if generated_commands[0] == 'delete':
#                 for i in range(len(generated_commands)-1):
#                     if generated_commands[i+1] in store:
#                         if not generated_commands[i+1] in default:
#                             indexVal = store.index(generated_commands[i+1])
#                             deletes.append(store.pop(indexVal))
#                 with open(sp_img_ext_loc,'w') as extF:
#                     for j in store:
#                         if j != len(store)-1:
#                             extF.write(f'{j}\n')
#                         else:
#                             extF.write(j)
#                 for i in deletes:
#                     print(f'Deleted {i} in {sp_img_ext_loc}')
#                 for j in store:
#                     if j in generated_commands and j in default:
#                         print(f'Not able to delete {j} as it is a default value')
#                 for k in generated_commands:
#                     if k not in deletes:
#                         if k in generated_commands and not k in default and k != 'delete':
#                             print(f'{k} not found in {sp_img_ext_loc}')                    

#         except BaseException as err:
#             print(err)

# editSpImgExtFile(str(input('Input Command : ')))

# def getSpImgExt():
#     sp_img_ext_name = 'Supported Image Extensions.txt'
#     sp_img_ext_loc = os.path.join(parentdir,sp_img_ext_name)
#     store = []
#     try:
#         with open(sp_img_ext_loc,'r') as extF:
#             num = extF.readlines()
#             for i in num:
#                 val = re.sub('\n','',i)
#                 store.append(val)
#             return store
#     except BaseException as err:
#         print(err)

